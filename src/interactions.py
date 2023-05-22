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
    if event.key == pygame.K_LSHIFT:
        Prof.set_img("res/Prof_Perso1_position2.png")
        if (
            abs(Prof.rect.x - Eleve.rect.x) <= 120
            and abs(Prof.rect.y - Eleve.rect.y) <= 60
        ):
            if Eleve.pvs[0] - attack_random() >= 0:
                pain = attack_random()
                Eleve.pvs[0] -= pain
                eleve_hurt = font.render(f"-{pain} points!", True, (255,0,0))
                eleve_subtext = font.render("It's not a sin() curve, it's a pair of boobs!", True, (255,0,0))
                display_rng = randint(1,11)
                screen.blit(eleve_hurt, (30,30))
                if display_rng in [1,2,3]:
                    screen.blit(eleve_subtext, (30, 60))
                pygame.display.flip()
                Prof.set_img("res/Prof_Perso1_position1.png")
            else:
                Eleve.pvs[0] = 0
    else:
        Prof.set_img("res/Prof_Perso1_position1.png")
        
    if event.key == pygame.K_RSHIFT:
        Eleve.set_img("res/Eleve_Pose3.png")
        if (
            abs(Prof.rect.x - Eleve.rect.x) <= 120
            and abs(Prof.rect.y - Eleve.rect.y) <= 60
        ):
            if Prof.pvs[0] - attack_random() >= 0: 
                pain = attack_random() * 100
                Prof.pvs[0] -= pain
                prof_hurt = font.render(f"-{pain}€!", True, (255,0,0))
                prof_subtext = font.render("It's not pedagogy, it's somnifere!", True, (255,0,0))
                display_rng = randint(1,11)
                screen.blit(prof_hurt, (900, 30))
                if display_rng in [1,2,3]:
                    screen.blit(prof_subtext, (900,60))
                pygame.display.flip()
                Prof.set_img("res/Prof_Perso1_position1.png")
            else:
                Prof.pvs[0] = 0
    else:
        Eleve.set_img("res/Eleve_Pose1.png")
    return 0
