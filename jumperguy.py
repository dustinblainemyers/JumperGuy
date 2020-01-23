import pygame
import sys
pygame.font.init()

def main():

    # Loading the background image and setting variables for x coordinates

    background_one = pygame.image.load('background.png')
    background_two = pygame.image.load('background2.png')
    # background_three = pygame.image.load('background3.png')

    background_one_x = 0
    background_two_x = background_one.get_width()
    # background_three_x = background_two.get_width()

    # Setting window display size

    width = background_one.get_width()
    height = background_one.get_height()
    screen = pygame.display.set_mode((width, height))

    # Initiliazing pygame, setting game caption, and initializing clock.
    
    pygame.init()
    pygame.display.set_caption('Jumper guy')
    clock = pygame.time.Clock()

    # Setting the speed of fps limit, and speed of the background, bigger numbers mean faster speed.
    
    fps = 60 
    speed = 10
    
    # Setting score variable and font

    myfont = pygame.font.Font('8bit16.ttf', 28)
    score = 0
    real_score = 0

    # Game initialization and starting of main loop

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        

        # Drawing the moving background
        
        screen.blit(background_one, [background_one_x, 0])
        screen.blit(background_two, [background_two_x, 0])
        # screen.blit(background_three, [background_three_x, 0])
        
        background_one_x -= speed
        background_two_x -= speed
        # background_three_x -= speed

        if background_one_x <= -1 * background_one.get_width():
            background_one_x = background_two_x + background_two.get_width()
        if background_two_x <= -1 * background_two.get_width():
            background_two_x = background_one_x + background_one.get_width()
        # if background_three_x <= -1 * background_three.get_width():
        #     background_three_x = background_two_x + background_two.get_width()

        # Adding to the score and displaying it.
        real_score += 1
        score_text = myfont.render('Score = {}'.format(score), 1, (255,255,255))
        screen.blit(score_text, [10,320])

        if real_score % 10 == 0:
            score +=1
            
        pygame.display.update()
        
        # Game clock
        clock.tick(fps)
         

    pygame.quit()

if __name__ == '__main__':
    main()
