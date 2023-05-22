import pygame
from src.menu import *
from src.game import *

pygame.mixer.init()
pygame.mixer.music.load("res/musique2.mp3")

pygame.init()

res = (1280, 720)
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()
background = pygame.image.load("res/decoration-salle-de-classe1280x720.jpg")
pygame.display.set_caption("bac fighter")

menuRunning = True

pygame.mixer.music.stop()
pygame.mixer.music.play()

while menuRunning:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        menuEvent = handle_main_menu(event, width, height, mouse)
        if menuEvent == "quit":
            quit(0)
        if menuEvent == "play":
            menuRunning = False
        if menuEvent=="credits":
            handle_credits_menu(screen)

    # stores the (x,y) coordinates into
    # the variable as a tuple
    screen.blit(background, background.get_rect())
    draw_main_menu(screen, mouse, width, height)

    # updates the frames of the game
    pygame.display.update()


winner = Game(screen)
screen.blit(background, background.get_rect())
handle_game_over(winner, screen)



pygame.quit()
quit(0)
