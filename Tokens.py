import pygame, sys
import pygame_menu
import random
import pygame_gui
pygame.init()
screen = pygame.display.set_mode((1200, 900))
class Food(object):
# tutorial used for counter: https://opensource.com/article/20/1/add-scorekeeping-your-python-game
    def __init__(self,food_screen):
        self.image= pygame.transform.scale(pygame.image.load("treatbone.png").convert(),(40,20))
        self.food_screen=food_screen
        self.eaten = False
        self.food_spawn()

    def food_spawn(self):
        self.food_x = random.randrange(0, 800, 1)
        self.food_y = random.randrange(0, 800, 1)

    def food_drawing(self,win):
        self.food_screen.blit(self.image, (self.food_x, self.food_y))
        pygame.display.flip()