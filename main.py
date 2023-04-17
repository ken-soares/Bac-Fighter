import pygame

pygame.init()

res = (1280,720)
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()
pygame.display.set_caption('bac fighter')
  
# color 
color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100)

smallFont = pygame.font.SysFont('Arial', 38)
text = smallFont.render('quit', True, color)
  
running = True
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width / 2 <= mouse[0] <= width/2 +140 and height / 2 <= mouse[1] <= height/2+40:
                pygame.quit()
    pygame.display.flip()
    clock.tick(60)
        # fills the screen with a color 
    screen.fill((0,0,0)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
      
    # superimposing the text onto our button 
    screen.blit(text , (width/2+50,height/2)) 
      
    # updates the frames of the game 
    pygame.display.update()
    
pygame.quit()
