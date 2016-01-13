import sys, pygame, math, random
pygame.init()

class Zombie():
    def __init__(self, images, pos = [0,0]):
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.maxSpeedx = 5
        self.maxSpeedy = 5
        
        self.images = []
        for image in images:
            self.images += [pygame.image.load(image)]
        
        self.frame = 0
        self.maxFrame = len(self.images)
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)

