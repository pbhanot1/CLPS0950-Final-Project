#testing how to use pygame gui
import pygame, sys
import pygame_gui
import gameboard

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((1200, 900))
screen = pygame.display.set_mode((1200, 900))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((800, 600))

first_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Pop Up Here',manager=manager,
                                            anchors={'left': 'left',
                                            'right': 'right',
                                            'top': 'top',
                                            'bottom': 'bottom'})

clock = pygame.time.Clock()
is_running = True

while is_running:
     time_delta = clock.tick(60)/1000.0
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             is_running = False
         if event.type == pygame_gui.UI_BUTTON_PRESSED:
             if event.ui_element == first_button:
                 gameboard.main()

         manager.process_events(event)

     manager.update(time_delta)

     window_surface.blit(background, (0, 0))
     manager.draw_ui(window_surface)

     pygame.display.update()