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

        self.jump_height = 20
        self.velocity = self.jump_height
        self.jumping = False

    def move(self, Prof, Eleve):
        key_input = pygame.key.get_pressed()

        gravity = 1

        if self.pvs[1] == 2000:
            if key_input[pygame.K_z]:
                self.jumping = True
            if key_input[pygame.K_d]:
                if not collision(Prof, Eleve):
                    self.rect.x += 10
            if key_input[pygame.K_q]:
                self.rect.x -= 10
        else:
            if key_input[pygame.K_o]:
                self.jumping = True
            elif key_input[pygame.K_m]:
                self.rect.x += 10
            elif key_input[pygame.K_k]:
                if not collision(Prof, Eleve):
                    self.rect.x -= 10

        if self.jumping:
            self.rect.y -= self.velocity
            self.velocity -= gravity
            if self.velocity < -self.jump_height:
                self.jumping = False
                self.velocity = self.jump_height

    def draw_player(self, scrn):
        scrn.blit(self.img, (self.rect.x, self.rect.y))
