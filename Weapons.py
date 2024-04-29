from math import *

class dagger:
    __init__(self, useSpeed = 1, startPos = [100, 100], angle = int(pi/3), name = "Soup Ladle",  images = ["Earth/SoupLadle/Images/SoupLadleLeft.png", "Earth/SoupLadle/Images/SoupLadleRight.png"):
        self.images = [pygame.image.load(image)]
        
        
        self.facing = angle
        self.image = self.images[self.frame]  
        self.rect = self.image.get_rect()
        self.rect = self.rect.animate(startPos)
        self.useSpeed = useSpeed
        self.movementX = 0
        self.movementY = 0
        self.movement = [self.movementX, self.movementY]
        self.change = 0
        self.mass = 1
        self.damage = 9999
        
        def pos(self):
            self.rect = self.rect + self.movement
                    
        def animate(self):
            if self.change = 1:
                self.movementX = 3(cos(self.facing))
                self.movementY = 3(sin(self.facing))
            if self.change = 2:
                self.movementX = 2(cos(self.facing))
                self.movementY = 2(sin(self.facing))
            if self.change = 3:
                self.movementX = 1(cos(self.facing))
                self.movementY = 1(sin(self.facing))
            if self.change = 4:
                self.movementX = -1(cos(self.facing))
                self.movementY = -1(sin(self.facing))
            if self.change = 5:
                self.movementX = -2(cos(self.facing))
                self.movementY = -2(sin(self.facing))
            if self.change = 6:
                self.movementX = -3(cos(self.facing))
                self.movementY = -3(sin(self.facing))
            self.change += 1
            self.pos()
            
        def update(self)
            

                
            
                
class sword:
    __init__(self, , useSpeed = 1, startPos = , name = "Frost Ae",  images = ["Water/FrostAxe/Images/FrostAxeLeft.png", "Water/FrostAxe/Images/FrostAxeRight.png"):
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
class staff:
    pass
class shooter:
    pass
    
