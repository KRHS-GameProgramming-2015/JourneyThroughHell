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

player = Player([width/2, height/2])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            elif event.key == pygame.K_DOWN:
                player.go("down")
            elif event.key == pygame.K_LEFT:
                player.go("left")
            elif event.key == pygame.K_RIGHT:
                player.go("right")
            elif event.key == pygame.K_a:
                player.go("attack")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            elif event.key == pygame.K_DOWN:
                player.go("stop down")
            elif event.key == pygame.K_LEFT:
                player.go("stop left")
            elif event.key == pygame.K_RIGHT:
                player.go("stop right")

    player.update()

    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
