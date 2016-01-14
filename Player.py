import sys, pygame, math

class Player():
    def __init__(self, weapon, pos = [0,0]):
        self.speedx = 3
        self.speedy = 3
        self.speed = [self.speedx, self.speedy]
        self.maxSpeedx = 5
        self.maxSpeedy = 5
        
        self.action = "standing"
        self.weapon = weapon
        
        if self.weapon == "chain saw":
            self.standing_ChainSawImages = [pygame.image.load("Player/ChainSawStanding.png")]
            self.moving_ChainSawImages = [pygame.image.load("Player/ChainSawMove.png")]
            self.attacking_ChainSawImages = [pygame.image.load("Player/ChainSawAttack.png")]
            self.images = self.standing_ChainSawImages
        else: #assume knife
            self.standing_KnifeImages = [pygame.image.load("Player/KnifeStanding.png")]
            self.moving_KnifeImages = [pygame.image.load("Player/KnifeMoving1.png")]
            self.attacking_KnifeImages = [pygame.image.load("Player/AttackKnife.png")]
            self.images = self.standing_KnifeImages
        
        self.frame = 0
        self.maxFrame = len(self.images)-1
        self.timer = 0
        self.timerMax = .5*60 #second*60
        
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.radius = self.rect.width/2 - 2
        
        self.rect = self.rect.move(pos)
    
    def update(self):
        self.move()
        self.animate()
        
    def animate(self):
        if self.action == "moving":
            if self.weapon == "chain saw":
                self.images = self.moving_ChainSawImages
            else:
                self.images = self.moving_KnifeImages
        elif self.action == "attacking":
            if self.weapon == "chain saw":
                self.images =  self.attacking_ChainSawImages
            else:
                self.images = self.attacking_KnifeImages
        else:
            if self.weapon == "chain saw":
                self.images = self.standing_ChainSawImages
            else:
                self.images = self.standing_KnifeImages
        
        self.image = self.images[self.frame]
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.didBounceX = False
        self.didBounceY = False

    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
    def go(self, direction):
        if direction == "attack":
            self.speedx = 0
            self.speedy = 0
            self.action = "attacking"
            
        if direction == "up":
            self.speedy = -self.maxSpeedy
            self.action = "moving"
        elif direction == "down":
            self.speedy = self.maxSpeedy
            self.action = "moving"
        if direction == "right":
            self.speedx = self.maxSpeedx
            self.action = "moving"
        elif direction == "left":
            self.speedx = -self.maxSpeedx
            self.action = "moving"
        
        if direction == "stop up":
            self.action = "standing"
            self.speedy = 0
        elif direction == "stop down":
            self.action = "standing"
            self.speedy = 0
        if direction == "stop right":
            self.action = "standing"
            self.speedx = 0
        elif direction == "stop left":
            self.action = "standing"
            self.speedx = 0
        
