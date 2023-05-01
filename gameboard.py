# Snake Game Final Project - gameboard
# edited 04.26.23 by Priya Bhanot
# pygame tutorials used: https://dr0id.bitbucket.io/legacy/pygame_tutorials.html, https://pyga.me/docs/

# import libraries
import pygame
import pygame_menu
import pygame_gui

#initialize pygame
pygame.init()

# game window setup: name, background color, animation frame rate, font, UI manager
pygame.display.set_caption("Dog Park Game")
screen = pygame.display.set_mode((1200,900))
screen.fill((120, 170, 20))
clock = pygame.time.Clock()
font = pygame.font.Font('GloriaHallelujah-Regular.ttf', 35)
manager = pygame_gui.UIManager((1200,900))

# characters
corgi = pygame.image.load('corgi.png')
screen.blit(corgi, (100,100))

husky = pygame.image.load('husky.png')
screen.blit(husky, (950,100))
poodle = pygame.image.load('poodle.png')
screen.blit(poodle, (600,450))
mavi = pygame.image.load('mavi.png')
screen.blit(mavi, (300,800))

# create variable to control the main loop
running = True

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

    manager.update(time_delta)

    pygame.display.update()
    clock.tick(60)



