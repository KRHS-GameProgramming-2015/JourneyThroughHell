import sys, pygame, math
from Ball import *
pygame.init()

clock = pygame.time.Clock()

width = 900 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

ball1 = Ball("ball1.png", [4, 6])
ball2 = Ball("ball2.png", [2, 6], [200, 200])
ball3 = Ball("ball1.png", [6, 5], [400, 0])
ball4 = Ball("ball.png", [3, 6], [600, 0])
ball5 = Ball("ball1 .png", [4, 6], [800, 800])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    ball1.move()
    ball1.collideScreen(size)
    
    ball2.move()
    ball2.collideScreen(size)
    
    ball3.move()
    ball3.collideScreen(size)
    
    ball4.move()
    ball4.collideScreen(size)
    
    ball5.move()
    ball5.collideScreen(size)
    
    ball1.collideBall(ball2)
    ball1.collideBall(ball3)
    ball1.collideBall(ball4)
    ball1.collideBall(ball5)
    
    ball2.collideBall(ball1)
    ball2.collideBall(ball3)
    ball2.collideBall(ball4)
    ball1.collideBall(ball5)
    
    ball3.collideBall(ball1)
    ball3.collideBall(ball2)
    ball3.collideBall(ball4)
    ball1.collideBall(ball5)
    
    ball4.collideBall(ball1)
    ball4.collideBall(ball2)
    ball4.collideBall(ball3)
    ball4.collideBall(ball5)
    
    ball5.collideBall(ball1)
    ball5.collideBall(ball2)
    ball5.collideBall(ball3)
    ball5.collideBall(ball4)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(ball1.image, ball1.rect)
    screen.blit(ball2.image, ball2.rect)
    screen.blit(ball3.image, ball3.rect)
    screen.blit(ball4.image, ball4.rect)
    screen.blit(ball5.image, ball5.rect)
    pygame.display.flip()
    clock.tick(60)










