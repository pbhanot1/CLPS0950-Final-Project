# import libraries
import pygame, sys
import pygame_menu
import pygame_gui
import gameboard

#initialize pygame
pygame.init()

# game window setup: name, background color, animation frame rate, font, UI manager
pygame.display.set_caption("Dog Park Game")
menu_screen = pygame.display.set_mode((1200,900))
game = False

# create Menu function
def create_menu():
    def start_game():
        gameboard.main()

    def back_button():
            menu.mainloop(menu_screen)
    def the_instructions():
            instructions = pygame_menu.Menu('Instructions', 800, 600, theme=pygame_menu.themes.THEME_SOLARIZED)
            instruction_img = pygame.image.load("instructions.png")
            instructions.add.surface(instruction_img)
            instructions.add.button('Back to Menu', back_button)
            instructions.mainloop(menu_screen)

    menu = pygame_menu.Menu('Dog Park!', 600, 400, theme=pygame_menu.themes.THEME_SOLARIZED)
    logo = pygame.image.load("logo.png")
    menu.add.surface(logo)
    menu.add.button('Start', start_game)
    menu.add.button('Instructions', the_instructions)
    menu.add.button('Quit Game', pygame_menu.events.EXIT)
    menu.mainloop(menu_screen)

create_menu()