import math, pygame, sys, random
#from Collisionhandler import *


class Charter: 

    def __init__(self, maxSpeed=4, speed = [8,8], startPos = [300,500], name = "monster",  image = "crazyPizza.png", doesFall = True):
        
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
        self.mass = 1
        self.standing = False
        self.hitCounter = 0
        self.hitAGuyX = False

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
        
    # ~ def wallCollide(self, size):
        # ~ width = size[0]
        # ~ height = size[1]
        # ~ if self.rect.bottom > height:
            # ~ self.rect.bottom = height
            # ~ self.speedy = 0
            # ~ self.jumping = False
            # ~ #print("Hit Ground")
        # ~ if not self.didBounceY:
            
            # ~ if self.rect.top < 0:
                # ~ self.speedy = -self.speedy
                # ~ self.move()
                # ~ self.speedy = 0
                # ~ self.didBounceY = True
        # ~ if not self.didBounceX:
            # ~ if self.rect.right > width:
                # ~ self.speedx = -self.speedx
                # ~ self.move()
                # ~ self.speedx = 0
                # ~ self.didBounceX = True
            # ~ if self.rect.left < 0:
                # ~ self.speedx = -self.speedx
                # ~ self.move()
                # ~ self.speedx = 0
                # ~ self.didBounceX = True
    
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:   
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if self.kind == "Bro":
                            if self.rect.bottom > other.rect.top + 25:
                                self.speedx = -self.speedx
                                print("weeeee")
                            self.speedy = -self.speedy
                            self.move()
                            if self.rect.bottom > other.rect.top + 1:
                                self.speedx = 0
                                print("wooooo")
                            if self.rect.right > other.rect.left:   
                                if self.rect.left < other.rect.right:
                                    if self.rect.bottom > other.rect.top:
                                        if self.rect.top < other.rect.bottom:
                                            self.rect.bottom = other.rect.top
                                            print("Get out of wall")
                            self.speedy = 0
                            self.didBounceX = True
                            self.didBounceY = True
                            if not self.rect.bottom > other.rect.top:
                                #print("jump")
                                self.jumping = False
                            return True
                        if self.kind == "GoopyGlob":
                            if self.rect.top > other.rect.top or self.rect.bottom > other.rect.top:
                                self.speedx = -self.speedx
                                #print("wheeeee")
                            self.speedy = -self.speedy
                            self.move()
                            if self.rect.top > other.rect.top or self.rect.bottom > other.rect.top:
                                self.speedx = 0
                                #print("whooooo")
                            self.speedy = 0
                            #self.didBounceX = True
                            #self.didBounceY = True
                            self.jumping = False
                            if int(self.rect.bottom) == int(other.rect.top) - 1: self.standing = True
                            return True
                        
    def charterChaterCollide(self, other):
        if self != other:
            if self.hitAGuyX == False:
                if self.didBounceY == False:
                    #print("ouch")
                    if self.rect.right > other.rect.left:   
                        if self.rect.left < other.rect.right:
                            if self.rect.bottom > other.rect.top:
                                if self.rect.top < other.rect.bottom:
                                    if self.kind == "Bro" or other.kind == "Bro":
                                        if other.kind == "Bro":
                                            if other.hitCounter > 30:
                                                other.health -= self.damage
                                                other.hitCounter = 0
                                        if self.kind == "Bro":
                                            if self.hitCounter > 30:
                                                self.health -= other.damage
                                                self.hitCounter = 0
                                        if self.rect.center != other.rect.center:
                                            self.elasticCollision(other, 'x')
                                            if other.standing == False:
                                                self.elasticCollision(other, 'y')
                                            self.move()

                                            self.hitAGuyX = False
                                    
    def charterWeaponCollide(self, other):
        if self != other:
            if self.kind != "Bro":
                if self.hitAGuyX == False:
                    if self.didBounceY == False:
                        #print("ouch")
                        if self.rect.right > other.rect.left:   
                            if self.rect.left < other.rect.right:
                                if self.rect.bottom > other.rect.top:
                                    if self.rect.top < other.rect.bottom:
                                        print("kind discovered")
                                        self.speedy -= other.mass / 4
                                        self.speedx = other.speedx * other.mass / 40
                                        self.health -= other.damage
                                        self.move()
                
    def update(self, size, playerpos):
        self.playerpos = playerpos
        #print(self.speed)
        self.speedy += self.gravity
        self.move()
        self.didBounceX = False
        self.didBounceY = False
        # ~ self.wallCollide(size)
        self.standing = False
        self.hitCounter += 1
        self.hitAGuyX = False
        
    def elasticCollision(self, other, direction):
        # ~ ke10=(mass1*myInitialVelocity**2)/2
        # ~ ke20=(mass2*thierInitialVelocity**2)/2
        # ~ p10=mass1*myInitialVelocity
        # ~ p20=mass2*thierInitialVelocity
        if direction == 'x':
            myInitialVelocity = self.speedx
            thierInitialVelocity = other.speedx
        else:
            myInitialVelocity = self.speedy
            thierInitialVelocity = other.speedy
        
        myFinalVelocity=((2 * self.mass * myInitialVelocity + (other.mass - self.mass) * thierInitialVelocity)/(other.mass + self.mass) + thierInitialVelocity - myInitialVelocity)/2
        # ~ ke10+ke20=ke11+ke21
        # ~ p10+p20=p11+p21
        #print(str(finalVelocity1) + " is first velo" + "\n" + str(finalVelocity2) + " is second velo")
        if direction == 'x':
            self.speedx = myFinalVelocity
        else:
            self.speedy = myFinalVelocity
        


