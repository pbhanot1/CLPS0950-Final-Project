# import libraries
import pygame
from pygame import mixer
import pygame_menu
import pygame_gui
import Tokens


#initialize pygame !
pygame.init()

# game window setup: name, background color, animation frame rate, font, UI manager
pygame.display.set_caption("Dog Park Game")
menu_screen = pygame.display.set_mode((1200,900))

# gameboard initialization and setup
pygame.init()
screen = pygame.display.set_mode((1200, 900))
background = pygame.image.load('background.png')
clock = pygame.time.Clock()
font = pygame.font.Font('GloriaHallelujah-Regular.ttf', 35)
manager = pygame_gui.UIManager((1200, 900))


#characters
corgi = pygame.image.load('corgi.png')
# the characters below are coded as objects and each have their own class in the Tokens.py file
treat = Tokens.Food(screen)
husky = Tokens.Husky(screen)
poodle = Tokens.Poodle(screen)
chow = Tokens.Chow(screen)
golden = Tokens.Golden(screen)
pug = Tokens.Pug(screen)
collie = Tokens.Collie(screen)

# main game loop
def main():
    # variable to run loop
    running = True

    # initialize variables for corgi position and movement
    x= 100
    y= 100
    global corgi_posx
    global corgi_posy

    # initialize treat counter
    counter = 0

    # creates corgi mask for collision functions in Tokens.py
    corgi_mask = pygame.mask.from_surface(corgi)

    # main game function
    while running:
        #UI timer
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            # if an event is of QUIT type, main loop closes (game ends)
            if event.type == pygame.QUIT:
                running = False
            # UI manager functions setup
            manager.process_events(event)
        screen.fill((120, 170, 20))
        pygame.time.delay(5)
        # corgi movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= 10
        if keys[pygame.K_DOWN]:
            y += 10
        if keys[pygame.K_LEFT]:
            x -= 10
        if keys[pygame.K_RIGHT]:
            x += 10
        if keys[pygame.K_SPACE]:
            # bark sound when space bar is pressed
            bark_sound = mixer.Sound('bark.wav')
            bark_sound.play()
            # calls collision code in Tokens.py for giving treats to dog and adjusting counter
            counter = husky.collision(corgi_mask, corgi_posx, corgi_posy, counter)
            counter = poodle.collision(corgi_mask, corgi_posx, corgi_posy, counter)
            counter = chow.collision(corgi_mask, corgi_posx, corgi_posy, counter)
            counter = golden.collision(corgi_mask, corgi_posx, corgi_posy, counter)
            counter = pug.collision(corgi_mask, corgi_posx, corgi_posy, counter)
            counter = collie.collision(corgi_mask, corgi_posx, corgi_posy, counter)
        corgi_posx = x
        corgi_posy = y
        screen.blit(background, (0, 0))
        # draws characters and treats on the screen after arrow keys are pressed
        screen.blit(corgi, (x, y))
        husky.husky_drawing(screen)
        poodle.poodle_drawing(screen)
        chow.chow_drawing(screen)
        golden.golden_drawing(screen)
        pug.pug_drawing(screen)
        collie.collie_drawing(screen)
        treat.food_drawing(screen)
        # calls treat collision code in Tokens.py for treat collection and displays counter
        counter = treat.collision(corgi_mask, corgi_posx, corgi_posy,counter)
        counter_text = font.render(f'Treats Collected: {counter}',True,(255,255,255))
        screen.blit(counter_text,(10,10))
        manager.update(time_delta)
        pygame.display.update()
        clock.tick(60)