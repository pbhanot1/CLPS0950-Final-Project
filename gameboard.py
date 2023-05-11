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
corgi = pygame.image.load('corgi.png')
treat = Tokens.Food(screen)
husky = Tokens.Husky(screen)
poodle = Tokens.Poodle(screen)
chow = Tokens.Chow(screen)
confirmation_dialog = pygame_gui.windows.UIConfirmationDialog(
    rect=pygame.Rect((275, 200), (260, 200)),
    manager=manager,
    window_title='Confirmation',
    action_long_desc='I need 3 treats to be your friend.',
    action_short_name='OK',
    blocking=True)

# create variable to control the main loop
def main():
    running = True
    x= 100
    y= 100
    global corgi_posx
    global corgi_posy

    counter = 0
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
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    confirmation_dialog.kill()
        screen.fill((120, 170, 20))
        pygame.time.delay(10)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= 10
        if keys[pygame.K_DOWN]:
            y += 10
        if keys[pygame.K_LEFT]:
            x -= 10
        if keys[pygame.K_RIGHT]:
            x += 10
        if keys[pygame.K_RETURN]:
            husky.popup(corgi_mask, corgi_posx, corgi_posy)
        if keys[pygame.K_SPACE]:
            counter = husky.collision(corgi_mask, corgi_posx, corgi_posy, counter)
            counter = poodle.collision(corgi_mask, corgi_posx, corgi_posy, counter)
            counter = chow.collision(corgi_mask, corgi_posx, corgi_posy, counter)
        corgi_posx = x
        corgi_posy = y
        screen.blit(corgi, (x, y))
        husky.husky_drawing(screen)
        poodle.poodle_drawing(screen)
        chow.chow_drawing(screen)
        treat.food_drawing(screen)
        counter = treat.collision(corgi_mask, corgi_posx, corgi_posy,counter)
        counter_text = font.render(f'Treats Collected: {counter}',True,(255,255,255))
        screen.blit(counter_text,(10,10))
        manager.update(time_delta)
        pygame.display.update()
        clock.tick(60)