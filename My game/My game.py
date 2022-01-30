from email.headerregistry import Group
from turtle import width
import pygame
from pygame.locals import *
import sys

from Ground import Ground
from Player import Player

#תחילת pygame
pygame.init()

width = 800
height = 400
FPS = 60
CLOCK = pygame.time.Clock()

display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Monster Killer")

#רקע
background = pygame.image.load('C:/Users/salav/Downloads/My game/night.png')

#אדמה
ground = Ground(900, 120, 0, 0, 'C:/Users/salav/Downloads/My game/ground1.png')

#שחקן
player = Player(200, 200)

GroundGroup = pygame.sprite.Group()
GroundGroup.add(ground)


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            pass
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.jump()

    player.move()


    
   
    display.blit(background,(0,0))
    ground.render(display)
    player.render(display)
    


    pygame.display.update()
    CLOCK.tick(FPS)
