import sys, pygame, math, random
pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("Backgrounds/Room1.png")
bgRect = bgImage.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
            
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    pygame.display.flip()
    clock.tick(60)
