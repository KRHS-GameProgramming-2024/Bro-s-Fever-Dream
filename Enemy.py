import math, pygame, sys, random
from Collisionhandler import *

class Charter: 

    def __init__(self, maxSpeed=4, speed = [8,8], startPos=[random.randint(200,1300),random.randint(200,700)], name = "monster", damage = 1, health = 1, weight = 50, image = "crazyPizza.png", doesFall = True):
        
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
        
        self.gravity = 1
        self.jumping = False
        self.jumpHeight = 25
        
    
        
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
        if self.rect.bottom > height:
            self.rect.bottom = height
            self.speedy = 0
            self.jumping = False
            #print("Hit Ground")
        if not self.didBounceY:
            
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
    
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:   
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        #self.speedx = -self.speedx
                        self.speedy = -self.speedy
                        self.move()
                        #self.speedx = 0
                        self.speedy = 0
                        self.didBounceX = True
                        self.didBounceY = True
                        self.jumping = False
                        return True
                        
    def charterChaterCollide(self, other):
        if self != other:
            if self.didBounceX == False:
                if self.didBounceY == False:
                    if self.rect.right > other.rect.left:   
                        if self.rect.left < other.rect.right:
                            if self.rect.bottom > other.rect.top:
                                if self.rect.top < other.rect.bottom:
                                    # ~ print("we're getting there")
                                    if other.kind == "Bro" or self.kind == "Bro":
                                        if self.rect.bottom > other.rect.top:
                                            if not abs(self.speedy) < abs(other.speedy):
                                                self.speedy = -self.speedy
                                                self.move
                                                # ~ print("a collision tried to happen here")
                                            else:
                                                self.speedy = other.speedy
                                                # ~ print("a collision tried to happen here")
                                        elif self.rect.top < other.rect.bottom:
                                            if not abs(self.speedy) > abs(other.speedy):
                                                self.speedy = -self.speedy
                                                self.move
                                                # ~ print("a collision tried to happen here")
                                            else:
                                                self.speedy = other.speedy
                                                # ~ print("a collision tried to happen here")
                                        else:
                                            pass
        
                
    def update(self, size, playerpos):
        self.playerpos = playerpos
        #print(self.speed)
        self.speedy += self.gravity
        self.move()
        self.didBounceX = False
        self.didBounceY = False
        self.wallCollide(size)

