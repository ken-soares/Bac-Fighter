#### attributs: pv ; pvmax
#### methodes: moove ; attack ; collision

import pygame 
from pygame.locals import K_UP,K_RIGHT,K_LEFT,K_z,K_q,K_d,K_RSHIFT,K_LSHIFT
from random import *

pygame.init()

class Player(pygame.sprite.Sprite):

  def __init__(self,pvmax,image, position): # position tuple (x,y)
    super().__init__()
    self.pvs = (pvmax,pvmax) # (pv , pvmax)
    self.rect = self.image.get_rect() # les dimensions de l'image
    self.rect.x = position[0]
    self.rect.y = position[1]
    self.image = image
    

  def move(self):
    if self.pvs[1]==2000:
      if pygame.event.key==K_z:
        self.rect.y-=25
      elif pygame.event.key==K_d:
        self.rect.x+=10
      elif pygame.event.key==K_q:
        self.rect.x-=10
    else:
      if pygame.event.key==K_UP:
        self.rect.y-=25
      elif pygame.event.key==K_RIGHT:
        self.rect.x+=10
      elif pygame.event.key==K_LEFT:
        self.rect.x-=10

  def draw_player(self,scrn):
    scrn.blit(self.image,(self.rect.x,self.rect.y)) 
