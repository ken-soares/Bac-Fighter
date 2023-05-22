from .player import Player
from .interactions import *
import pygame
import time

background = pygame.image.load("res/decoration-salle-de-classe1280x720.jpg")

font = pygame.font.SysFont("Arial", 25)


def Game(screen):
    pygame.mixer.Sound("res/Fight.mp3").play()
    from .menu import handle_game_over
    Eleve = Player(20, "res/Eleve_Pose1.png", (1030, 470), "Eleve")
    Prof = Player(2000, "res/Prof_Perso1_position1.png", (50, 470), "Prof")
    
    quitText = font.render("ESC to RAGEQUIT(git gud LOL)", True, (255,255,255))


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
        screen.blit(quitText, (300, 110))
        screen.blit(profHP, (30, 10))
        screen.blit(playerHP, (1120, 10))
        Eleve.draw_player(screen)
        Prof.draw_player(screen)
        pygame.display.flip()

        Eleve.move(Prof, Eleve)
        Prof.move(Prof, Eleve)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                attack_dist(Eleve, Prof, event, screen)
                attack(Eleve, Prof, event, screen)
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_F11:
                    screen = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)
        if Prof.pvs[0] <= 0 and Eleve.pvs[0] != 0:
            screen.blit(background, background.get_rect())
            handle_game_over("Student", screen)
        elif Prof.pvs[0] != 0 and Eleve.pvs[0] <= 0:
            screen.blit(background, background.get_rect())
            handle_game_over("Prof", screen)

        clock.tick(60)
