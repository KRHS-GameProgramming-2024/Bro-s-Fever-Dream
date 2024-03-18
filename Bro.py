import math, pygame, sys, random
from Enemy import *
	
class Bro(Charter):
    def __init__(self, maxSpeed=4, speed = [8,8], startPos=[0,1]):
        Charter.__init__(self, [0,0], startPos)
        self.images = [pygame.image.load("Bro/Images/BroLeftBigger.png"),
                        pygame.image.load("Bro/Images/BroRightBigger.png")]
        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]  
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(startPos)
        self.maxSpeed = maxSpeed
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.kind = "Bro"
            
        self.didBounceX = False
        self.didBounceY = False
        
   
                
    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "up" and not self.jumping:
            self.jumping = True
            self.speedy = -self.jumpHeight
        elif direction == "down":
            self.speedy = self.maxSpeed
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        elif direction == "sup":
            # ~ self.speedy = 0
            pass
        elif direction == "sdown":
            self.speedy = 0
    
    def look(self, look):
        if look == "right":
            self.frame = 1
        elif look == "left":
            self.frame = 0
        self.image = self.images[self.frame]
        
                
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

    def update(self, size):
        #print(self.speed)
        self.speedy += self.gravity
        self.move()
        self.didBounceX = False
        self.didBounceY = False
        self.wallCollide(size)
    
        
        
