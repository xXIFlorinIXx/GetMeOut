import pygame
import settings
from random import randint
from draw import *

class CameraGroup(pygame.sprite.Group):
    def __init__(self, surface: pygame.Surface):
        super().__init__()
        self.display_surface = surface

        #Camera Offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.width // 2
        self.half_h = self.display_surface.height // 2

        #box setop
        self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.width - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.height - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)
        self.nx = self.camera_rect.x
        self.ny = self.camera_rect.y

        #ground
        self.groud_rect = settings.Big_maze_surf.get_rect()

        #camera speed
        self.keyboard_speed = 200

    def draw_map(self):
        draw_maze(settings.maze, settings.Big_rect, settings.Big_maze_surf, True)


    def box_target_camera(self, target):

        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
            self.nx = self.camera_rect.x

        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
            self.nx = self.camera_rect.x
          
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
            self.ny = self.camera_rect.y

        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom
            self.ny = self.camera_rect.y

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    def keyboard_control(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.nx -= self.keyboard_speed * dt
            self.camera_rect.x = self.nx

        if keys[pygame.K_RIGHT]:
            self.nx += self.keyboard_speed * dt
            self.camera_rect.x = self.nx

        if keys[pygame.K_UP]:
            self.ny -= self.keyboard_speed * dt
            self.camera_rect.y = self.ny

        if keys[pygame.K_DOWN]:
            self.ny += self.keyboard_speed * dt
            self.camera_rect.y = self.ny

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    def game_draw(self, player, dt):
        self.display_surface.fill('lightblue')

        self.box_target_camera(player)
        self.keyboard_control(dt)

        #ground
        ground_offset = self.groud_rect.topleft - self.offset
        self.display_surface.blit(settings.Big_maze_surf, ground_offset)
  
        #player
        self.display_surface.blit(player.image, player.rect.topleft - self.offset)
