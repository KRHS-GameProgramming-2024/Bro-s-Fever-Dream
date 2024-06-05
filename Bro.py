import math, pygame, sys, random
from Enemy import *
#weapons
from Weapons import *
    #daggers
from SoupLadle import *
from Lavarang import *
    #swords
    
    #ranged

    
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
        self.baseSpeed = maxSpeed
        self.maxSpeedx = maxSpeed
        self.maxSpeedy = maxSpeed
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.weight = 15
        self.kind = "Bro"
        self.health = 100
        self.maxHealth = 100
        self.damage = 0
        self.hitCounter = 0
        self.run = "none"
        self.living = True
        self.scroll = 0
        if self.scroll == 0:
            self.equipped = Lavarang
        elif self.scroll == 1:
            self.quipped = SoupLadle    
        self.didBounceX = False
        self.didBounceY = False
        
    def regen(self):
        if self.health < self.maxHealth:
            if self.hitCounter > 499:
                if self.hitCounter % 25 == 0:
                    self.health += 1
                
    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeedx
            self.run = "left"
        elif direction == "right":
            self.speedx = self.maxSpeedx
            self.run = "right"
        elif direction == "up" and not self.jumping:
            #print("jumping")
            self.jumping = True
            self.speedy = -self.jumpHeight
        elif direction == "down":
            self.speedy = self.maxSpeedy
        elif direction == "sleft":
            if self.run == "left":
                self.speedx = 0
                self.run = "none"
        elif direction == "sright":
            if self.run == "right":
                self.speedx = 0
                self.run = "none"
        elif direction == "sup":
            # ~ self.speedy = 0
            pass
        elif direction == "sdown":
            self.speedy = 0
        elif direction == "run":
            self.maxSpeedx = self.baseSpeed+1
            if self.run == "left":
                self.speedx = -self.maxSpeedx
            if self.run == "right":
                self.speedx = self.maxSpeedx
            elif self.run == "none":
                pass
        elif direction == "srun":
            self.maxSpeedx = self.baseSpeed-1
            if self.run == "left":
                self.speedx = -self.maxSpeedx
            if self.run == "right":
                self.speedx = self.maxSpeedx
            elif self.run == "none":
                pass
    
    def weaponSwap(self, scroll):
        if scroll == 0:
            self.scroll = 0
            self.equipped = Lavarang
        elif scroll == 1:
            self.scroll = 1
            self.equipped = SoupLadle
        elif scroll == 2:
            self.scroll = 2
        
    
    def look(self, look):
        if look == "right":
            self.frame = 1
        elif look == "left":
            self.frame = 0
        self.image = self.images[self.frame]

    def update(self, size):
        # ~ if self.scroll == 0:
            # ~ self.equipped = Lavarang
        # ~ elif self.scroll == 1:
            # ~ self.quipped = SoupLadle    
        #print(self.scroll)
        #print(self.equipped)
        #print(self.speed)
        self.speedy += self.gravity
        self.move()
        self.didBounceX = False
        self.didBounceY = False
        # ~ self.wallCollide(size)
        self.hitCounter += 1
        self.regen()

