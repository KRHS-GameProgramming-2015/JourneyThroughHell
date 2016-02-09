import sys, pygame, math, random
from Player import *
from Zombie import *
from Boss import *
pygame.init()

clock = pygame.time.Clock()

width = 1200 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

while True:
    zombies = []
    zombieTimer = 0
    zombieTimerMax = .75 * 60
    zombiesSpawned = 0
    zombieLimit = 5

    bosses = []
    bossTimer = 0
    bossTimerMax = 75 * 100
    bossesSpawned = 0
    bossLimit = 1

    bgImage = pygame.image.load("Backgrounds/Room4.png")
    bgRect = bgImage.get_rect()

    player = Player([width/2, height/2])

    win = False
    while not win:
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
        if zombieTimer >= zombieTimerMax and zombiesSpawned < zombieLimit:
            zombieTimer = 0
            zombiesSpawned += 1
            zombiePos = [random.randint(100, width-100),
                         random.randint(100, height-100)]
            zombies += [Zombie(["Enemies/Zombie1.png",
                            "Enemies/Zombie2.png"],
                           zombiePos)]
        if zombiesSpawned >= zombieLimit and len(zombies) == 0 and bossesSpawned < bossLimit:
            bossesSpawned += 1
            bossPos = [random.randint(100, width-100),
                         random.randint(100, height-100)]
            bosses += [Boss(["Bosses/R1Boss1.png",
                            "Bosses/R1Boss2.png"],
                           bossPos)]
        player.update(size)

        for zombie in zombies:
            zombie.collidePlayer(player)
            zombie.update(size)
            if not zombie.living:
                zombies.remove(zombie) 

        for boss in bosses:
            boss.collidePlayer(player)
            boss.update(size)
            if not boss.living:
                bosses.remove(boss)
                win = True
                

        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(player.image, player.rect)
        for zombie in zombies:
            screen.blit(zombie.image, zombie.rect)
        for boss in bosses:
            screen.blit(boss.image, boss.rect)
        pygame.display.flip()
        clock.tick(60)
        
        
    bg = pygame.image.load("Backgrounds/YOUWIN.png")
    bgrect = bg.get_rect()
    
    bgImage = pygame.image.load("Backgrounds/YOUWIN.png")
    bgRect = bgImage.get_rect()
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
