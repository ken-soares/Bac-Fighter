import pygame
from .game import *

pygame.init()
# color
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

# fonts
smallFont = pygame.font.SysFont("Arial", 38)
bigFont = pygame.font.SysFont("Arial", 45)
quit_text = smallFont.render("quit", True, color)
credits_text = smallFont.render("credits", True, color)
play_text = smallFont.render("play", True, color)
bac_fighter_text = bigFont.render("Bac-Fighter", True, color)
mumu_inc = smallFont.render("A game by MuMu Inc.", True, color_dark)


def draw_main_menu(screen, mouse, width, height):
    if (width / 2) - 38 <= mouse[0] <= (width / 2) + 100 and (height / 2) - 20 <= mouse[
        1
    ] <= (height / 2) + 50:
        pygame.draw.rect(screen, color_light, [(width / 2) - 38, height / 2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [(width / 2) - 38, (height / 2), 140, 40])

    if (width / 2) - 38 <= mouse[0] <= (width / 2) + 100 and 300 - 20 <= mouse[
        1
    ] <= 300 + 50:
        pygame.draw.rect(screen, color_light, [(width / 2) - 38, 300, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [(width / 2) - 38, 300, 140, 40])
    if (width / 2) -38 <= mouse[0] <= (width / 2) +100 and 420-20 <=mouse[1]<= 420+50:
        pygame.draw.rect(screen, color_light, [(width / 2) - 38, 420, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [(width / 2) - 38, 420, 140, 40])
    # superimposing the text onto our button
    screen.blit(bac_fighter_text, ((width - 140) / 2, height / 4))
    screen.blit(mumu_inc, ((width - 370, height - 40)))
    screen.blit(quit_text, (width / 2, height / 2))
    screen.blit(play_text, (width / 2, 300))
    screen.blit(credits_text,(width/2-15,420))


def handle_main_menu(event, width, height, mouse):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (width / 2) - 38 <= mouse[0] <= (width / 2) + 100 and (
            height / 2) - 20 <= mouse[1] <= (height / 2) + 50:
            return "quit"
        if (width / 2) - 38 <= mouse[0] <= (width / 2) + 100 and 300 - 20 <= mouse[
            1
        ] <= 300 + 50:
            return "play"
        if (width / 2) -38 <= mouse[0] <= (width / 2) +100 and 420-20 <=mouse[1]<= 420+50:
            return "credits"
            
credits_contenu = smallFont.render("With the support of : TOURNIER Thibaut as Coach <3", True, color_light)
credits_contenu1 = smallFont.render("A game by MuMu Inc.", True, color_light)
credits_contenu2 = smallFont.render("With:", True, color_light)
credits_contenu3 = smallFont.render("SOARES Kenneth as Project Manager", True, color_light)
credits_contenu4 = smallFont.render("RENAULT Gabriel as Emotional Support Manager", True, color_light)
credits_contenu5 = smallFont.render("PULIERO Mélusine as Project Deputy", True, color_light)
credits_contenu6 = smallFont.render("MENARD Damien as Physics Manager", True, color_light)
credits_contenu7 = smallFont.render("JARROUX Océane as Graphics Designer", True, color_light)

def handle_credits_menu(screen):
    print("dans la fonction")
    screen.fill((0,0,0))
    screen.blit(credits_contenu1,(500,100))
    screen.blit(credits_contenu2,(600,175))
    screen.blit(credits_contenu3,(360,250))
    screen.blit(credits_contenu4,(300,325))
    screen.blit(credits_contenu5,(370,400))
    screen.blit(credits_contenu6,(370,475))
    screen.blit(credits_contenu7,(365,550))
    screen.blit(credits_contenu,(500,670))
    pygame.display.flip()
    pygame.time.wait(12000)


def handle_game_over(winner, screen):
    winner_text = smallFont.render(f"{winner} won!", True, color)
    return_text = smallFont.render("Press ESC to quit", True, color)
    restart_text = smallFont.render("Press ENTER to play again", True, color)
    screen.blit(winner_text, (250, 150))
    screen.blit(return_text, (250, 220))
    screen.blit(restart_text, (250, 260))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit(0)
                if event.key == pygame.K_RETURN:
                    Game(screen)
