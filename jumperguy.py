import pygame
import sys
import random
pygame.font.init()
from titlescreen import titlescreen
from exitscreen import exitscreen

# Calling the title screen

lastloc = 1000

titlescreen()




def main():

    # Loading the background image and setting variables for x coordinates
    
    
    background_one = pygame.image.load('background.png')
    background_two = pygame.image.load('background2.png')

    background_one_x = 0
    background_two_x = background_one.get_width()

    # Setting window display size

    WIDTH = 1000
    HEIGHT = 350
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    

    # define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    
    # Initiliazing pygame, setting game caption, and initializing clock.
    
    pygame.init()
    pygame.display.set_caption('Jumper guy')
    clock = pygame.time.Clock()

    #frame tracker to randomly put obstacles on screen
    frame_tracker = 0

    # Setting the speed of FPS limit, and speed of the background, bigger numbers mean faster speed.
    
    FPS = 60
    speed = 10
    
    # Setting score variable and font

    myfont = pygame.font.Font('8bit16.ttf', 28)
    
    real_score = 0
    score = 0
    
    global is_jumping 
    is_jumping = False
    global jump_count
    jump_count = 10

    class Player(pygame.sprite.Sprite):
        
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 40))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0
        def update(self):
            self.rect.x += self.speedx
            global is_jumping
            global jump_count
            if is_jumping: 
                while jump_count > 5:
                    self.rect.bottom += 1
                    jump_count -= 1
                while jump_count > 0:
                    self.rect.bottom -= 1
                    jump_count -= 1
                
                
                jump_count = 10
            is_jumping = False


    class Mob(pygame.sprite.Sprite):
       def __init__(self, x_location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x_location
        self.rect.y = 250
        self.speedy = 0
        self.speedx = -10
        
        # lastloc = 1000
        
       def update(self):
           self.rect.x += self.speedx
           
           
        
           if self.rect.x < -25  :
            obstacle_generation(self)
       
            
            
        #    if lastloc > 3000:
        #        lastloc = 1000 
    def obstacle_generation(obstacle):
           global lastloc
           obstacle.rect.x = lastloc + 100
           obstacle.rect.y = 250
           lastloc = obstacle.rect.x
           print(obstacle.rect.x)
           

    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    mobs = pygame.sprite.Group()

    for i in range(1):
        m = Mob(lastloc + random.randrange(1500))
        all_sprites.add(m)
        mobs.add(m)
        

    # Game initialization and starting of main loop

    stop_game = False
    while not stop_game:
        
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            is_jumping = True
            pygame.time
            
            
           


        #Logic to randomly place obstacles

        if frame_tracker % 300 == 0:
            for i in range(1):
                m = Mob(lastloc + random.randrange(1500))
                all_sprites.add(m)
                mobs.add(m)

        # Drawing the moving background
        
        screen.blit(background_one, [background_one_x, 0])
        screen.blit(background_two, [background_two_x, 0])
        
        background_one_x -= speed
        background_two_x -= speed

        if background_one_x <= -1 * background_one.get_width():
            background_one_x = background_two_x + background_two.get_width()
        if background_two_x <= -1 * background_two.get_width():
            background_two_x = background_one_x + background_one.get_width() + 1

        # Adding to the score and displaying it.
        real_score += 1
        score_text = myfont.render('Score = {}'.format(score), 1, (255,255,255))
        screen.blit(score_text, [10,320])

        if real_score % 10 == 0:
            score +=1

        all_sprites.update() 
        all_sprites.draw(screen)
        pygame.display.flip()   
        pygame.display.update()
        frame_tracker += 1
        
        # Game clock
        clock.tick(FPS)
         
    exitscreen()

    pygame.quit()

    

if __name__ == '__main__':
    main()
