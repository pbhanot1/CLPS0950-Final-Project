#testing how to use pygame gui
import pygame, sys
import pygame_gui
import gameboard
import Tokens
from pygame_gui.elements import UIButton

pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Game with Pop-up")
clock = pygame.time.Clock()

ui_manager = pygame_gui.UIManager(screen_size)
#button = UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Click to Talk', manager=ui_manager)

confirmation_dialog = pygame_gui.windows.UIConfirmationDialog(
    rect=pygame.Rect((275, 200), (250, 150)),
    manager=ui_manager,
    window_title='Confirmation',
    action_long_desc='I need 3 treats to be your friend.',
    action_short_name='OK',
    blocking=False)

is_running = True
while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        ui_manager.process_events(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                confirmation_dialog.kill()
                #if event.ui_element == button:
                #    confirmation_dialog.kill()

    ui_manager.update(time_delta)
    screen.fill((255, 255, 255))  # Fill the screen with white color

    ui_manager.draw_ui(screen)
    pygame.display.update()

#first_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                       #     text='Pop Up Here',manager=manager,
                                         #   anchors={'left': 'left',
                                        #    'right': 'right',
                                        #    'top': 'top',
                                       #     'bottom': 'bottom'})

#clock = pygame.time.Clock()
#is_running = True

#while is_running:
  #   time_delta = clock.tick(60)/1000.0
  #   for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
  #           is_running = False
  #       if event.type == pygame_gui.UI_BUTTON_PRESSED:
   #          if event.ui_element == first_button:
 #                gameboard.main()

   #      manager.process_events(event)

 #    manager.update(time_delta)

   #  window_surface.blit(background, (0, 0))
 #    manager.draw_ui(window_surface)

  #   pygame.display.update()