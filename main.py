import pygame
from pyautogui import size
import game_files.menu,game_files.game
import time
time = time.time()
pygame.mixer.init()
bg = pygame.mixer.music.load('game_files/sounds/background.mp3')

game_over_sound = pygame.mixer.Sound('game_files/sounds/game_over.mp3')
game_over_sound_played = False

game_win_sound = pygame.mixer.Sound('game_files/sounds/game_win.mp3')
game_win_sound_played = False

main_screen_sound = pygame.mixer.Sound('game_files/sounds/main_screen.mp3')
main_screen_sound_played = False

width,height = size()
height = height - (height*10/100) 
width = width -500
win = pygame.display.set_mode((width,height))
fps = 60
clock = pygame.time.Clock()

#Object initializing 
gm = game_files.game.Game(win,width,height)
mnu = game_files.menu.MenuScreens(win,width,height,gm,time)

#Used to get the rects positions and make collide with options and mouse
M_play_rect,M_quit_rect = 0,0
over_try_again_rect,over_quit_rect = 0,0
won_play_again_rect,won_quit_rect = 0,0

def when_gaming():
    # Initializing all values for the start of the game when player clicks the play/re-play buton 
    gm.game_start = True
    gm.game_over = False
    gm.game_won = False
    gm.player_surface_x = gm.surface_width/2
    gm.player_surface_y = gm.height /2
    gm.bot_surface_x = gm.width - gm.surface_width/2
    gm.bot_surface_y = gm.height/2
    gm.ball_x = gm.width / 2
    gm.ball_y = gm.height / 2
    gm.ball_rect = gm.ball_image.get_rect(center = (gm.ball_x,gm.ball_y))
    pygame.mixer.music.play(-1,0.0)
    gm.ball_velocity = pygame.Vector2(gm.width*0.7/100,gm.height*1/100)

while True:
    keys = pygame.key.get_pressed()
    left_click, middle, right = pygame.mouse.get_pressed(3)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if not gm.game_start:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if over_try_again_rect == 0 and won_play_again_rect == 0:
                    if M_play_rect.collidepoint(mouse):
                        when_gaming()
                if M_play_rect ==0 and won_play_again_rect == 0:
                    if over_try_again_rect.collidepoint(mouse):
                        when_gaming()

                if M_play_rect == 0 and over_try_again_rect == 0:
                    if won_play_again_rect.collidepoint(mouse):
                        when_gaming()
                
                if over_quit_rect == 0 and M_quit_rect == 0:
                    if won_quit_rect.collidepoint(mouse):
                        exit()

                if over_quit_rect ==0 and won_quit_rect == 0:
                    if M_quit_rect.collidepoint(mouse):
                        exit()  
                if M_quit_rect == 0 and won_quit_rect == 0:
                    if over_quit_rect.collidepoint(mouse):
                        exit()

    if gm.game_start:
        win.fill('#1f003a')
        pygame.mouse.set_visible(False)
        gm.draw()
        gm.update()
        gm.player_controls(keys)
        game_over_sound_played = False
        main_screen_sound_played = False
        game_win_sound_played = False
        main_screen_sound.stop()
        game_over_sound.stop()
        game_win_sound.stop()

    elif gm.main_screen:
        pygame.mouse.set_visible(True)
        M_play_rect,M_quit_rect = mnu.main_screen(mouse)
        over_try_again_rect,over_quit_rect = 0,0
        won_play_again_rect,won_qut_rect = 0,0

        pygame.mixer.music.stop()
        game_over_sound_played = False
        game_win_sound_played = False

        if not main_screen_sound_played:
            main_screen_sound.set_volume(0.5)
            main_screen_sound.play(-1)
            main_screen_sound_played = True

    elif gm.game_over:
        pygame.mouse.set_visible(True)
        over_try_again_rect,over_quit_rect = mnu.game_over_screen(mouse)
        M_play_rect,M_quit_rect = 0,0
        won_play_again_rect,won_quit_rect = 0,0

        pygame.mixer.music.stop()
        main_screen_sound_played = False
        game_win_sound_played = False
        
        if not game_over_sound_played:
            game_over_sound.play()
            game_over_sound_played = True

    elif gm.game_won:
        pygame.mouse.set_visible(True)
        won_play_again_rect,won_quit_rect = mnu.game_won_screen(mouse)
        M_play_rect,M_quit_rect = 0,0
        over_try_again_rect,over_quit_rect = 0,0

        pygame.mixer.music.stop()
        game_over_sound_played = False
        main_screen_sound_played = False
        
        if not game_win_sound_played:
            game_win_sound.set_volume(0.3)
            game_win_sound.play()
            game_win_sound_played = True

    pygame.display.update()
    clock.tick(fps)