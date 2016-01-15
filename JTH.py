import sys, pygame, math, random
from Player import *
from Zombie import *
pygame.init()

clock = pygame.time.Clock()

width = 1200 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

zombies = []
zombieTimer = 0
zombieTimerMax = .75 * 60
zombieLimit = 5

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
            elif event.key == pygame.K_a:
                player.go("stop attack")

    zombieTimer += 1
    if zombieTimer >= zombieTimerMax:
        zombieTimer = 0
        if len(zombies) < zombieLimit:
            zombiePos = [random.randint(100, width-100),
                         random.randint(100, height-100)]
            zombies += [Zombie(["Enemies/Zombie1.png",
                            "Enemies/Zombie2.png"],
                           zombiePos)]

    player.update()

    for zombie in zombies:
        zombie.collidePlayer(player)
        zombie.update(size)
        if not zombie.living:
            zombies.remove(zombie) 

    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    screen.blit(player.image, player.rect)
    for zombie in zombies:
        screen.blit(zombie.image, zombie.rect)
    pygame.display.flip()
    clock.tick(60)
