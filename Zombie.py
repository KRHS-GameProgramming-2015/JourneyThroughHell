import sys, pygame, math, random
pygame.init()

class Zombie():
    def __init__(self, images, pos = [0,0]):
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.maxSpeedx = 5
        self.maxSpeedy = 5

