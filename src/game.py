from player import Player
from interactions import *

def Game():
  Eleve=Player(20, "../res/Eleve_Pose1.png",(1080,580))
  Prof=Player(2000, "../res/Prof_Perso1_position1.png",(100,580))
  while True:
    Eleve.move()
    Prof.move()
    collision(Eleve,Prof)
    attack(Eleve,Prof)
