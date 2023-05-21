#### attributs: pv ; pvmax
#### methodes: moove ; attack ; collision
from .interactions import *
import pygame

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, pvmax, image, position, name):  # position tuple (x,y)
        super().__init__()
        self.name = name
        self.pvs = [pvmax, pvmax]  # (pv , pvmax)
        self.img = pygame.image.load(image).convert_alpha()
        self.img = pygame.transform.scale(self.img, (200, 200))
        self.rect = self.img.get_rect()  # les dimensions de l'image
        self.rect.x = position[0]
        self.rect.y = position[1]

    def move(self, Prof, Eleve, dt):
        key_input = pygame.key.get_pressed()
        if self.pvs[1] == 2000:
            if key_input[pygame.K_z]:
                self.rect.y -= 2 * dt
            elif key_input[pygame.K_d]:
                if not collision(Prof, Eleve):
                    self.rect.x += 1 * dt
            elif key_input[pygame.K_q]:
                self.rect.x -= 1 * dt
        else:
            if key_input[pygame.K_o]:
                self.rect.y -= 2 * dt
            elif key_input[pygame.K_m]:
                self.rect.x += 1 * dt
            elif key_input[pygame.K_k]:
                if not collision(Prof, Eleve):
                    self.rect.x -= 1 * dt

    def draw_player(self, scrn):
        scrn.blit(self.img, (self.rect.x, self.rect.y))
