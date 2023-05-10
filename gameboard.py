# Snake Game Final Project - gameboard
# edited 04.26.23 by Priya Bhanot
# pygame tutorials used: https://dr0id.bitbucket.io/legacy/pygame_tutorials.html, https://pyga.me/docs/

# import libraries
import pygame, sys
import pygame_menu
import pygame_gui
import Tokens


#initialize pygame !
pygame.init()

# game window setup: name, background color, animation frame rate, font, UI manager
pygame.display.set_caption("Dog Park Game")
menu_screen = pygame.display.set_mode((1200,900))
game = False

# gameboard initialization and setup

pygame.init()
screen = pygame.display.set_mode((1200, 900))
background = screen.fill((120, 170, 20))
clock = pygame.time.Clock()
font = pygame.font.Font('GloriaHallelujah-Regular.ttf', 35)
manager = pygame_gui.UIManager((1200, 900))
#characters
husky = pygame.image.load('husky.png')
screen.blit(husky, (950,100))
poodle = pygame.image.load('poodle.png')
screen.blit(poodle, (600,450))
mavi = pygame.image.load('mavi.png')
screen.blit(mavi, (300,800))
corgi = pygame.image.load('corgi.png')
treat = Tokens.Food(screen)

# create variable to control the main loop
def main():
    running = True
    x= 100
    y= 100
    global corgi_posx
    global corgi_posy
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
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= 10
        if keys[pygame.K_DOWN]:
            y += 10
        if keys[pygame.K_LEFT]:
            x -= 10
        if keys[pygame.K_RIGHT]:
            x += 10
        screen.blit(husky, (950, 100))
        screen.blit(poodle, (600, 450))
        screen.blit(mavi, (300, 800))
        corgi_posx = x
        corgi_posy = y
        screen.blit(corgi, (x, y))
        treat.food_drawing(screen)
        treat.collision(corgi_mask, corgi_posx, corgi_posy)
        pygame.display.update()
        manager.update(time_delta)
        pygame.display.update()
        clock.tick(60)