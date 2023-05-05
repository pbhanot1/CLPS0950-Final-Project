# Snake Game Final Project - gameboard
# edited 04.26.23 by Priya Bhanot
# pygame tutorials used: https://dr0id.bitbucket.io/legacy/pygame_tutorials.html, https://pyga.me/docs/

# import libraries
import pygame, sys
import pygame_menu
import pygame_gui

#initialize pygame
pygame.init()

# game window setup: name, background color, animation frame rate, font, UI manager
pygame.display.set_caption("Dog Park Game")
menu_screen = pygame.display.set_mode((1200,900))
game = False

# create Menu function
def create_menu():
    def start_game():
        sys.exit(menu_screen)
        game = True
        screen=pygame.display.set_mode((1200, 900))
        background = screen.fill((120, 170, 20))
        clock = pygame.time.Clock()
        font = pygame.font.Font('GloriaHallelujah-Regular.ttf', 35)
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

if game == False:
    create_menu()
else:
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    background = screen.fill((120, 170, 20))
    clock = pygame.time.Clock()
    font = pygame.font.Font('GloriaHallelujah-Regular.ttf', 35)
    manager = pygame_gui.UIManager((1200, 900))
    #characters
    husky = pygame.image.load('husky.png')
    screen.blit(husky, (950,100))
    poodle = pygame.image.load('poodle.png')
    screen.blit(poodle, (600,450))
    mavi = pygame.image.load('mavi.png')
    screen.blit(mavi, (300,800))
    corgi = pygame.image.load('corgi.png')
    def corgi_moves(x,y):
        Player=screen.blit(corgi, (x,y))
        run=True
        while run:
            screen.fill((120, 170, 20))
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            keys=pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y-=10
            if keys[pygame.K_DOWN]:
                y+=10
            if keys[pygame.K_LEFT]:
                x-=10
            if keys[pygame.K_RIGHT]:
                x+=10
            screen.blit(husky, (950, 100))
            screen.blit(poodle, (600, 450))
            screen.blit(mavi, (300, 800))
            Player=screen.blit(corgi,(x,y))
            pygame.display.update()
    corgi_moves(100,100)

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
        #if game_state=='menu':
            #create_menu()
        #if game_state==''