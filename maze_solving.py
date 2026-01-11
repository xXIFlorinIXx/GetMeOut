import pygame
import classes
import heapq
from draw import *
from settings import *
from random import shuffle, randint
import time

path = {}

def no_dead_ends(maze: dict[tuple[int, int], classes.Cell]):

    start = (0, 0)
    final = (settings.lines - 1, settings.rows -1)
    start_left = (0, settings.rows - 1)
    final_left = (settings.lines -1, 0)

    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    dir = [0, 1, 2, 3]
    Bdir = {0:1, 1:0, 2:3, 3:2}

    for key in maze:

        if key in [start, final, start_left, final_left]:
            continue
        
        cnt_wall = 0
        for wall_state in maze[key].walls:
            if wall_state:
                cnt_wall += 1 

        if cnt_wall >= 3:
            shuffle(dir)

            y, x = key
            for d in dir:
                ny, nx = y + dy[d], x + dx[d]
                if (ny >= 0  and ny < settings.lines) and (nx >= 0 and nx < settings.rows):
                    maze[key].walls[d] = False
                    maze[(ny, nx)].walls[Bdir[d]] = False
                    break

def unvisit_maze(maze: dict[tuple[int, int], classes.Cell]):
    path.clear()
    for key in maze.keys():
        maze[key].visited = False
        maze[key].exit_path = False

#Alg euristic
# Pun biscuiti pe unde am fost de fiecare data cand intru intr-o celula, in momentul in care ajung intr-o intersectie ma uit in ce directie sunt cei mai putin biscuiti si ma duc dupa ei,
# Daca pe drum vad ca am o celula fara biscuiti ma duc in celula respetiva, reiau tot procesul pana ajung la final (Larisa)
def rezolva_labirintul_cu_biscuiti(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface):
    pass

def mark_path_to_exit(start_x: int, start_y: int, final_x: int, final_y:int, path: dict, maze: dict[tuple[int, int], classes.Cell]):

    start = (0, 0)
    final = (settings.lines - 1, settings.rows -1)
    final_y, final_x = final
    start_y, start_x = start

    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    Ry, Rx = start_y, start_x
    maze[(Ry,Rx)].exit_path = True
   
    cnt = 0
    while (Ry, Rx) != (final_y, final_x):
        
        cnt += 1
        if (Ry, Rx) not in path:
            break
        else:
            dir_to = path[(Ry,Rx)]
        
        Ry = Ry + dy[dir_to]
        Rx = Rx + dx[dir_to]

        maze[(Ry,Rx)].exit_path = True
    
    print('-----', cnt)

#1 Random mouse algorithm
def Random_mouse(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animation: bool = False):

    start = (0, 0)
    final = (settings.lines - 1, settings.rows -1)
    final_y, final_x = final
    start_y, start_x = start

    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    Bdir = {0:1, 1:0, 2:3, 3:2}
    dir = [0, 1, 2, 3]
    coords = []

    cy, cx = start_y, start_x
    dir_to = None

    if animation:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()
    
    while (cy, cx) != (final_y, final_x):
        
        shuffle(dir)

        check_events()
        if animation:
            maze[(cy,cx)].highlite = True
            maze[(cy,cx)].draw(settings.rect, surface)
            coords.append((cx,cy))
            maze[(cy,cx)].highlite = False
            pygame.display.update(get_rect_for(coords))
            settings.clock.tick(tick_solving)
            coords.clear()

        cnt_walls = 0
        for wall_state in maze[(cy,cx)].walls: 
            if wall_state:
                cnt_walls += 1
                
        for d in dir:
            if (maze[(cy,cx)].walls[d] == False and (dir_to == None or d != Bdir[dir_to])) or (cnt_walls == 3 and maze[(cy,cx)].walls[d] == False):
                dir_to = d
                break

        maze[(cy,cx)].visited = True
        if animation:
            maze[(cy,cx)].draw(settings.rect, surface)
            coords.append((cx,cy))
        cy, cx = cy + dy[dir_to], cx + dx[dir_to]

    maze[(cy,cx)].visited = True
        
    mark_path_to_exit(start_x, start_y, final_x, final_y, path, maze)

#2 Hand-on-wall rule
#2.1 right-hand rule
def Right_Hand_on_wall(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animation: bool = False):

    start = (0, 0)
    final = (settings.lines - 1, settings.rows -1)
     
    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    Rdir = {2:1, 1:3, 3:0, 0:2}
    dir = [1,2,0,3] #S, E, N, W

    cy, cx = start
    index = 0
    dir_to = dir[index]

    if animation:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()

    while (cy, cx) != final:

        if maze[(cy,cx)].walls[Rdir[dir_to]] == False:
            dir_to = Rdir[dir_to]
            index = dir.index(dir_to)
        else:
            while maze[(cy,cx)].walls[dir_to] == True:
                index = (index + 1) % 4
                dir_to = dir[index]

        path[(cy,cx)] = dir_to
        maze[(cy,cx)].exit_path = True

        check_events()
        if animation:
            maze[(cy,cx)].draw(settings.rect, surface)
            pygame.display.update(get_rect_for([(cx,cy)]))
            settings.clock.tick(tick_solving)

        cy, cx = cy + dy[dir_to], cx + dx[dir_to]
    
    maze[(cy,cx)].exit_path = True
                     
#2.1 left-hand rule  
def Left_Hand_on_wall(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animation: bool = False):

    start_left = (0, settings.rows - 1)
    final_left = (settings.lines -1, 0)
     
    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    Ldir = {1:2, 2:0, 0:3, 3:1}
    dir = [1,3,0,2] #S, W, N, E
    settings.lines = settings.settings.lines
    settings.rows = settings.settings.rows

    cy, cx = start_left
    index = 0
    dir_to = dir[index]

    if animation:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()

    while (cy, cx) != final_left:
        
        if maze[(cy,cx)].walls[Ldir[dir_to]] == False:
            dir_to = Ldir[dir_to]
            index = dir.index(dir_to)
        else:
            while maze[(cy,cx)].walls[dir_to] == True:
                index = (index + 1) % 4
                dir_to = dir[index]

        check_events()
        path[(cy,cx)] = dir_to
        maze[(cy,cx)].exit_path = True
        
        if animation:
            maze[(cy,cx)].draw(settings.rect, surface)
            pygame.display.update(get_rect_for([(cx,cy)]))
            settings.clock.tick(tick_solving)

        cy, cx = cy + dy[dir_to], cx + dx[dir_to]
    
    maze[(cy,cx)].exit_path = True
                     
#Dead-end filling
def Dead_end_filling(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animation: bool = False):

    start = (0, 0)
    final = (settings.lines - 1, settings.rows -1)

    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    dir = [0, 1, 2, 3]
    settings.lines = settings.settings.lines
    settings.rows = settings.settings.rows

    maze[start].walls[0] = False
    maze[final].walls[1] = False

    if animation:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()

    for key in maze:
        
        if maze[key].visited:
            continue

        cnt_wall = 0
        for wall_state in maze[key].walls:
            if wall_state:
                cnt_wall += 1

        ok = False
        if cnt_wall >= 3 and key != start and key != final:
            ok = True

        y, x = key
        while ok:

            check_events()
            maze[(y,x)].visited = True
            if animation:
                maze[(y,x)].draw(settings.rect, surface)
                pygame.display.update(get_rect_for([(x,y)]))
                settings.clock.tick(tick_solving)

            for d in dir:
                ny, nx = y + dy[d], x + dx[d]
                if maze[(y,x)].walls[d] == False and not maze[(ny,nx)].visited:
                    cnt_wall = 0
                    cnt = 0
                    for wall_state in maze[(ny,nx)].walls:
                        zy = ny + dy[cnt]
                        zx = nx + dx[cnt]
                        if wall_state: 
                            cnt_wall += 1
                        elif (zy,zx) != (y,x) and (zy >= 0 and zy < settings.lines) and (zx >= 0 and zx < settings.rows) and maze[(zy, zx)].visited:
                            cnt_wall += 1
                        cnt += 1

                    if cnt_wall > 1:
                        y, x = ny, nx
                        break
                    else:
                        ok = False
                        break

                if cnt_wall >= 4:
                    break
        
        check_events()
        
    maze[start].walls[0] = True
    maze[final].walls[1] = True

#BFS
def BFS(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animation: bool = False):

    start = (0, 0)
    final = (settings.lines - 1, settings.rows -1)
    final_y, final_x = final
    start_y, start_x = start
    
    visited = []
    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    Bdir = {0:1, 1:0, 2:3, 3:2}
    dir = [0, 1, 2, 3]

    if animation:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()

    for _ in range(settings.lines):
        line = []
        for __ in range(settings.rows):
            line.append(0)
        visited.append(line)
    
    #FIFO
    coords = []
    queue = []
    path = {}

    y, x = start
    queue.append((y,x))
    visited[y][x] = 1
    
    while queue:
        y, x = queue.pop(0)
        maze[(y,x)].visited = True
    
        if (y, x) == final:
            mark_path_to_exit(final_x, final_y, start_x, start_y,  path, maze)
            return 1

        check_events()
        if animation:
            maze[(y,x)].highlite = True
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))
            maze[(y,x)].highlite = False
            pygame.display.update(get_rect_for(coords))
            settings.clock.tick(tick_solving)
            coords.clear()

        for d in dir:
            ny, nx = y + dy[d], x + dx[d]

            if not maze[(y,x)].walls[d] and not visited[ny][nx]:
                path[(ny,nx)] = Bdir[d]
                queue.append((ny,nx))
                visited[ny][nx] = 1

        if animation:
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))

    return -1
        
#DFS
def DFS(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animation: bool = False):

    start = (0, 0)
    final = (settings.lines - 1, settings.rows -1)
    final_y, final_x = final
    start_y, start_x = start
    
    visited = []
    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    Bdir = {0:1, 1:0, 2:3, 3:2}
    dir = [0, 1, 2, 3]

    if animation:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()

    for _ in range(settings.lines):
        line = []
        for __ in range(settings.rows):
            line.append(0)
        visited.append(line)
    
    #LIFO
    coords = []
    stack = []
    path = {}

    y, x = start
    stack.append((y,x))
    visited[y][x] = 1

    while stack:
        y, x = stack.pop()
        maze[(y,x)].visited = True

        if (y, x) == final:
            mark_path_to_exit(final_x, final_y, start_x, start_y,  path, maze)  
            return 1
        
        check_events()
        if animation:
            maze[(y,x)].highlite = True
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))
            maze[(y,x)].highlite = False
            pygame.display.update(get_rect_for(coords))
            settings.clock.tick(tick_solving)  
            coords.clear()

        for d in dir:
            ny, nx = y + dy[d], x + dx[d]

            if not maze[(y,x)].walls[d] and not visited[ny][nx]:
                path[(ny,nx)] = Bdir[d]
                stack.append((ny,nx))
                visited[ny][nx] = 1

        if animation:
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))
         
    return -1

def A_star(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animation: bool = False):

    

    def Manhattan_distance(x1: int, y1: int, x2: int, y2:int):
        return abs(x1 - x2) + abs(y1 - y2)

    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    Bdir = {0:1, 1:0, 2:3, 3:2}
    dir = [0, 1, 2, 3]

    if animation:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()

    coords = []
    heap = []
    path = {}
    gScore = {}
    fScore = {}

    heapq.heapify(heap)
    y_end, x_end = settings.lines - 1, settings.rows - 1
    y_start, x_start = 0, 0

    inf = 999999999
    for key in maze:
        gScore[key] = inf
        fScore[key] = inf

    gScore[(y_start, x_start)] = 0
    fScore[(y_start, x_start)] = Manhattan_distance(x_start, y_start, x_end, y_end)
    heapq.heappush(heap, (Manhattan_distance(x_start, y_start, x_end, y_end), Manhattan_distance(x_start, y_start, x_end, y_end), (y_start, x_start)))
    
    while heap:
        old_dist, _, (y, x) = heapq.heappop(heap)
        maze[(y,x)].visited = True

        if (y, x) == (y_end, x_end):
            mark_path_to_exit(x_end, y_end, x_start, y_start, path, maze)
            return 1

        if old_dist > fScore[(y,x)]:
            continue

        check_events()
        if animation:
            maze[(y,x)].highlite = True
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))
            maze[(y,x)].highlite = False
            pygame.display.update(get_rect_for(coords))
            settings.clock.tick(tick_solving)  
            coords.clear()

        for d in dir:
            if not maze[(y,x)].walls[d]:
                ny, nx = y + dy[d], x + dx[d]
                tentative_gScore = gScore[(y,x)] + 1
                if  tentative_gScore < gScore[(ny,nx)]:
                    path[(ny,nx)] = Bdir[d]
                    gScore[(ny,nx)] = tentative_gScore
                    fScore[(ny,nx)] = tentative_gScore + Manhattan_distance(nx, ny, x_end, y_end)
                    heapq.heappush(heap, (fScore[(ny,nx)], Manhattan_distance(nx, ny, x_end, y_end), (ny, nx)))

        if animation:
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))

    return -1

def dijkshtra(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animation: bool = False):

   

    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    Bdir = {0:1, 1:0, 2:3, 3:2}
    dir = [0, 1, 2, 3]

    if animation:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()

    coords = []
    heap = []
    path = {}
    gScore = {}

    y_end, x_end = settings.lines - 1, settings.rows - 1
    y_start, x_start = 0, 0

    inf = 999999999
    for key in maze:
        gScore[key] = inf

    gScore[(y_start, x_start)] = 0
    
    heapq.heappush(heap, (gScore[(y_start, x_start)], (y_start, x_start)))
    
    while heap:
        old_dist, (y, x) = heapq.heappop(heap)
        
        if old_dist > gScore[(y, x)]:
            continue

        maze[(y,x)].visited = True

        if (y, x) == (y_end, x_end):
            mark_path_to_exit(x_end, y_end, x_start, y_start, path, maze)
            return 1

        check_events()
        if animation:
            maze[(y,x)].highlite = True
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))
            maze[(y,x)].highlite = False
            pygame.display.update(get_rect_for(coords))
            settings.clock.tick(tick_solving)  
            coords.clear()

        for d in dir:
            if not maze[(y,x)].walls[d]:
                ny, nx = y + dy[d], x + dx[d]
                if (ny, nx) in maze:
                    tentative_gScore = gScore[(y,x)] + 1
                    if tentative_gScore < gScore[(ny,nx)]:
                        path[(ny,nx)] = Bdir[d]
                        gScore[(ny,nx)] = tentative_gScore 
                        heapq.heappush(heap, (gScore[(ny,nx)], (ny, nx)))

        if animation:
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))
    
    return -1