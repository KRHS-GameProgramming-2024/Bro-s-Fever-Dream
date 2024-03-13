import math, pygame, sys, random

class Enemy: 
    def __init__(self, maxSpeed=4, speed = [8,8], startPos=[random.randint(0,1500),random.randint(0,900)], name = "monster", damage = "1", health = "1", image = "crazyPizza.png", doesFall = True):
        
        self.images = [pygame.image.load(image)]
        
        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]  
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(startPos)
        self.maxSpeed = maxSpeed
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.kind = "Enemy"



        self.didBounceX = False
        self.didBounceY = False
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed) 
        
    def look(self, look):
        if look == "right":
            self.frame = 1
        elif look == "left":
            self.frame = 0
        self.image = self.images[self.frame]
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
            if self.rect.top < 0:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
        if not self.didBounceX:
            if self.rect.right > width:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
            if self.rect.left < 0:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
    
    def wallsCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBounceX = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True
                            return True
                        pass
    def fall(self, size):
        if doesFall == True:
            if self.rect.bottom > 0:
                self.speedy += 6
            if self.rect.bottom == 0:
                self.speedy = 0

def GoopyGlobSpawn():
    Enemy(name = "Goopy Glob", damage = random.randint(1,6), health = 50, image = "Earth\GoopyGlob\Images\GooppyGlob.png")
