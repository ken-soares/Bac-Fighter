import pygame
from src.menu import *

pygame.init()

res = (1280,720)
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()
pygame.display.set_caption('bac fighter')
  
menuRunning = True
clock = pygame.time.Clock()

    
while menuRunning:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuRunning = False
        menuEvent = handle_main_menu(event, width, height, mouse)
        if menuEvent == "quit":
            pygame.quit()
        if menuEvent == 'play':
            menuRunning = False

    clock.tick(60)
        # fills the screen with a color 
    screen.fill((0,0,0))
      
    # stores the (x,y) coordinates into
    # the variable as a tuple

    draw_main_menu(screen, mouse, width, height)


      
    # updates the frames of the game 
    pygame.display.update()
    
pygame.quit()
