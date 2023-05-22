import pygame
import time
from random import randint

pygame.init()
font = pygame.font.SysFont("Arial", 28)


def collision(Eleve, Prof):
    if abs(Prof.rect.x - Eleve.rect.x) <= 100:
        return True
    else:
        return False


def attack_random():
    coup = 0
    chiffre = randint(1, 1001)
    if chiffre <= 600:
        coup = 1
    elif chiffre <= 850:
        coup = 2
    elif chiffre <= 950:
        coup = 3
    elif chiffre <= 1000:
        coup = 4
    return coup


def attack(Eleve, Prof, event, screen):
    if event.key == pygame.K_LCTRL:
        Prof.set_img("res/Prof_Perso1_position2.png")
        if (
            abs(Prof.rect.x - Eleve.rect.x) <= 120
            and abs(Prof.rect.y - Eleve.rect.y) <= 60
        ):
            if Eleve.pvs[0] - attack_random() >= 0:
                pain = attack_random()
                Eleve.pvs[0] -= pain
                if Eleve.rect.x + 100 <= 1100:  
                    Eleve.rect.x += 100
                else:
                    Eleve.rect.x = 1100
                Prof.set_img("res/Prof_Perso1_position1.png")
            else:
                Eleve.pvs[0] = 0
    else:
        Prof.set_img("res/Prof_Perso1_position1.png")
        
    if event.key == pygame.K_RCTRL:
        Eleve.set_img("res/Eleve_Pose3.png")
        if (
            abs(Prof.rect.x - Eleve.rect.x) <= 120
            and abs(Prof.rect.y - Eleve.rect.y) <= 60
        ):
            if Prof.pvs[0] - attack_random() >= 0: 
                pain = attack_random() * 100
                Prof.pvs[0] -= pain
                
                if Prof.rect.x - 100 >= 30:
                    Prof.rect.x -= 100
                else:
                    Prof.rect.x = 30
                    
                Prof.set_img("res/Prof_Perso1_position1.png")
            else:
                Prof.pvs[0] = 0
    else:
        Eleve.set_img("res/Eleve_Pose1.png")
    return 0
    
def attack_dist(Eleve, Prof, event, screen):
    if event.key == pygame.K_a:
        Prof.set_img("res/Prof_Perso2_position1.png")
        if (
            abs(Prof.rect.x - Eleve.rect.x) <= 180
            and abs(Prof.rect.y - Eleve.rect.y) <= 60
        ):
            if Eleve.pvs[0] - attack_random() >= 0:
                pain = attack_random()
                Eleve.pvs[0] -= pain
                if Eleve.rect.x + 300 <= 1100:  
                    Eleve.rect.x += 300
                else:
                    Eleve.rect.x = 1100
                Prof.set_img("res/Prof_Perso1_position1.png")
            else:
                Eleve.pvs[0] = 0
    else:
        Prof.set_img("res/Prof_Perso1_position1.png")
        
    if event.key == pygame.K_p:
        Eleve.set_img("res/Eleve_Perso2_Pose1.png")
        if (
            abs(Prof.rect.x - Eleve.rect.x) <= 180
            and abs(Prof.rect.y - Eleve.rect.y) <= 60
        ):
            if Prof.pvs[0] - attack_random() >= 0: 
                pain = attack_random() * 100
                Prof.pvs[0] -= pain
                
                if Prof.rect.x - 300 >= 30:
                    Prof.rect.x -= 300
                else:
                    Prof.rect.x = 30
                    
                Prof.set_img("res/Prof_Perso1_position1.png")
            else:
                Prof.pvs[0] = 0
    else:
        Eleve.set_img("res/Eleve_Pose1.png")
    return 0
