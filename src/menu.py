import pygame
pygame.init()
# color 
color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100)

# fonts
smallFont = pygame.font.SysFont('Arial', 38)
quit_text = smallFont.render('quit', True, color)
play_text = smallFont.render('play', True, color)

def draw_main_menu(screen, mouse, width, height):
    if (width/2)-38 <= mouse[0] <= (width/2)+38 and (height/2) - 20 <= mouse[1] <= (height/2) + 20: 
        pygame.draw.rect(screen,color_light,[(width/2)-38,height/2,140,40])      
    else: 
        pygame.draw.rect(screen,color_dark,[(width/2)-38,(height/2),140,40])
        
    if (width/2)-38 <= mouse[0] <= (width/2)+38 and 300 - 20 <= mouse[1] <= 300 + 20: 
        pygame.draw.rect(screen,color_light,[(width/2)-38,300,140,40])      
    else: 
        pygame.draw.rect(screen,color_dark,[(width/2)-38,300,140,40])
        
    # superimposing the text onto our button 
    screen.blit(quit_text , (width/2,height/2))
    screen.blit(play_text, (width/2, 300))

def handle_main_menu(event, width, height, mouse):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (width / 2) - 38 <= mouse[0] <= (width/2)+38 and (height/ 2) - 20 <= mouse[1] <= (height/ 2) + 20:
            return 'quit'
        if (width/2)-38 <= mouse[0] <= (width/2)+38 and 300 - 20 <= mouse[1] <= 300 + 20:
            return 'play'
