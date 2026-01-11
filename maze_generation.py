import pygame
import classes
from draw import *
from settings import *
from random import shuffle, randint

#DFS - recursive
def Randomized_depth_first_search_recursive(maze: dict[tuple[int, int], classes.Cell], surface : pygame.Surface):

    visited = []
    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    M = {0:1, 1:0, 2:3, 3:2}   
    lines = settings.lines
    rows = settings.rows 

    for _ in range(lines):
        line = []
        for __ in range(rows):
            line.append(0)
        visited.append(line)

    def DFS(y, x):

        if visited[y][x] == True:
            return
        
        check_events()
        
        maze[(y,x)].visited = True
        visited[y][x] = 1

        dirs = [0,1,2,3] 
        shuffle(dirs)

        for index in dirs:
            i = dy[index] + y #i
            j = dx[index] + x #j
           
            if (i >= 0 and i < lines) and (j >= 0 and j < rows) and not visited[i][j]:
                maze[(y,x)].walls[index] = False
                maze[(i,j)].walls[M[index]] = False

                maze[(y,x)].highlite = True
                draw_maze(maze, settings.rect, surface)
                maze[(y,x)].highlite = False
                
                pygame.display.update()
                settings.clock.tick(ticks_generation)

                DFS(i,j)

                maze[(i,j)].highlite = True
                draw_maze(maze, settings.rect, surface)
                maze[(i,j)].highlite = False
                
                pygame.display.update()
                settings.clock.tick(ticks_generation)

    DFS(0,0)

#DFS - iterative
def Randomized_depth_first_search_iterative(maze: dict[tuple[int, int], classes.Cell], surface : pygame.Surface, animated: bool = False):

    visited = []
    stack = []
    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1] 
    Bdir = {0:1, 1:0, 2:3, 3:2}
    coords = []
    lines = settings.lines
    rows = settings.rows

    for _ in range(lines):
        line = []
        for _ in range(rows):
            line.append(0)
        visited.append(line)

    if animated:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()
    
    y, x = 0, 0
    visited[y][x] = 1
    maze[(y,x)].visited = True
    
    stack.append((y,x))

    #LIFO
    while stack:

        check_events()
        if animated:
            maze[((y,x))].highlite = True
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))
            maze[(y,x)].highlite = False
            pygame.display.update(get_rect_for(coords))
            settings.clock.tick(ticks_generation)
            coords.clear()
            maze[(y,x)].draw(settings.rect, surface)
            coords.append((x,y))

        y, x = stack.pop()
        
        neighbours = []
        dir = [0,1,2,3]
        
        shuffle(dir)
        for index in range(len(dir)):
            Ry = y + dy[dir[index]]
            Rx = x + dx[dir[index]]

            if (Ry >= 0 and Ry < lines) and (Rx >= 0 and Rx < rows) and not visited[Ry][Rx]:
                neighbours.append((Ry,Rx))
            else:
                dir[index] = -1
        
        i = 0
        while i < len(dir):
            if dir[i] == -1:
                dir.pop(i)
                i -= 1
            i += 1

        if len(neighbours) > 0:
            stack.append((y,x))
            
            maze[(y,x)].walls[dir[0]] = False

            if animated:
                maze[(y,x)].draw(settings.rect, surface)
                coords.append((x,y))
           
            y, x = neighbours.pop(0)
            
            maze[(y,x)].walls[Bdir[dir[0]]] = False
            visited[y][x] = 1
            maze[(y,x)].visited = True

            stack.append((y,x))
        else:
            if animated:
                maze[(y,x)].draw(settings.rect, surface)
                coords.append((x,y))

#Prim's algorithm
def Prim_algoritm(maze: dict[tuple[int, int], classes.Cell], surface : pygame.Surface, animated: bool = False):

    visited = []
    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    dir = [0,1,2,3]
    Bdir = {0:1, 1:0, 2:3, 3:2}
    unvisited_cells = []
    lines = settings.lines
    rows = settings.rows

    for _ in range(lines):
        line = []
        for __ in range(rows):
            line.append(0)
        visited.append(line)

    if animated:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()

    y, x = 0, 0
    visited[y][x] = 1
    maze[(y,x)].visited = True
    if animated:
        maze[(y,x)].draw(settings.rect, surface)

    for d in dir:
        ny = y + dy[d]
        nx = x + dx[d]
        if (ny >= 0 and ny < lines) and (nx >= 0 and nx < rows):
            unvisited_cells.append((ny,nx))

    while unvisited_cells:

        index = randint(0, len(unvisited_cells) - 1)
        y, x = unvisited_cells[index][0], unvisited_cells[index][1]

        if visited[y][x] == 1:
            unvisited_cells.pop(index)
            continue

        dir = [0,1,2,3]
        shuffle(dir)

        for d in dir:
            ny = y + dy[d]
            nx = x + dx[d]
            if (ny >= 0 and ny < lines) and (nx >= 0 and nx < rows) and visited[ny][nx] == 1:
                maze[(y,x)].walls[d] = False
                maze[(ny, nx)].walls[Bdir[d]] = False

                visited[y][x] = 1
                maze[(y,x)].visited = True

                check_events()

                coords = [(x,y), (nx, ny)]
                rects = get_rect_for(coords)

                if animated:
                    maze[(y,x)].draw(settings.rect, surface)
                    maze[(ny, nx)].draw(settings.rect, surface)
                    pygame.display.update(rects)
                    settings.clock.tick(ticks_generation)

                for di in dir:
                    ny = y + dy[di]
                    nx = x + dx[di]
                    if (ny >= 0 and ny < lines) and (nx >= 0 and nx < rows) and visited[ny][nx] == 0:
                        unvisited_cells.append((ny,nx))
                break

        unvisited_cells.pop(index)

#Aldous-Broder algorithm
def Aldous_Broder_algorithm(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animated: bool = False):

    visited = []
    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1] 
    dir = [0,1,2,3]
    Bdir = {0:1, 1:0, 2:3, 3:2}
   
    visited_cells = 0
    lines = settings.lines
    rows = settings.rows

    total_cells = lines * rows

    for _ in range(lines):
        line =  []
        for __ in range(rows):
            line.append(0)
        visited.append(line)

    y, x = randint(0, lines - 1), randint(0, rows - 1)
    visited[y][x] = 1
    maze[(y,x)].visited = True
    visited_cells += 1

    if animated:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()

    while visited_cells < total_cells:

        check_events()

        if animated:
            maze[(y,x)].highlite = True
            draw_maze(maze, settings.rect, surface)
            maze[(y,x)].highlite = False
            pygame.display.update()
            settings.clock.tick(ticks_generation)

        ny, nx = -1, -1
        neighbors = []
        for d in dir:
            ny = y + dy[d]
            nx = x + dx[d]
            if (ny >= 0 and ny < lines) and (nx >= 0 and nx < rows):
                neighbors.append(d)

        dir_index = neighbors[randint(0, len(neighbors) - 1)]
        ny, nx = y + dy[dir_index], x + dx[dir_index]
            
        if visited[ny][nx] == 0:
            maze[(y,x)].walls[dir_index] = False
            maze[(ny, nx)].walls[Bdir[dir_index]] = False

            visited[ny][nx] = 1
            maze[(ny,nx)].visited = True
            visited_cells += 1

        y, x = ny, nx

#Wilson's algorithm
def Wilson_algorithm(maze: dict[tuple[int, int], classes.Cell], surface: pygame.Surface, animated: bool = False):

    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    Bdir = {0:1, 1:0, 2:3, 3:2}
    coords = []
    unvisited = []
    lines = settings.lines
    rows = settings.rows

    for y in range(lines):
        for x in range(rows):
            unvisited.append((y,x))
    
    start_index = randint(0, len(unvisited) - 1)
    y, x = unvisited.pop(start_index)
    maze[(y,x)].visited = True

    if animated:
        draw_maze(maze, settings.rect, surface)
        pygame.display.update()
    
    while unvisited:

        index = randint(0, len(unvisited) - 1)
        cy, cx = unvisited[index]

        path = {}
        curr_y, curr_x = cy, cx

        while (curr_y, curr_x) in unvisited:

            neighbors = []
            for d in range(4):
                ny = curr_y + dy[d]
                nx = curr_x + dx[d]
                if (ny >= 0 and ny < lines)and (nx >= 0 and nx < rows):
                    neighbors.append(d)

            dir_to = neighbors[randint(0, len(neighbors) - 1)]
            path[(curr_y, curr_x)] = dir_to

            curr_y += dy[dir_to]
            curr_x += dx[dir_to]
            
            check_events()

            if animated:
                draw_maze(maze, settings.rect, surface)
                highlite_path(cx, cy, curr_x, curr_y, path, surface)
                maze[(curr_y, curr_x)].highlite = True
                maze[(curr_y, curr_x)].draw(settings.rect, surface)
                coords.append((curr_x, curr_y))
                maze[(curr_y, curr_x)].highlite = False
                pygame.display.update()
                settings.clock.tick(ticks_generation)
                coords.clear()

        curr_y, curr_x = cy, cx
        while (curr_y, curr_x) in unvisited:

            dir_to = path[(curr_y, curr_x)]

            ny = curr_y + dy[dir_to]
            nx = curr_x + dx[dir_to]
            
            maze[(curr_y, curr_x)].walls[dir_to] = False
            maze[(ny, nx)].walls[Bdir[dir_to]] = False

            if (curr_y, curr_x) in unvisited:
                unvisited.remove((curr_y, curr_x))
                maze[(curr_y, curr_x)].visited = True

            maze[(curr_y, curr_x)].draw(settings.rect, surface)
            
            curr_y, curr_x = ny, nx

        if animated:
            pygame.display.update()
