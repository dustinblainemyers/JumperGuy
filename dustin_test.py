import pygame
import random
from os import path

# path.dirname : gets path of current directory that this file is located in by passing __file__. (__file__ is the current running python module) . 
# 
# path.join : 

img_dir2 = path.join(path.dirname(__file__), 'img2')

FPS = 30 
speed = 10

# WIDTH = 600
# HEIGHT = 480
# FPS = 60



# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize pygame and create window
pygame.init()



   # Loading the background image and setting variables for x coordinates


    
    # Setting window display size

subway_background1 = pygame.image.load(path.join(img_dir2, 'background.png'))
subway_background2 = pygame.image.load(path.join(img_dir2, 'background.png'))
width = subway_background1.get_width()
height = subway_background1.get_height()

subway_background1_x = 0
subway_background2_x = subway_background1.get_width()
screen = pygame.display.set_mode((width, height))
intro_background2 = pygame.image.load(path.join(img_dir2, 'menu.png')).convert()
intro_background_rect2 = intro_background2.get_rect()

intro_background2 = pygame.image.load(path.join(img_dir2, 'menu.png')).convert()
intro_background_rect2 = intro_background2.get_rect()




pygame.display.set_caption("SubwayFighter")
clock = pygame.time.Clock()



def show_menu_screen():
    screen.blit(intro_background2, intro_background_rect2)
    # draw_text(screen, "THIS IS THE MENU SCREEN", 64, WIDTH / 2, HEIGHT / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Any key press will start the game
            if event.type == pygame.KEYDOWN:
                waiting = False
    
# def maingame():
#     screen.blit(main_background, main_background_rect2)
#     # draw_text(screen, "THIS IS THE MENU SCREEN", 64, WIDTH / 2, HEIGHT / 4)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             # Any key press will start the game
#             if event.type == pygame.KEYDOWN:
#                 waiting = False

    
    # Game initialization and starting of main loop
def maingame():
    global subway_background1_x
    global subway_background2_x
    stop_game = False
    
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
        screen.blit(subway_background1, [subway_background1_x, 0])
        screen.blit(subway_background2, [subway_background2_x, 0])
        subway_background1_x -= speed
        subway_background2_x -= speed
    
        if subway_background1_x <= -1 * subway_background1.get_width():
            subway_background1_x = subway_background2_x + subway_background2.get_width()
        if subway_background2_x <= -1 * subway_background2.get_width():
            subway_background2_x = subway_background1_x + subway_background1.get_width()
    
        pygame.display.update()
    
    
    


 

    # Game logic

    # Drawing the moving background
    
    # screen.blit(subway_background1, [subway_background1_x, 0])
    # screen.blit(background_two, [subway_background2_x, 0])
    
    # subway_background1_x -= speed
    # subway_background2_x -= speed

    # if subway_background1_x <= -1 * subway_background1.get_width():
    #     subway_background1_x = subway_background2_x + background_two.get_width()
    # if subway_background2_x <= -1 * background_two.get_width():
    #     subway_background2_x = subway_background1_x + subway_background1.get_width()

    # pygame.display.update()





show_menu_screen()
maingame()

pygame.quit()