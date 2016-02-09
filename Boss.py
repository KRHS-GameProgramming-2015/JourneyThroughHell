import sys, pygame, math, random
pygame.init()

class Boss():
    def __init__(self, images, pos = [0,0]):
        self.speedx = 5
        self.speedy = 5
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
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.invincible = False
        self.invincibleTimer = 0
        self.invincibleTimerMax = 2*60
        
        self.living = True 
        self.hp = 10
        
    def update(self, size):
        self.collideScreen(size)
        self.move()
        self.animate()
        if self.invincible:
            self.invincibleTimer += 1
            if self.invincibleTimer >= self.invincibleTimerMax:
                self.invincible = False
                self.invincibleTimer = 0
                    
    def animate(self):
        if self.speed == [0,0]:
            self.frame = 0
        else:
            self.frame = 1
        self.image = self.images[self.frame]
        
    def move(self):
        if random.randint(1,10) == 1:
            if self.speed == [0,0]:
                self.speedx = self.oldspeedx
                self.speedy = self.oldspeedy
            else:
                self.oldspeedx = self.speedx
                self.oldspeedy = self.speedy
                self.speedx = 0
                self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.didBounceX = False
        self.didBounceY = False
        

    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                self.move()
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                selfdidBounceY = True
                self.move()
     
    def collidePlayer(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if other.action=="attacking" and not self.invincible:
                    self.hp -= 1
                    self.invincible = True
                    print self.hp
                if self.hp <= 0:
                    self.living = False
                    
        
    def collideBoss(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceTo(other.rect.center):
                    if not self.didBounceX:
                        if ((self.rect.center[0] < other.rect.center[0] and self.speedx > 0) or
                            (self.rect.center[0] > other.rect.center[0] and self.speedx < 0)):
                            self.speedx = -self.speedx
                            self.didBounceX = True
                            self.move()
                    if not self.didBounceY:
                        if ((self.rect.center[1] < other.rect.center[1] and self.speedy > 0) or
                            (self.rect.center[1] > other.rect.center[1] and self.speedy < 0)):
                            self.speedy = -self.speedy
                            self.didBounceY = True
                            self.move()
                    
        
    def distanceTo(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
