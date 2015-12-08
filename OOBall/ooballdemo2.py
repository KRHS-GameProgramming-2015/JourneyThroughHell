import sys, pygame, math, random
from Ball import *
pygame.init()

clock = pygame.time.Clock()

width = 1200 
height = 700
size = width, height

bgColor = r,g,b = 200, 0, 200

screen = pygame.display.set_mode(size)

balls = []
ballTimer = 0
ballTimerMax = 3 * 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    ballTimer += 1
    if ballTimer >= ballTimerMax:
        ballTimer = 0
        ballSpeed = [random.randint(-5, 5),
                     random.randint(-5, 5)]
        ballPos = [random.randint(100, width-100),
                     random.randint(100, height-100)]
        balls += [Ball("ball.png",ballSpeed,ballPos)]
    
    for ball in balls:
        ball.move()
        ball.collideScreen(size)
    
    for first in balls:
        for second in balls:
            if first != second:
                first.collideBall(second)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    clock.tick(60)










