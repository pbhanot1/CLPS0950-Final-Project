# tutorials used to write code are linked in the ReadME

# import libraries
import pygame
import pygame_menu
import pygame_gui
import gameboard
from pygame import mixer

#initialize pygame
pygame.init()

#background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# game window setup: name, background color, animation frame rate, font, UI manager
pygame.display.set_caption("Dog Park!")
menu_screen = pygame.display.set_mode((1200,900))

# create Menu function
def create_menu():
    def start_game():
        pygame.mixer.music.pause() # pauses background music because there are other sound effects in game
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