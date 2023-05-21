import pygame
from random import randint

pygame.init()


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


def attack(Eleve, Prof, event):
    if event.key == pygame.K_LSHIFT:
        if (
            abs(Prof.rect.x - Eleve.rect.x) <= 120
            and abs(Prof.rect.y - Eleve.rect.y) <= 60
        ):
            if Eleve.pvs[0] - attack_random() >= 0:
                Eleve.pvs[0] -= attack_random()
    if event.key == pygame.K_RSHIFT:
        if (
            abs(Prof.rect.x - Eleve.rect.x) <= 120
            and abs(Prof.rect.y - Eleve.rect.y) <= 60
        ):
            if Prof.pvs[0] - attack_random() >= 0:
                Prof.pvs[0] -= attack_random() * 100
            else:
                Prof.pvs[0] = 0
    return 0
