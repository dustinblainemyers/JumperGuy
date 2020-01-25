<<<<<<< HEAD

# Importing score for display.


    

def exitscreen():
=======
def exitfun():
>>>>>>> 27daa9accc34d1a53ec26fb9a44e30f73df8772a
    import pygame

     # Loading the background image and setting variables for x coordinates

    background_one = pygame.image.load('background.png')
    background_two = pygame.image.load('background2.png')

    # loading the death logo and death instructions.

    death = pygame.image.load('death.png')
<<<<<<< HEAD
    tryagain = pygame.image.load('tryagain.png')

    # Setting background x-coordinate variables.
=======
    
    # Setting background x-coordinate variables.

>>>>>>> 27daa9accc34d1a53ec26fb9a44e30f73df8772a
    background_one_x = 0
    background_two_x = background_one.get_width()

    # Setting window display size

    width = background_one.get_width()
    height = background_one.get_height()
    screen = pygame.display.set_mode((width, height))

    # initializing pygame, the clock, and setting game caption.
    pygame.init()
    pygame.display.set_caption('Jumper Guy')
    clock = pygame.time.Clock()

    # Setting Speed 
    speed = 10

    # Setting font

    myfont = pygame.font.Font('8bit16.ttf', 28)
    # score_text = myfont.render('final score =  {}'.format(score), 1, (255,255,255))

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.KEYDOWN:
                stop_game = True
            if event.type == pygame.QUIT:
                exit()
<<<<<<< HEAD
=======
          

>>>>>>> 27daa9accc34d1a53ec26fb9a44e30f73df8772a

        # Draw background
        screen.blit(background_one, [background_one_x, 0])
        screen.blit(background_two, [background_two_x, 0])
        
        background_one_x -= speed
        background_two_x -= speed

        if background_one_x <= -1 * background_one.get_width():
            background_one_x = background_two_x + background_two.get_width()
        if background_two_x <= -1 * background_two.get_width():
            background_two_x = background_one_x + background_one.get_width() + 1

        # Adding the exit screen logo, score, and text. 

<<<<<<< HEAD
        screen.blit(death, [0, 0])
        screen.blit(tryagain, [0, 90])
        # screen.blit(score_text, [0,0])

=======
        screen.blit(death, [0, 90])
        
        
>>>>>>> 27daa9accc34d1a53ec26fb9a44e30f73df8772a
        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()