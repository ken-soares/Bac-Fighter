from .player import Player
from .interactions import *
import pygame

background = pygame.image.load("res/decoration-salle-de-classe1280x720.jpg")

def Game(screen):
  Eleve=Player(20, "res/Eleve_Pose1.png",(1030,470),"Eleve")
  Prof=Player(2000, "res/Prof_Perso1_position1.png",(50,470),"Prof")

  while True:
    screen.blit(background, background.get_rect())
    Eleve.draw_player(screen)
    Prof.draw_player(screen)
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        Eleve.move(event,Prof,Eleve)
        Prof.move(event,Prof,Eleve)
        attack(Eleve,Prof, event)
        if event.key == pygame.K_ESCAPE:
          quit(0)
