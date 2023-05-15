import pygame
from src.menu import *
from game import *

pygame.init()

res = (1281, 720)
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()
background = pygame.image.load("res/decoration-salle-de-classe1280x720.jpg")
pygame.display.set_caption("bac fighter")

menuRunning = True
clock = pygame.time.Clock()

while menuRunning:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuRunning = False
        menuEvent = handle_main_menu(event, width, height, mouse)
        if menuEvent == "quit":
            quit(1)
        if menuEvent == "play":
            menuRunning = False

    clock.tick(60)

    # stores the (x,y) coordinates into
    # the variable as a tuple
    screen.blit(background, background.get_rect())
    draw_main_menu(screen, mouse, width, height)

    # updates the frames of the game
    pygame.display.update()
game()   
pygame.quit()
