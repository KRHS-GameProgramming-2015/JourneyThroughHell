import sys, pygame, math, random
from Player import *
pygame.init()

clock = pygame.time.Clock()

width = 1200 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("Backgrounds/Room1.png")
bgRect = bgImage.get_rect()

player = Player("knife", [width/2, height/2])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
            
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
