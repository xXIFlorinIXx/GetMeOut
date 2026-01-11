import pygame
import settings
import classes
from draw import *
import camera
from maze_generation import *
from maze_solving import *
import time
from sys import exit

classes.Cell.load_resources()
classes.Player.load_resources()

classes.clear_maze()

camera_group = camera.CameraGroup(settings.screen)

player = classes.Player(settings.maze[(0,0)], camera_group)

font = pygame.font.Font('font/Pixeltype.ttf', 80)
font_rez = pygame.font.Font('font/Pixeltype.ttf', 50)

pygame.mixer.init()
pygame.mixer_music.load('audio/bg_music.mp3')
pygame.mixer_music.set_volume(0.3)
pygame.mixer_music.play()


#Menius
meniu_empty = pygame.image.load('Menus/background_empty.jpeg').convert_alpha()
meniu_generation = pygame.image.load('Menus/background_generation.jpeg').convert_alpha()
meniu_login = pygame.image.load('Menus/background_login.jpeg').convert_alpha()
meniu_pc = pygame.image.load('Menus/background_pc.jpeg').convert_alpha()
meniu_rezultate_om = pygame.image.load('Menus/background_rezultateom.jpeg').convert_alpha()
meniu_rezultate_pc = pygame.image.load('Menus/background_rezultatepc.jpeg').convert_alpha()
meniu_setari = pygame.image.load('Menus/background_settings.jpeg').convert_alpha()
meniu_start = pygame.image.load('Menus/background_start.jpeg').convert_alpha()

#Buttons
button_1 = classes.Button(770,280,pygame.transform.scale2x(pygame.image.load('Menus/button_1.jpeg').convert_alpha()))
button_2 = classes.Button(300,375,pygame.transform.scale2x(pygame.image.load('Menus/button_2.jpeg').convert_alpha()))
button_3 = classes.Button(1225,375,pygame.transform.scale2x(pygame.image.load('Menus/button_3.jpeg').convert_alpha()))
button_4 = classes.Button(100,560, pygame.transform.scale2x(pygame.image.load('Menus/button_4.jpeg').convert_alpha()))
button_5 = classes.Button(560,560,pygame.transform.scale2x(pygame.image.load('Menus/button_5.jpeg').convert_alpha()))
button_6 = classes.Button(1020,560,pygame.transform.scale2x(pygame.image.load('Menus/button_6.jpeg').convert_alpha()))
button_7 = classes.Button(1480,560,pygame.transform.scale2x(pygame.image.load('Menus/button_7.jpeg').convert_alpha()))

button_1_om = classes.Button(770,280,pygame.transform.scale2x(pygame.image.load('Menus/button_1.jpeg').convert_alpha()))
button_2_om = classes.Button(300,375,pygame.transform.scale2x(pygame.image.load('Menus/button_2.jpeg').convert_alpha()))
button_3_om = classes.Button(1225,375,pygame.transform.scale2x(pygame.image.load('Menus/button_3.jpeg').convert_alpha()))
button_4_om = classes.Button(100,560, pygame.transform.scale2x(pygame.image.load('Menus/button_4.jpeg').convert_alpha()))
button_5_om = classes.Button(560,560,pygame.transform.scale2x(pygame.image.load('Menus/button_5.jpeg').convert_alpha()))
button_6_om = classes.Button(1020,560,pygame.transform.scale2x(pygame.image.load('Menus/button_6.jpeg').convert_alpha()))
button_7_om = classes.Button(1480,560,pygame.transform.scale2x(pygame.image.load('Menus/button_7.jpeg').convert_alpha()))

button_20x30 = classes.Button(520,480,pygame.transform.scale2x(pygame.image.load('Menus/20x30.jpeg').convert_alpha()))
button_40x60 = classes.Button(790,480,pygame.transform.scale2x(pygame.image.load('Menus/40x60.jpeg').convert_alpha()))
button_100x200 = classes.Button(1060,480,pygame.transform.scale2x(pygame.image.load('Menus/100x200.jpeg').convert_alpha()))

button_20x30_om = classes.Button(800,570,pygame.transform.scale2x(pygame.image.load('Menus/20x30.jpeg').convert_alpha()))
button_40x60_om = classes.Button(1100,570,pygame.transform.scale2x(pygame.image.load('Menus/40x60.jpeg').convert_alpha()))
button_100x200_om = classes.Button(1400,570,pygame.transform.scale2x(pygame.image.load('Menus/100x200.jpeg').convert_alpha()))

button_800x600 = classes.Button(940,320,pygame.transform.scale2x(pygame.image.load('Menus/800x600.jpeg').convert_alpha()))
button_1280x1024 = classes.Button(710,320,pygame.transform.scale2x(pygame.image.load('Menus/1280x1024.jpeg').convert_alpha()))
button_1920x1080 = classes.Button(480,320,pygame.transform.scale2x(pygame.image.load('Menus/1920x1080.jpeg').convert_alpha()))
button_210x380 = classes.Button(1330,480,pygame.transform.scale2x(pygame.image.load('Menus/210x380.jpeg').convert_alpha()))

button_a = classes.Button(1060,320,pygame.transform.scale2x(pygame.image.load('Menus/button_a.jpeg').convert_alpha()))
button_bfs = classes.Button(520,320,pygame.transform.scale2x(pygame.image.load('Menus/button_bfs.jpeg').convert_alpha()))
button_dfs = classes.Button(790,320,pygame.transform.scale2x(pygame.image.load('Menus/button_dfs.jpeg').convert_alpha()))
button_dijkstra = classes.Button(1330,320,pygame.transform.scale2x(pygame.image.load('Menus/button_dijkstra.jpeg').convert_alpha()))
button_inapoi = classes.Button(60,35,pygame.transform.scale2x(pygame.image.load('Menus/button_inapoi.jpeg').convert_alpha()))
button_login = classes.Button(640,360,pygame.transform.scale2x(pygame.image.load('Menus/button_login.jpeg').convert_alpha()))
button_moscraciun = classes.Button(280,520,pygame.transform.scale2x(pygame.image.load('Menus/button_moscraciun.jpeg').convert_alpha()))
button_off = classes.Button(290,410,pygame.transform.scale2x(pygame.image.load('Menus/button_off.jpeg').convert_alpha()))

button_om = classes.Button(960,650,pygame.transform.scale2x(pygame.image.load('Menus/button_om.jpeg').convert_alpha()))
button_om_rez = classes.Button(530,650,pygame.transform.scale2x(pygame.image.load('Menus/button_om.jpeg').convert_alpha()))
button_on = classes.Button(170,410,pygame.transform.scale2x(pygame.image.load('Menus/button_on.jpeg').convert_alpha()))
button_pc = classes.Button(730,650,pygame.transform.scale2x(pygame.image.load('Menus/button_pc.jpeg').convert_alpha()))
button_pc_rez = classes.Button(300,650,pygame.transform.scale2x(pygame.image.load('Menus/button_pc.jpeg').convert_alpha()))

button_prim = classes.Button(720,400,pygame.transform.scale2x(pygame.image.load('Menus/button_prim.jpeg').convert_alpha()))
button_randomdfs = classes.Button(130,400,pygame.transform.scale2x(pygame.image.load('Menus/button_randomdfs.jpeg').convert_alpha()))

button_rezultate = classes.Button(270,500,pygame.transform.scale2x(pygame.image.load('Menus/button_rezultate.jpeg').convert_alpha()))

button_setari = classes.Button(1270,500,pygame.transform.scale2x(pygame.image.load('Menus/button_setari.jpeg').convert_alpha()))
button_soricel = classes.Button(530,520,pygame.transform.scale2x(pygame.image.load('Menus/button_soricel.jpeg').convert_alpha()))
button_start = classes.Button(770,500,pygame.transform.scale2x(pygame.image.load('Menus/button_start.jpeg').convert_alpha()))
button_start_game = classes.Button(1430,35,pygame.transform.scale2x(pygame.image.load('Menus/button_start.jpeg').convert_alpha()))
button_wilson = classes.Button(1310,400,pygame.transform.scale2x(pygame.image.load('Menus/button_wilson.jpeg').convert_alpha()))


def get_mouse_click():
    if pygame.mouse.get_just_pressed()[0]:
        print(pygame.mouse.get_pos())
    
def main():
    is_meniu_start: bool = True
    is_meniu_login: bool = False
    is_meniu_game: bool = False
    is_meniu_generare: bool = False
    is_meniu_pc: bool = False
    is_meniu_rezultate_pc: bool = False
    is_meniu_rezultate_om: bool = False
    is_meniu_setari: bool = False
    run: bool = True
    map: bool = False
    previous_time = time.time()
    name: str = 'The Runner'
    pc_rez: list = []
    om_rez: list = []

    algoritm: str = None
    dim: bool = False


    while run:

        dt = time.time() - previous_time
        previous_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                map = not map

            if button_login.pressed:

                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and len(name) > 0:
                   name = name.removesuffix(name[len(name) - 1]) 

                elif event.type == pygame.KEYDOWN:
                    name += event.unicode
                      
        if is_meniu_start:
            screen.fill('black')
            screen.blit(meniu_start)

            button_start.draw(screen)
            button_rezultate.draw(screen)
            button_setari.draw(screen)

            if pygame.mouse.get_just_pressed()[0]:

                if button_start.ispressed(pygame.mouse.get_pos()):
                   button_start.pressed = True
                   button_rezultate.pressed = False

                if button_start.pressed and button_om.ispressed(pygame.mouse.get_pos()):
                    is_meniu_start = False
                    button_start.pressed = False
                    is_meniu_login = True

                if button_start.pressed and button_pc.ispressed(pygame.mouse.get_pos()):
                    is_meniu_start= False
                    button_start.pressed = False
                    is_meniu_pc = True

                if button_rezultate.ispressed(pygame.mouse.get_pos()):
                    button_rezultate.pressed = True
                    button_start.pressed = False

                if button_rezultate.pressed and button_pc_rez.ispressed(pygame.mouse.get_pos()):
                    is_meniu_start = False
                    is_meniu_rezultate_pc = True

                if button_rezultate.pressed and button_om_rez.ispressed(pygame.mouse.get_pos()):
                    is_meniu_start = False
                    is_meniu_rezultate_om = True

                    om_rez.clear()

                    with open("rezultate_om.txt", "r", encoding="utf-8") as f:
                        for line in f:
                            if line.strip():
                                parts = line.split(":")
                                nume = parts[0] 
                                timp_text = parts[1].replace(" seconds", "").strip() 
                                timp = round(float(timp_text), 4)
                                om_rez.append((timp, nume))

                    om_rez.sort()

                if button_setari.ispressed(pygame.mouse.get_pos()):
                    is_meniu_start = False
                    is_meniu_setari = True

            if button_start.pressed:
                button_om.draw(screen)
                button_pc.draw(screen)

            if button_rezultate.pressed:
                button_om_rez.draw(screen)
                button_pc_rez.draw(screen)

        if is_meniu_setari:
            screen.fill('black')
            screen.blit(meniu_setari)

            button_1920x1080.draw(screen)
            # button_1280x1024.draw(screen)
            # button_800x600.draw(screen)

            button_on.draw(screen)
            button_off.draw(screen)

            button_moscraciun.draw(screen)
            button_soricel.draw(screen)

            button_inapoi.draw(screen)

            if pygame.mouse.get_just_pressed()[0]:

                if button_moscraciun.ispressed(pygame.mouse.get_pos()):
                    button_soricel.pressed = False
                    button_moscraciun.pressed = True
                    settings.change_themes('Christmas')
                    classes.Cell.load_resources(True)
                    classes.Player.load_resources(True)
                    camera_group.draw_map()

                if button_soricel.ispressed(pygame.mouse.get_pos()):
                    button_soricel.pressed = True
                    button_moscraciun.pressed = False
                    settings.change_themes('Classic')
                    classes.Cell.load_resources(True)
                    classes.Player.load_resources(True)
                    camera_group.draw_map()

                if button_inapoi.ispressed(pygame.mouse.get_pos()):
                    is_meniu_setari = False
                    is_meniu_start = True

                if button_on.ispressed(pygame.mouse.get_pos()):
                    button_on.pressed = True
                    button_off.pressed = False
                    pygame.mixer_music.play()

                if button_off.ispressed(pygame.mouse.get_pos()):
                    button_on.pressed = False
                    button_off.pressed = True
                    pygame.mixer_music.pause()

        if is_meniu_pc:
            screen.fill('black')
            screen.blit(meniu_pc)

            button_bfs.draw(screen)
            button_dfs.draw(screen)
            button_a.draw(screen)
            button_dijkstra.draw(screen)

            button_20x30.draw(screen)
            button_40x60.draw(screen)
            button_100x200.draw(screen)
            button_210x380.draw(screen)

            button_inapoi.draw(screen)
            button_start_game.draw(screen)

            
            if pygame.mouse.get_just_pressed()[0]:

                if button_inapoi.ispressed(pygame.mouse.get_pos()):
                    is_meniu_pc = False
                    is_meniu_start = True
                    button_start_game.pressed = False
                    
                if button_start_game.ispressed(pygame.mouse.get_pos()):
                    button_start_game.pressed = True

                    if button_start_game.pressed and algoritm == 'BFS' and dim:
                        settings.screen.fill('black')
                        unvisit_maze(settings.maze)
                        time_start = time.time()
                        BFS(settings.maze, settings.maze_surf, True)
                        time_end = time.time()
                        
                        pc_rez.append((time_end - time_start, 'BFS'))
                        with open("rezultate_pc.txt", "a", encoding="utf-8") as f:
                            f.write(f"\nBFS: {time_end - time_start} seconds")

                        camera_group.draw_map()

                    if button_start_game.pressed and algoritm == 'DFS' and dim:
                        settings.screen.fill('black')
                        unvisit_maze(settings.maze)
                        time_start = time.time()
                        DFS(settings.maze, settings.maze_surf, True)
                        time_end = time.time()
                        
                        pc_rez.append((time_end - time_start, 'DFS'))

                        with open("rezultate_pc.txt", "a", encoding="utf-8") as f:
                            f.write(f"\nDFS: {time_end - time_start} seconds")

                        camera_group.draw_map()

                    if button_start_game.pressed and algoritm == 'A*' and dim:
                        settings.screen.fill('black')
                        unvisit_maze(settings.maze)
                        time_start = time.time()
                        A_star(settings.maze, settings.maze_surf, True)
                        time_end = time.time()
                        
                        pc_rez.append((time_end - time_start, 'A*'))
                        with open("rezultate_pc.txt", "a", encoding="utf-8") as f:
                            f.write(f"\nA*: {time_end - time_start} seconds")

                        camera_group.draw_map()

                    if button_start_game.pressed and algoritm == 'Dijkstra' and dim:
                        settings.screen.fill('black')
                        unvisit_maze(settings.maze)
                        time_start = time.time()
                        dijkshtra(settings.maze, settings.maze_surf, True)
                        time_end = time.time()
                    
                        pc_rez.append((time_end - time_start, 'Dijkstra'))
                        with open("rezultate_pc.txt", "a", encoding="utf-8") as f:
                            f.write(f"\nDijkstra: {time_end - time_start} seconds")

                        camera_group.draw_map()

                    if button_start_game.pressed and algoritm is not None and dim:
                        is_meniu_pc = False
                        is_meniu_rezultate_pc = True
                        button_start_game.pressed = False
                        pc_rez.sort()

                if button_bfs.ispressed(pygame.mouse.get_pos()):
                    button_bfs.pressed = True
                    button_dfs.pressed = False
                    button_a.pressed = False
                    button_dijkstra.pressed = False
                    algoritm = 'BFS'

                if button_dfs.ispressed(pygame.mouse.get_pos()):
                    button_bfs.pressed = False
                    button_dfs.pressed = True
                    button_a.pressed = False
                    button_dijkstra.pressed = False
                    algoritm = 'DFS'
            
                if button_a.ispressed(pygame.mouse.get_pos()):
                    button_bfs.pressed = False
                    button_dfs.pressed = False
                    button_a.pressed = True
                    button_dijkstra.pressed = False
                    algoritm = 'A*'

                if button_dijkstra.ispressed(pygame.mouse.get_pos()):
                    button_bfs.pressed = False
                    button_dfs.pressed = False
                    button_a.pressed = False
                    button_dijkstra.pressed = True
                    algoritm = 'Dijkstra'

                if button_20x30.ispressed(pygame.mouse.get_pos()):
                    button_20x30.pressed = True
                    button_40x60.pressed = False
                    button_100x200.pressed = False
                    button_210x380.pressed = False
                    settings.change_maze_size(20,30)
                    classes.clear_maze()
                    screen.blit(meniu_empty)
                    Prim_algoritm(settings.maze, settings.maze_surf, True)
                    dim = True

                if button_40x60.ispressed(pygame.mouse.get_pos()):
                    button_20x30.pressed = False
                    button_40x60.pressed = True
                    button_100x200.pressed = False
                    button_210x380.pressed = False
                    settings.change_maze_size(40,60)
                    classes.clear_maze()
                    screen.blit(meniu_empty)
                    Prim_algoritm(settings.maze, settings.maze_surf, True)
                    dim = True
                
                if button_100x200.ispressed(pygame.mouse.get_pos()):
                    button_20x30.pressed = False
                    button_40x60.pressed = False
                    button_100x200.pressed = True
                    button_210x380.pressed = False
                    settings.change_maze_size(100,200)
                    classes.clear_maze()
                    screen.blit(meniu_empty)
                    Prim_algoritm(settings.maze, settings.maze_surf, True)
                    dim = True

                if button_210x380.ispressed(pygame.mouse.get_pos()):
                    button_20x30.pressed = False
                    button_40x60.pressed = False
                    button_100x200.pressed = False
                    button_210x380.pressed = True
                    settings.change_maze_size(210,380)
                    classes.clear_maze()
                    screen.blit(meniu_empty)
                    Prim_algoritm(settings.maze, settings.maze_surf, True)
                    dim = True

        if is_meniu_rezultate_om:
            screen.fill('black')
            screen.blit(meniu_rezultate_om)

            button_inapoi.draw(screen)
            button_1_om.draw(screen)
            button_2_om.draw(screen)
            button_3_om.draw(screen)
            button_4_om.draw(screen)
            button_5_om.draw(screen)
            button_6_om.draw(screen)
            button_7_om.draw(screen)

            if pygame.mouse.get_just_pressed()[0]:
                if button_inapoi.ispressed(pygame.mouse.get_pos()):
                    is_meniu_rezultate_om = False
                    is_meniu_start = True

            om_rez.clear()

            with open("rezultate_om.txt", "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        parts = line.split(":")
                        nume = parts[0].strip()
                        timp_text = parts[1].replace(" seconds", "").strip()
                        timp = round(float(timp_text), 4)
                        om_rez.append((timp, nume))

            om_rez.sort()

            if len(om_rez) >= 1:

                rez, alg = om_rez[0]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (63, 82))
                button_1_om.image.blit(pygame.image.load('Menus/button_1.jpeg').convert_alpha())
                button_1_om.image.blit(font_top, font_top_rect)

            if len(om_rez) >= 2:
                rez, alg = om_rez[1]

                top1: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top1, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (75, 48))
                button_2_om.image.blit(pygame.image.load('Menus/button_2.jpeg').convert_alpha())
                button_2_om.image.blit(font_top, font_top_rect)

            if len(om_rez) >= 3:
                rez, alg = om_rez[2]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (75, 48))
                button_3_om.image.blit(pygame.image.load('Menus/button_3.jpeg').convert_alpha())
                button_3_om.image.blit(font_top, font_top_rect)

            if len(om_rez) >= 4:
                rez, alg = om_rez[3]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (60, 25))
                button_4_om.image.blit(pygame.image.load('Menus/button_4.jpeg').convert_alpha())
                button_4_om.image.blit(font_top, font_top_rect)

            if len(om_rez) >= 5:
                rez, alg = om_rez[4]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (60, 25))
                button_5_om.image.blit(pygame.image.load('Menus/button_5.jpeg').convert_alpha())
                button_5_om.image.blit(font_top, font_top_rect)

            
            if len(om_rez) >= 6:
                rez, alg = om_rez[5]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (60, 25))
                button_6_om.image.blit(pygame.image.load('Menus/button_6.jpeg').convert_alpha())
                button_6_om.image.blit(font_top, font_top_rect)

            if len(om_rez) >= 7:
                rez, alg = om_rez[6]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (60, 25))
                button_7_om.image.blit(pygame.image.load('Menus/button_7.jpeg').convert_alpha())
                button_7_om.image.blit(font_top, font_top_rect)

        if is_meniu_rezultate_pc:
            screen.fill('black')
            screen.blit(meniu_rezultate_pc)

            button_inapoi.draw(screen)
            button_1.draw(screen)
            button_2.draw(screen)
            button_3.draw(screen)
            button_4.draw(screen)
            button_5.draw(screen)
            button_6.draw(screen)
            button_7.draw(screen)


            if pygame.mouse.get_just_pressed()[0]:
                if button_inapoi.ispressed(pygame.mouse.get_pos()):
                    is_meniu_rezultate_pc = False
                    is_meniu_pc = True

            if len(pc_rez) >= 1:
                rez, alg = pc_rez[0]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (63, 82))
                button_1.image.blit(pygame.image.load('Menus/button_1.jpeg').convert_alpha())
                button_1.image.blit(font_top, font_top_rect)

            if len(pc_rez) >= 2:
                rez, alg = pc_rez[1]

                top1: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top1, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (75, 48))
                button_2.image.blit(pygame.image.load('Menus/button_2.jpeg').convert_alpha())
                button_2.image.blit(font_top, font_top_rect)

            if len(pc_rez) >= 3:
                rez, alg = pc_rez[2]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (75, 48))
                button_3.image.blit(pygame.image.load('Menus/button_3.jpeg').convert_alpha())
                button_3.image.blit(font_top, font_top_rect)

            if len(pc_rez) > 4:
                rez, alg = pc_rez[3]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (60, 25))
                button_4.image.blit(pygame.image.load('Menus/button_4.jpeg').convert_alpha())
                button_4.image.blit(font_top, font_top_rect)

            if len(pc_rez) >= 5:
                rez, alg = pc_rez[4]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (60, 25))
                button_5.image.blit(pygame.image.load('Menus/button_5.jpeg').convert_alpha())
                button_5.image.blit(font_top, font_top_rect)

            
            if len(pc_rez) > 6:
                rez, alg = pc_rez[5]

                top: str = str(alg) + ': ' + str(rez)
                
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (60, 25))
                button_6.image.blit(pygame.image.load('Menus/button_6.jpeg').convert_alpha())
                button_6.image.blit(font_top, font_top_rect)

            if len(pc_rez) >= 7:
                rez, alg = pc_rez[6]

                top: str = str(alg) + ': ' + str(rez)
                font_top = font_rez.render(top, False, 'Red')
                font_top_rect = font_top.get_rect(topleft = (60, 25))
                button_7.image.blit(pygame.image.load('Menus/button_7.jpeg').convert_alpha())
                button_7.image.blit(font_top, font_top_rect)

        if is_meniu_login:
            screen.fill('black')
            screen.blit(meniu_login)

            button_20x30_om.draw(screen)
            button_40x60_om.draw(screen)
            button_100x200_om.draw(screen)
            button_inapoi.draw(screen)
            button_start_game.draw(screen)
            button_login.draw(screen)

            if pygame.mouse.get_just_pressed()[0]:
                
                button_login.pressed = False

                if button_20x30_om.ispressed(pygame.mouse.get_pos()):
                    button_20x30_om.pressed = True
                    button_40x60_om.pressed = False
                    button_100x200_om.pressed = False
                    settings.change_maze_size(20,30)
                    classes.clear_maze()

                if button_40x60_om.ispressed(pygame.mouse.get_pos()):
                    button_20x30_om.pressed = False
                    button_40x60_om.pressed = True
                    button_100x200_om.pressed = False
                    settings.change_maze_size(40,60)
                    classes.clear_maze()
                  
                if button_100x200_om.ispressed(pygame.mouse.get_pos()):
                    button_20x30_om.pressed = False
                    button_40x60_om.pressed = False
                    button_100x200_om.pressed = True
                    settings.change_maze_size(100,200)
                    classes.clear_maze()

                if button_inapoi.ispressed(pygame.mouse.get_pos()):
                    is_meniu_login = False
                    is_meniu_start = True

                if button_start_game.ispressed(pygame.mouse.get_pos()):
                    is_meniu_login = False
                    is_meniu_generare = True

                    global player
                    player = classes.Player(settings.maze[(0,0)], camera_group)

                if button_login.ispressed(pygame.mouse.get_pos()):
                    button_login.pressed = True
 
            login_name_surf = font.render(name, False, 'red')
            login_name_rect = login_name_surf.get_rect(topleft = (670,400))
            screen.blit(login_name_surf, login_name_rect)
  
        if is_meniu_generare:
            screen.fill('black')
            screen.blit(meniu_generation)

            button_randomdfs.draw(screen)
            button_prim.draw(screen)
            button_wilson.draw(screen)
            button_inapoi.draw(screen)

            if button_randomdfs.ispressed(pygame.mouse.get_pos()):
                settings.screen.fill('black')
                classes.clear_maze()
                Randomized_depth_first_search_iterative(settings.maze, settings.maze_surf, True)
                camera_group.draw_map()
                is_meniu_generare = False
                is_meniu_game = True
                initial_time = time.time()

            if button_prim.ispressed(pygame.mouse.get_pos()):
                settings.screen.fill('black')
                classes.clear_maze()
                Prim_algoritm(settings.maze, settings.maze_surf, True)
                camera_group.draw_map()
                is_meniu_generare = False
                is_meniu_game = True
                initial_time = time.time()

            if button_wilson.ispressed(pygame.mouse.get_pos()):
                settings.screen.fill('black')
                classes.clear_maze()
                Wilson_algorithm(settings.maze, settings.maze_surf, True)
                camera_group.draw_map()
                is_meniu_generare = False
                is_meniu_game = True
                initial_time = time.time()

            if button_inapoi.ispressed(pygame.mouse.get_pos()):
                is_meniu_generare = False
                is_meniu_login = True

        if is_meniu_game:
            if map: #Minimap
                settings.screen.fill('black')
                player.highlite(True)
                draw_maze(settings.maze, settings.rect, settings.maze_surf)
                player.highlite(False)

            else: #Game
                player.update(dt)
                camera_group.game_draw(player, dt)
            
                time_name_surf = font.render(f'Time: {round((time.time() - initial_time), 3)}s', True, 'black')
                time_name_rect = login_name_surf.get_rect(topleft = (1520, 30))
                screen.blit(time_name_surf, time_name_rect)

                if player.isplayer_there((settings.lines - 1, settings.rows - 1)):
                    final_time = time.time()
                    # print(name, final_time - initial_time)

                    with open("rezultate_om.txt", "a", encoding="utf-8") as f:
                        f.write(f"\n{name}: {final_time - initial_time} seconds")

                    is_meniu_game = False
                    is_meniu_rezultate_om = True

        # get_mouse_click()
        pygame.display.update() 
        settings.clock.tick(settings.ticks)

if __name__ == "__main__":
    main()