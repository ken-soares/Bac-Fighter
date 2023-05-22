from .player import Player
from .interactions import *
import pygame
import time

background = pygame.image.load("res/decoration-salle-de-classe1280x720.jpg")

font = pygame.font.SysFont("Arial", 25)


def Game(screen):
    Eleve = Player(20, "res/Eleve_Pose1.png", (1030, 470), "Eleve")
    Prof = Player(2000, "res/Prof_Perso1_position1.png", (50, 470), "Prof")

    while True:
        if Eleve.pvs[0] <= 0:
            playerHP = font.render(f"Grade:0/{Eleve.pvs[1]}", True, (50, 50, 50))
        else:
            playerHP = font.render(
                f"Grade:{Eleve.pvs[0]}/{Eleve.pvs[1]}", True, (50, 50, 50)
            )
        if Prof.pvs[0] <= 0:
            profHP = font.render(f"Salary:0/{Prof.pvs[1]}", True, (50, 50, 50))
        else:
            profHP = font.render(
                f"Salary:{Prof.pvs[0]}/{Prof.pvs[1]}", True, (50, 50, 50)
            )

        # utile pour les déplacements
        clock = pygame.time.Clock()

        screen.blit(background, background.get_rect())
        screen.blit(profHP, (30, 10))
        screen.blit(playerHP, (1120, 10))
        Eleve.draw_player(screen)
        Prof.draw_player(screen)
        pygame.display.flip()

        Eleve.move(Prof, Eleve)
        Prof.move(Prof, Eleve)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                attack(Eleve, Prof, event, screen)
                if event.key == pygame.K_ESCAPE:
                    quit(0)
        if Prof.pvs[0] <= 0 and Eleve.pvs[0] != 0:
            return "Student"
        elif Prof.pvs[0] != 0 and Eleve.pvs[0] <= 0:
            return "Prof"

        clock.tick(60)
