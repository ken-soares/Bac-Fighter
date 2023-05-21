import pygame

pygame.init()
# color
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

# fonts
smallFont = pygame.font.SysFont("Arial", 38)
bigFont = pygame.font.SysFont("Arial", 45)
quit_text = smallFont.render("quit", True, color)
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

    # superimposing the text onto our button
    screen.blit(bac_fighter_text, ((width - 140) / 2, height / 4))
    screen.blit(mumu_inc, ((width - 370, height - 40)))
    screen.blit(quit_text, (width / 2, height / 2))
    screen.blit(play_text, (width / 2, 300))


def handle_main_menu(event, width, height, mouse):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (width / 2) - 38 <= mouse[0] <= (width / 2) + 100 and (
            height / 2
        ) - 20 <= mouse[1] <= (height / 2) + 50:
            return "quit"
        if (width / 2) - 38 <= mouse[0] <= (width / 2) + 100 and 300 - 20 <= mouse[
            1
        ] <= 300 + 50:
            return "play"


def handle_game_over(winner, screen):
    winner_text = smallFont.render(f"{winner} won!", True, color)
    return_text = smallFont.render(f"Press ESC to quit", True, color)
    screen.blit(winner_text, (250, 180))
    screen.blit(return_text, (250, 240))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
