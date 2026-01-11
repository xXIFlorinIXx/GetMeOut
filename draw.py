import pygame
import settings

def get_rect_for(coords: list[tuple[int, int]]):

    if not coords:
        return

    rects: list[pygame.Rect] = []
    for (x, y) in coords:
        local_rect = pygame.Rect(x * settings.rect, y * settings.rect, settings.rect, settings.rect)
        offset_x, offset_y =  settings.maze_surf.get_abs_offset()
        rects.append(local_rect.move(offset_x, offset_y))
    
    return rects

def draw_maze(maze: dict, rect: int, surface: pygame.Surface, game: bool = False):
    if game:
        surface.fill('lightblue')
    else:
        surface.fill('black')
        
    for key in maze.keys():
        maze[key].draw(rect, surface, game)

def highlite_path(start_x: int, start_y: int, final_x: int, final_y:int , path: dict, surface: pygame.Surface):

    dy = [-1,1,0,0] #N, S, E, W
    dx = [0,0,1,-1]
    cy, cx = start_y, start_x

    pygame.draw.rect(surface, "#15ff00d4", (cx * settings.rect ,cy * settings.rect, settings.rect, settings.rect))
   
    while (cy, cx) != (final_y, final_x):
        
        if (cy, cx) not in path:
            break

        dir_to = path[(cy,cx)]
        cy = cy + dy[dir_to]
        cx = cx + dx[dir_to]

        pygame.draw.rect(surface, "#15ff00d4", (cx * settings.rect ,cy * settings.rect, settings.rect, settings.rect))
