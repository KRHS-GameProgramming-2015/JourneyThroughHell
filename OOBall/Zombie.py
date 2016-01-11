import sys, pygame, math, random
pygame.init()

class Zombie():
    def __init__(self, images, pos = [0,0]):
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.maxSpeedx = 5
        self.maxSpeedy = 5

ballTimer += 1
    if ballTimer >= ballTimerMax:
        ballTimer = 0
        ballSpeed = [random.randint(-5, 5),
                     random.randint(-5, 5)]
        ballPos = [random.randint(100, width-100),
                     random.randint(100, height-100)]
        balls += [Ball(["zombie1.png",
                        "zombie2.png"],
                       ballSpeed,
                       ballPos)]
