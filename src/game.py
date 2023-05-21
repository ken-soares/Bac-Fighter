from .player import Player
from .interactions import *
import pygame

background = pygame.image.load("res/decoration-salle-de-classe1280x720.jpg")

font = pygame.font.SysFont("Arial", 25)


def Game(screen):
    Eleve = Player(20, "res/Eleve_Pose1.png", (1030, 470), "Eleve")
    Prof = Player(2000, "res/Prof_Perso1_position1.png", (50, 470), "Prof")

    while True:
        playerHP = font.render(
            f"Note:{Eleve.pvs[0]}/{Eleve.pvs[1]}", True, (50, 50, 50)
        )
        profHP = font.render(f"Salaire:{Prof.pvs[0]}/{Prof.pvs[1]}", True, (50, 50, 50))
        screen.blit(background, background.get_rect())
        screen.blit(profHP, (30, 10))
        screen.blit(playerHP, (1120, 10))
        Eleve.draw_player(screen)
        Prof.draw_player(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            Eleve.move(Prof, Eleve)
            Prof.move(Prof, Eleve)
            if event.type == pygame.KEYDOWN:
                attack(Eleve, Prof, event)
                if event.key == pygame.K_ESCAPE:
                    quit(0)

                # CODE DE TEST DU MENU GAME OVER /!\ À RETIRER PLUS TARD /!\
                if event.key == pygame.K_f:
                    return "Prof"
