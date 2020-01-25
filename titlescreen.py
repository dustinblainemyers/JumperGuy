def titlescreen():
    import pygame

    # Loading the background images

    background_one = pygame.image.load('background.png')
    background_two = pygame.image.load('background2.png')

    # Loading main logo and instructions

    logo = pygame.image.load('logo.png')
    instructions = pygame.image.load('instructions.png')

    # Setting variables for x-coordinates

    background_one_x = 0
    background_two_x = background_one.get_width()

    # Setting window display size

    width = background_one.get_width()
    height = background_one.get_height()
    screen = pygame.display.set_mode((width, height))

    # Initializing pygame, the clock, and setting the game caption.

    pygame.init()
    pygame.display.set_caption('Jumper Guy')
    clock = pygame.time.Clock()

    # Setting Speed
    speed = 10

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.KEYDOWN:
                stop_game = True
            if event.type == pygame.QUIT:
                exit()

        # displaying the background on the screen.
        screen.blit(background_one, [background_one_x, 0])
        screen.blit(background_two, [background_two_x, 0])

        background_one_x -= speed
        background_two_x -= speed

        if background_one_x <= -1 * background_one.get_width():
            background_one_x = background_two_x + background_two.get_width()
        if background_two_x <= -1 * background_two.get_width():
            background_two_x = background_one_x + background_one.get_width() + 1

        # Displaying main logo and instructions

        screen.blit(logo, [0, -90])
        screen.blit(instructions, [0, 90])

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
