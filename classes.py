import pygame
import settings
import math

class Cell:
    
    image_wall = None
    image_floor = None
    image_prize = None
    offset_wall = 0

    @classmethod
    def load_resources(cls, reload = False):
        if cls.image_wall is None or reload:
            #Wall
            cls.image_wall = pygame.image.load(f'Assets/Themes/{settings.themes}/wall.jpeg').convert_alpha()
            cls.image_wall = pygame.transform.smoothscale(cls.image_wall,(32,8))
            cls.image_wall = pygame.transform.scale(cls.image_wall, (settings.Big_rect, cls.image_wall.get_height()))
           
            cls.offset_wall = cls.image_wall.get_height() // 2
            
            #Floor
            cls.image_floor = pygame.image.load(f'Assets/Themes/{settings.themes}/floor.jpeg').convert_alpha()
            cls.image_floor = pygame.transform.scale(cls.image_floor, (settings.Big_rect, settings.Big_rect))

            #Prize
            cls.image_prize = pygame.image.load(f'Assets/Themes/{settings.themes}/prize.png').convert_alpha()
            cls.image_prize = pygame.transform.scale(cls.image_prize, (settings.Big_rect, settings.Big_rect))

    def __init__(self, y: int, x: int, walls: list[bool]):
        self.y: int = y
        self.x: int = x
        self.walls: list = walls
        self.visited: bool = False
        self.exit_path: bool = False
        self.highlite: bool = False

    def draw(self, rect: int, surface: pygame.Surface, game: bool = False):
        Rx: int = self.x * rect
        Ry: int = self.y * rect

        if game:
            surface.blit(self.image_floor,(Rx, Ry))

            if (self.y, self.x) == (settings.lines - 1, settings.rows - 1):
                surface.blit(self.image_prize,(Rx, Ry))
                
        elif self.highlite:
            pygame.draw.rect(surface, "#ffffffff", (Rx, Ry, rect, rect))
        elif self.exit_path:
            pygame.draw.rect(surface, "#b45555ff", (Rx, Ry, rect, rect))
        elif self.visited:
            pygame.draw.rect(surface, "#60b455ff", (Rx, Ry, rect, rect))

        #North
        if self.walls[0]:
            if game:
                surface.blit(self.image_wall,(Rx, Ry - self.offset_wall))
            else:
                pygame.draw.line(surface,'green',(Rx, Ry),(Rx + rect, Ry), settings.wall_thickness)
           
        #South
        if self.walls[1]:
            if game:
                surface.blit(self.image_wall,(Rx,Ry + rect - self.offset_wall))
            else:
                pygame.draw.line(surface,'green',(Rx,Ry + rect),(Rx + rect, Ry + rect), settings.wall_thickness)
           
        #East
        if self.walls[2]:
            if game:
                surface.blit(pygame.transform.rotate(self.image_wall, 90),(Rx + rect - self.offset_wall, Ry))
            else:
                pygame.draw.line(surface,'green',(Rx + rect, Ry + rect),(Rx + rect, Ry), settings.wall_thickness)
            
        #West
        if self.walls[3]:
            if game:
                surface.blit(pygame.transform.rotate(self.image_wall, 90),(Rx - self.offset_wall, Ry))
            else:
                pygame.draw.line(surface,'green',(Rx,Ry),(Rx, Ry + rect), settings.wall_thickness)

class Player(pygame.sprite.Sprite):

    move_up_image = None
    move_down_image = None
    move_left_right_image = None
    pause_image = None
    pause_image = None
    image = None

    @classmethod
    def load_resources(cls, reload = False):

        if cls.move_up_image is None or reload:
            cls.move_down_image = pygame.image.load(f'Assets/Themes/{settings.themes}/player_move_down.png').convert_alpha()
            cls.move_down_image = pygame.transform.scale(cls.move_down_image, (settings.Big_rect - 10, settings.Big_rect - 10))

            cls.move_up_image = pygame.image.load(f'Assets/Themes/{settings.themes}/player_move_up.png').convert_alpha()
            cls.move_up_image = pygame.transform.scale(cls.move_up_image, (settings.Big_rect - 10, settings.Big_rect - 10))

            cls.move_left_right_image = pygame.image.load(f'Assets/Themes/{settings.themes}/player_move_left_right.png').convert_alpha()
            cls.move_left_right_image = pygame.transform.scale(cls.move_left_right_image, (settings.Big_rect - 10, settings.Big_rect - 10))

            cls.pause_image = pygame.image.load(f'Assets/Themes/{settings.themes}/player_pause.png').convert_alpha()
            cls.pause_image = pygame.transform.scale(cls.pause_image, (settings.Big_rect - 10, settings.Big_rect - 10))
            cls.image = cls.pause_image

    def __init__(self, cell: Cell, group):
        self.cell: Cell = cell
        self.next_cell: Cell = cell
        self.y = cell.y
        self.x = cell.x
        self.ny = self.y
        self.nx = self.x

        self.rect = self.image.get_rect(topleft = (self.x + 10, self.y + 10))
        self.speed = 4
        
    def update_rect(self):
        rect = settings.Big_rect
        Ry: int = self.y * rect
        Rx: int = self.x * rect

        self.rect.topleft = (Rx + 10, Ry + 10)

    def isplayer_there(self, there):
        if (self.y, self.x) == there:
            return True
        return False

    def highlite(self, status: bool):
        settings.maze[(self.y, self.x)].highlite = status

    def move(self, next_cell: Cell):
        self.cell = next_cell
        self.y = self.cell.y
        self.x = self.cell.x

        self.update_rect()

    def input(self):

        if self.cell != self.next_cell:
            return

        keys = pygame.key.get_pressed()

        if  keys[pygame.K_w] and not settings.maze[(self.y, self.x)].walls[0]:
            self.image = self.move_up_image
            self.next_cell = settings.maze[(self.y - 1, self.x)]
            
        elif keys[pygame.K_s] and not settings.maze[(self.y, self.x)].walls[1]:
            self.image = self.move_down_image
            self.next_cell = settings.maze[(self.y + 1, self.x)]

        elif keys[pygame.K_d] and not settings.maze[(self.y, self.x)].walls[2]:
            self.image = pygame.transform.flip(self.move_left_right_image, 1, 0)
            self.pause_image = pygame.transform.flip(self.pause_image,1,0)
            self.next_cell = settings.maze[(self.y, self.x + 1)]

        elif keys[pygame.K_a] and not settings.maze[(self.y, self.x)].walls[3]:
            self.image = pygame.transform.flip(self.move_left_right_image, 0, 0)
            self.pause_image = pygame.transform.flip(self.pause_image,1,0)
            self.next_cell = settings.maze[(self.y, self.x - 1)]
           
    def animation(self, dt):

        if self.cell == self.next_cell:
            return
        
        if self.next_cell.y != self.y:
            if self.next_cell.y > self.y:
                self.ny += self.speed * dt
                self.y = self.ny
            elif self.next_cell.y < self.y:
                self.ny -= self.speed * dt
                self.y = self.ny
        elif self.next_cell.x != self.x:
            if self.next_cell.x > self.x:
                self.nx += self.speed * dt
                self.x = self.nx
            elif self.next_cell.x < self.x:
                self.nx -= self.speed * dt
                self.x = self.nx
                
        if self.y != self.next_cell.y and math.isclose(self.y, self.next_cell.y, abs_tol=0.01):
            self.cell = self.next_cell
            self.y = self.cell.y
            self.x = self.cell.x
            self.next_cell = self.cell
            self.ny = self.y
            self.nx = self.x
            
        if self.x != self.next_cell.x and math.isclose(self.x, self.next_cell.x, abs_tol=0.01):
            self.cell = self.next_cell
            self.y = self.cell.y
            self.x = self.cell.x
            self.next_cell = self.cell
            self.ny = self.y
            self.nx = self.x

        self.update_rect()

    def update(self, dt):

        if self.cell == self.next_cell:
            self.image = Player.pause_image

        self.input()
        self.animation(dt)

def clear_maze():
    settings.maze.clear()
    for y in range(settings.lines):
        for x in range(settings.rows):
            settings.maze[(y,x)] = Cell(y,x, [True, True, True, True])

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        self.x = x
        self.y = y

        self.image = image
        self.image = pygame.transform.scale_by(self.image,0.5)

        self.rect = self.image.get_rect(topleft = (self.x, self.y))

        self.pressed: bool = False
        

    def ispressed(self, pos) -> bool:
        if (pos[0] > self.rect.left and pos[0] < self.rect.right) and (pos[1] > self.rect.top and pos[1] < self.rect.bottom) and pygame.mouse.get_just_pressed()[0]:
            return True
        return False
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.pressed:
            pygame.draw.rect(surface,'yellow',(self.rect), 2)

    def update(self):

        if self.ispressed(pygame.mouse.get_pos()):
            print("MERGE")
        
