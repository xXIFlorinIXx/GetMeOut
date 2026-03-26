import pygame
from sys import exit

#Back - End
lines, rows = 10, 10
rect = 5
Big_rect = 80
wall_thickness = 1
wall_thickness_game = 4
maze = {}

#Front - End
pygame.init()
clock = pygame.time.Clock()
ticks = 0
ticks_generation = 360
tick_solving = 360
pygame.event.set_grab(True) #Alt - TAB

themes = 'Classic'


#Windows

#1. Maine - Window
sizes = pygame.display.list_modes()
screen = pygame.display.set_mode((1920, 1080))
print(sizes)
# pygame.display.toggle_fullscreen()
size = screen.get_size()
screen_rect = screen.get_rect()

#1.1 Maze - surface
maze_rect = pygame.Rect((0,0), (rows * rect + wall_thickness, lines * rect + wall_thickness))
maze_rect.center = (screen_rect.centerx, screen_rect.centery)
maze_surf = screen.subsurface(maze_rect)
Big_maze_surf = pygame.Surface((rows * Big_rect + wall_thickness_game, lines * Big_rect + wall_thickness_game))
Big_maze_surf.fill('lightblue')

def check_events():
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

def change_themes(in_to: str):
    global themes

    themes = in_to
   
def change_maze_size(l, r):
    global lines
    global rows
    global Big_maze_surf
    global maze_rect
    global maze_surf

    lines = l
    rows = r

    Big_maze_surf = pygame.Surface((rows * Big_rect + wall_thickness_game, lines * Big_rect + wall_thickness_game))
    Big_maze_surf.fill('lightblue')

    maze_rect = pygame.Rect((0,0), (rows * rect + wall_thickness, lines * rect + wall_thickness))
    maze_rect.center = (screen_rect.centerx, screen_rect.centery)
    maze_surf = screen.subsurface(maze_rect)