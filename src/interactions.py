import pygame 
from pygame.locals import K_UP,K_RIGHT,K_LEFT,K_z,K_q,K_d,K_RSHIFT,K_LSHIFT
from random import *

pygame.init()

def collision(Eleve, Prof):
    if Prof.rect.x>Eleve.rect.x:
      return False
    elif Eleve.rect.x<Prof.rect.x:
      return False
    else:
      return True

def attack_random():
  coup = 0
  chiffre = randint(1,1001)
  if chiffre <= 600:
    coup = 1
  elif chiffre <= 850:
    coup = 2
  elif chiffre <= 950:
    coup = 3
  elif chiffre <= 1000:
    coup = 4
  return coup
  
  
def attack(Eleve, Prof):
  if pygame.event.key == K_LSHIFT:
    if abs(Prof.rect.x - Eleve.rect.x) < 80 and abs(Prof.rect.y - Eleve.rect.y)< 20:
      Eleve.pvs[0] -= attack_random()
  if pygame.event.key == K_RSHIFT:
    if abs(Prof.rect.x - Eleve.rect.x) < 80 and abs(Prof.rect.y - Eleve.rect.y)< 20:
      Prof.pvs[0] -= attack_random()*100
  return 1