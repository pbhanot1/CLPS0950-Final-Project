# Snake Game Final Project - gameboard
# edited 04.26.23 by Priya Bhanot
# this file creates game initialization function
#pygame tutorials used: https://dr0id.bitbucket.io/legacy/pygame_tutorials.html, https://pyga.me/docs/

import pygame
import pygame_gui

pygame.init()

# game window setup: name, background color, animation frame rate, font, UI manager
pygame.display.set_caption("Dog Park Game")
screen = pygame.display.set_mode((700,600))
screen.fill((120,170,20))
clock = pygame.time.Clock()
font = pygame.font.Font('GloriaHallelujah-Regular.ttf', 35)
manager = pygame_gui.UIManager((700,600))

# create variable to control the main loop
running = True

# display screen
display = True
display_surface = pygame.Surface((300, 200))
display_surface.fill('White')
title_surface = font.render('Dog Park!', True, 'Black')
instructions_surface = pygame.image.load('instructions.png')

# create corgi avatar
corgi = pygame.image.load("corgi.png")

if display == True:
    # display screen buttons: instructions + start
    instructions_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((280, 280), (150, 30)), text='Instructions', manager=manager)
    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((280, 320), (150, 30)), text='Start', manager=manager)

# main game loop
while running:
    #UI timer
    time_delta = clock.tick(60)/1000.0
    if display == True:
        screen.blit(display_surface, (200, 200))
        manager.draw_ui(screen)
        screen.blit(corgi, (235, 300))
        screen.blit(title_surface, (280, 200))

    for event in pygame.event.get():
        # if an event is of QUIT type, main loop closes (game ends)
        if event.type == pygame.QUIT:
            running = False

        #button functions
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            #instructions button
            if event.ui_element == instructions_button:
                display = False
                screen.blit(instructions_surface,(200,200))
                back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((280, 350), (150, 30)),text='Main Page', manager=manager)
                if event.ui_element == back_button:
                    display = True
        # UI manager functions setup
        manager.process_events(event)
    manager.update(time_delta)

    pygame.display.update()
    clock.tick(60)



