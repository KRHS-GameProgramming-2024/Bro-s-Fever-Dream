import pygame, sys, random
from math import *
from Bro import *

class dagger:
    def __init__(self, useSpeed = 1, 
                   startPos = [0, 1], 
                   angle = int(pi/3), 
                   name = "Soup Ladle",  
                   images = ["Earth/SoupLadle/Images/SoupLadleLeft.png"] 
                             ):
        self.images = []
        for image in images:
            self.images += [pygame.image.load(image)]
        self.facing = angle
        self.image = self.images[0]  
        self.rect = self.image.get_rect(center = startPos)
        #self.rect = self.rect.animate(startPos)
        self.useSpeed = useSpeed
        self.movementX = 0
        self.movementY = 0
        self.movement = [self.movementX, self.movementY]
        self.change = 1
        self.mass = 1
        self.damage = 9999
        adjacent = 100
        self.kind = "Dagger"
        self.speedy = 0
        self.speedx = 0
        
        self.speedScaler = 2
        self.timeScaler = 3
        
    def move(self):
        self.movement = [round(self.speedx), round(self.speedy)]
        # ~ print("movement trying to go, movement = ", self.movement)
        self.rect = self.rect.move(self.movement)
        # ~ print("Rect: ", self.rect)
        
                
    def animate(self):
        print("animate is called")
        if self.change == 1:
            self.speedx = 5 * self.speedScaler * (cos(self.facing))
            self.speedy = 5 * self.speedScaler * (sin(self.facing))
        if self.change == 2:
            self.speedx = 4 * self.speedScaler * (cos(self.facing))
            self.speedy = 4 * self.speedScaler * (sin(self.facing))
        if self.change == 3:
            self.speedx = 3 * self.speedScaler * (cos(self.facing))
            self.speedy = 3 * self.speedScaler * (sin(self.facing))
        if self.change == 4:
            self.speedx = -3 * self.speedScaler * (cos(self.facing))
            self.speedy = -3 * self.speedScaler * (sin(self.facing))
        if self.change == 5:
            self.speedx = -4 * self.speedScaler * (cos(self.facing))
            self.speedy = -4 * self.speedScaler * (sin(self.facing))
        if self.change == 6:
            self.speedx = -5 * self.speedScaler * (cos(self.facing))
            self.speedy = -5 * self.speedScaler * (sin(self.facing))
        self.change += 1/self.timeScaler
        # ~ print(self.change)
        # ~ print("sine of angle ", sin(self.facing), " cosine of angle ", cos(self.facing), " self.facing ", self.facing)
        # ~ print("Movement: " + str([self.movementX, self.movementX]))
        return self.change
            
    def update(self, player):
        adjacent = 1
        # ~ print("Mouse Pos: " + str(pygame.mouse.get_pos()) + ", Player Pos: " + str(player.rect.center))
        diff = [(pygame.mouse.get_pos()[0] - player.rect.center[0]), (pygame.mouse.get_pos()[1] - player.rect.center[1])]
        adjacent = diff[0]
        if adjacent == 0:
            adjacent = .01
    
        self.facing = atan(diff[1] / adjacent)
        if (diff[0] < 0):
            self.facing += math.pi
        # ~ print("Facing: ", self.facing, "Adjacent: ", adjacent)
        self.animate()
        self.speedx += player.speedx / 2
        self.speedy += player.speedy / 2
        self.move()

                
            
                
class sword:
    def __init__(self, useSpeed = 1, 
                    startPos = [0, 0], 
                    name = "Frost Axe",  
                    images = ["Water/FrostAxe/Images/FrostAxeLeft.png", "Water/FrostAxe/Images/FrostAxeRight.png"]):
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

# ~ class staff:
    # ~ pass
# ~ class shooter:
    # ~ pass
    
