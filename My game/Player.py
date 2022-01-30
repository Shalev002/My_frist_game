from sys import base_exec_prefix
import pygame
from pygame.locals import *


vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.dy = 0

        self.image = pygame.image.load('C:/Users/salav/Downloads/My game/IMGES/idle player/player/0.png')    
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        self.pos = vec(x, y)
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)

        self.ACC = 0.4
        self.FRIC = -0.1
        self.jumping = False
        self.running = False


    def move(self):

        self.acc = vec(0, 0.5)

        keys = pygame.key.get_pressed()

        if keys[K_a]:
            self.acc.x = -self.ACC
        if keys[K_d]:
            self.acc.x = self.ACC


        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.topleft = self.pos



    def grounnd(self):
        if self.rect.bottom + self.dy > 400:
            self.dy = 400 - self.rect.bottom
            self.in_air = False


    def jump(self):
        self.vel.y = -15

    def render(self, display):
        display.blit(self.image, self.pos)
        

