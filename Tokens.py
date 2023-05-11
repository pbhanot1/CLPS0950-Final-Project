# import libraries
import pygame, sys
import pygame_menu
import random
import gameboard
import pygame_gui

#initialize screen
pygame.init()
screen = pygame.display.set_mode((1200, 900))
font = pygame.font.Font('GloriaHallelujah-Regular.ttf', 35)
manager = pygame_gui.UIManager((800, 600))
clock = pygame.time.Clock()
# object-oriented programming for treat token
class Food(object):
# tutorial used for counter: https://opensource.com/article/20/1/add-scorekeeping-your-python-game, https://www.makeuseof.com/pygame-game-scores-displaying-updating/
    def __init__(self,food_screen):
        self.image = pygame.image.load("treatbone.png")
        self.food_screen=food_screen
      #  self.food_spawn()
        self.x = 200
        self.y = 200

    def food_drawing(self,win):
        self.food_screen.blit(self.image, (self.x, self.y))


    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        # creates a treat mask (ignores transparent pixels)
        treat_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx), int(self.y - corgi_posy))

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(treat_mask, offset)  # point of intersection

        if poi != None:
            self.x = random.randint(100,1000)
            self.y = random.randint(100,800)
            self.food_screen.blit(self.image, (self.x, self.y))
            counter += 1
            return counter
        else:
            return counter

class Husky():
    def __init__(self, husky_screen):
        self.image = pygame.image.load("husky.png")
        self.husky_screen = husky_screen
        #  self.food_spawn()
        self.x = 950
        self.y = 100
    def husky_drawing(self,win):
        self.husky_screen.blit(self.image, (self.x, self.y))
    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        husky_mask = pygame.mask.from_surface(self.image)
        offset = (int(self.x - corgi_posx) + 10, int(self.y - corgi_posy)+10)
        poi = corgi_mask.overlap(husky_mask, offset)  # point of intersection

        if poi != None:
            # pop up comes
            if counter >= 3:
                counter = counter - 3
                self.image = pygame.image.load('huskyfriend.png')
                #pop up message thx im ur friend
            return counter
        else:
            return counter

    #def popup(self, corgi_mask, corgi_posy, corgi_posx):
        #husky_mask = pygame.mask.from_surface(self.image)
       # offset = (int(self.x - corgi_posx) + 10, int(self.y - corgi_posy) + 10)
        #poi = corgi_mask.overlap(husky_mask, offset)  # point of intersection

        #if poi != None:
         #   confirmation_dialog = pygame_gui.windows.UIConfirmationDialog(
          #      rect=pygame.Rect((275, 200), (250, 150)),
          #      manager=manager,
           #     window_title='Confirmation',
            #    action_long_desc='I need 3 treats to be your friend.',
             #   action_short_name='OK',
              #  blocking=False)
          #  is_running = True
           # while is_running:
            #    time_delta = clock.tick(60) / 1000.0

             #   for event in pygame.event.get():
              #      if event.type == pygame.QUIT:
               #         is_running = False

                #    manager.process_events(event)

                 #   if event.type == pygame.USEREVENT:
                  #      if event.type == pygame_gui.UI_BUTTON_PRESSED:
                   #         confirmation_dialog.kill()

class Poodle():
    def __init__(self, poodle_screen):
        self.image = pygame.image.load("poodle.png")
        self.poodle_screen = poodle_screen
        #  self.food_spawn()
        self.x = 600
        self.y = 450
    def poodle_drawing(self,win):
        self.poodle_screen.blit(self.image, (self.x, self.y))

    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        # creates a treat mask (ignores transparent pixels)
        poodle_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx) + 10, int(self.y - corgi_posy)+10)

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(poodle_mask, offset)  # point of intersection

        if poi != None:
            # pop up comes
            if counter >= 6:
                counter = counter - 6
                self.image = pygame.image.load('poodlefriend.png')
                #pop up message thx im ur friend
            return counter
        else:
            return counter

class Chow():
    def __init__(self, chow_screen):
        self.image = pygame.image.load("mavi.png")
        self.chow_screen = chow_screen
        #  self.food_spawn()
        self.x = 300
        self.y = 800
    def chow_drawing(self,win):
        self.chow_screen.blit(self.image, (self.x, self.y))

    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        # creates a treat mask (ignores transparent pixels)
        chow_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx) + 10, int(self.y - corgi_posy)+10)

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(chow_mask, offset)  # point of intersection

        if poi != None:
            # pop up comes
            if counter >= 2:
                counter = counter - 2
                self.image = pygame.image.load('mavifriend.png')
                #pop up message thx im ur friend
            return counter
        else:
            return counter