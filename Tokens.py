import pygame, sys
import pygame_menu
import random
import gameboard
import pygame_gui
pygame.init()
screen = pygame.display.set_mode((1200, 900))
class Food(object):
# tutorial used for counter: https://opensource.com/article/20/1/add-scorekeeping-your-python-game
    def __init__(self,food_screen):
        self.image= pygame.transform.scale(pygame.image.load("treatbone.png").convert(),(40,20))
        self.food_screen=food_screen
        self.eaten = False
      #  self.food_spawn()
        self.x = 200
        self.y = 200

  #  def food_spawn(self):
   #     self.x = random.randrange(0, 800, 1)
   #     self.y = random.randrange(0, 800, 1)

    def food_drawing(self,win):
        self.food_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    #def move(self,win, corgi_posx, corgi_posy):
        #if self.is_in_range(self.x, corgi_posx - 20, corgi_posy + 20) and self.is_in_range(self.y, corgi_posy - 20, corgi_posy + 20):
            #print('collide')
            #self.x = random.randint(0,1200)*40
            #self.y = random.randint(0,900)*20
            #self.food_screen.blit(self.image, (self.x, self.y))
            #pygame.display.flip()


    def collision(self, corgi_mask, corgi_posx, corgi_posy):
        # creates a treat mask (ignores transparent pixels)
        treat_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx), int(self.y - corgi_posy))

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(treat_mask, offset)  # point of intersection

        if poi != None:
            self.x = random.randint(0,1000)
            self.y = random.randint(0,700)
            self.food_screen.blit(self.image, (self.x, self.y))
            pygame.display.flip()
