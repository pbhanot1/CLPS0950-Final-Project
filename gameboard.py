# Snake Game Final Project - gameboard
# edited 04.24.23 by Priya Bhanot

# this file will initialize the snake game arena, avatar options, and basic tokens

import pygame
#pygame tutorial used: https://dr0id.bitbucket.io/legacy/pygame_tutorials.html
# gameboard initialization

# create main function to control overall gameplay.
def main():
    # pygame module initialization
    pygame.init()
    # display game name above playing arena
    pygame.display.set_caption("Snake Game")
    # create arena surface of size 700x600 and set background color
    arena = pygame.display.set_mode((700,600))
    arena.fill((120,170,20))
    # load corgi avatar in arena
    corgi = pygame.image.load("corgi.png")
    arena.blit(corgi,(50,50))
    pygame.display.flip()
    # create variable to control the main loop
    running = True

    # main loop
    while running:
        for event in pygame.event.get():
            # if an event is of QUIT type, main loop closes (game ends)
            if event.type == pygame.QUIT:
                running = False

main()



