# import libraries
import pygame
import pygame_menu
import random
import gameboard
from pygame import mixer

#initialize screen
pygame.init()
screen = pygame.display.set_mode((1200, 900))
font = pygame.font.Font('GloriaHallelujah-Regular.ttf', 35)

# object-oriented programming for treat token

# created class for treats
class Food():
    def __init__(self,food_screen):
        self.image = pygame.image.load("treatbone.png")
        self.food_screen=food_screen
        self.x = 200
        self.y = 200

    # draws character on screen
    def food_drawing(self,win):
        self.food_screen.blit(self.image, (self.x, self.y))

# determines whether corgi and treat are overlapping
    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        # creates a treat mask
        treat_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx), int(self.y - corgi_posy))

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(treat_mask, offset)  # point of intersection

# if corgi and treat are overlapping, counter changes and treat moves elsewhere on screen
        if poi != None:
            self.x = random.randint(100,1000)
            self.y = random.randint(100,800)
            self.food_screen.blit(self.image, (self.x, self.y))
            chew_sound = mixer.Sound('chewsound.wav')
            chew_sound.play()
            counter += 1
            return counter
        else:
            return counter

# created class for Husky character
class Husky():
    def __init__(self, husky_screen):
        self.image = pygame.image.load("husky.png")
        self.husky_screen = husky_screen
        self.x = 750
        self.y = 50

# draws husky on screen
    def husky_drawing(self,win):
        self.husky_screen.blit(self.image, (self.x, self.y))

# determines whether corgi and husky are close together
    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        # creates a treat mask
        husky_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx) - 50, int(self.y - corgi_posy)+50)

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(husky_mask, offset)  # point of intersection

# if corgi has enough treats and is close enough, then counter changes, husky updates
        if poi != None:
            if counter >= 3:
                counter = counter - 3
                self.image = pygame.image.load('huskythanks.png')
                wahoo_sound = mixer.Sound('wahoo.ogg')
                pygame.time.delay(300)
                wahoo_sound.play()
            return counter
        else:
            return counter

# creates class for poodle character
class Poodle():
    def __init__(self, poodle_screen):
        self.image = pygame.image.load("poodle.png")
        self.poodle_screen = poodle_screen
        self.x = 500
        self.y = 450

# draws poodle on screen
    def poodle_drawing(self,win):
        self.poodle_screen.blit(self.image, (self.x, self.y))

# determines whether corgi and poodle are near each other
    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        # creates a treat mask
        poodle_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx) - 50, int(self.y - corgi_posy)+50)

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(poodle_mask, offset)  # point of intersection

# treats are "given" to poodle and counter updates, and dog is marked as a friend
        if poi != None:
            if counter >= 10:
                counter = counter - 10
                self.image = pygame.image.load('poodlethanks.png')
                harp_sound = mixer.Sound('harp.mp3')
                pygame.time.delay(300)
                harp_sound.play()
            return counter
        else:
            return counter

# creates new class for chow chow dog character
class Chow():
    def __init__(self, chow_screen):
        self.image = pygame.image.load("mavi.png")
        self.chow_screen = chow_screen
        self.x = 190
        self.y = 700

    # draws chow dog on screen
    def chow_drawing(self,win):
        self.chow_screen.blit(self.image, (self.x, self.y))

# determines whether corgi is near chow
    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        chow_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx) - 50, int(self.y - corgi_posy)+50)

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(chow_mask, offset)  # point of intersection
# updates counter by "giving" treats to chow, sound effect, changes chow image to a friend
        if poi != None:
            if counter >= 5:
                counter = counter - 5
                self.image = pygame.image.load('mavithanks.png')
                howl_sound = mixer.Sound('howl.wav')
                pygame.time.delay(300)
                howl_sound.play()
            return counter
        else:
            return counter

# creates class for golden retriever character
class Golden():
    def __init__(self, golden_screen):
        self.image = pygame.image.load("golden.png")
        self.golden_screen = golden_screen
        self.x = 350
        self.y = 200

   # draws golden retriever
    def golden_drawing(self,win):
        self.golden_screen.blit(self.image, (self.x, self.y))

    # determines whether corgi and golden are close enough
    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        # creates a treat mask (ignores transparent pixels)
        golden_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx) - 50, int(self.y - corgi_posy)+50)

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(golden_mask, offset)  # point of intersection

# changes counter by "giving" treats to golden, plays sound, changes character image to a friend
        if poi != None:
            if counter >= 4:
                counter = counter - 4
                self.image = pygame.image.load('goldenthanks.png')
                golden_sound = mixer.Sound('goldensound.mp3')
                pygame.time.delay(300)
                golden_sound.play()
            return counter
        else:
            return counter

# creates class for pug character
class Pug():
    def __init__(self, pug_screen):
        self.image = pygame.image.load("pug.png")
        self.pug_screen = pug_screen
        self.x = 800
        self.y = 650

    # draws pug on screen
    def pug_drawing(self,win):
        self.pug_screen.blit(self.image, (self.x, self.y))

 # determines whether corgi and pug are close enough
    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        # creates a treat mask (ignores transparent pixels)
        pug_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx) - 50, int(self.y - corgi_posy)+50)

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(pug_mask, offset)  # point of intersection

# "gives" treats to pug and changes counter, updates image to indicate dog is a friend
        if poi != None:
            if counter >= 3:
                counter = counter - 3
                self.image = pygame.image.load('pugthanks.png')
                pug_sound = mixer.Sound('pugsound.mp3')
                pygame.time.delay(300)
                pug_sound.play()
            return counter
        else:
            return counter

# creates new class for border collie dog character
class Collie():
    def __init__(self, collie_screen):
        self.image = pygame.image.load("collie.png")
        self.collie_screen = collie_screen
        self.x = 0
        self.y = 450

    # draws border collie character on screen
    def collie_drawing(self,win):
        self.collie_screen.blit(self.image, (self.x, self.y))

    # determines whether corgi and border collie are close enough
    def collision(self, corgi_mask, corgi_posx, corgi_posy, counter):
        # creates a treat mask (ignores transparent pixels)
        collie_mask = pygame.mask.from_surface(self.image)

        # checks the offset position of the treat relative to the dog
        offset = (int(self.x - corgi_posx) - 50, int(self.y - corgi_posy)+50)

        # looks for a point of intersection between the treat and the dog
        poi = corgi_mask.overlap(collie_mask, offset)  # point of intersection

# "gives" treats to border collie if close enough, updates counter, plays sound, changes image to indicate friend
        if poi != None:
            if counter >= 2:
                counter = counter - 2
                self.image = pygame.image.load('colliethanks.png')
                cricket_sound = mixer.Sound('cricketchirp.mp3')
                pygame.time.delay(300)
                cricket_sound.play()
            return counter
        else:
            return counter
