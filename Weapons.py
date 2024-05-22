import pygame, sys, random
from math import *
from Bro import *

def getScaledMouse():
    size = [1024,768]
    x, y=pygame.display.get_surface().get_size()
    xScale=size[0]/x
    yScale=size[1]/y
   
    x2=x/size[0]
    y2=y/size[1]
   
    if x2==y2:
        offset=[0,0]
    elif x2>y2:
        offset=[(x-y)/2,0]
    elif x2<y2:
        offset=[0,(y-x)/2]
    else:
        print('something went wrong, check function "getScaledMouse"')
   
    mousex,mousey=pygame.mouse.get_pos()
   
    return [xScale*mousex, yScale*mousey]

class dagger:
    def __init__(self, useSpeed = 1, 
                   startPos = [0, 1], 
                   angle = int(pi/3), 
                   name = "Soup Ladle",  
                   images = [pygame.image.load("Earth/SoupLadle/Images/SoupLadleLeft.png"), 
                            pygame.image.load("Earth/SoupLadle/Images/SoupLadleRight.png")
                            ]):
        self.images = [pygame.image.load("Earth/SoupLadle/Images/SoupLadleLeft.png"), pygame.image.load("Earth/SoupLadle/Images/SoupLadleRight.png")]
        self.facing = angle
        self.frame = 1
        print(self.images)
        self.image = self.images[self.frame]  
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
        self.playerSpeedX = 0
        self.playerSpeedY = 0
        self.live = 0
        
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
            self.speedx = 5 * self.speedScaler * (cos(self.facing)) + self.playerSpeedX * 2
            self.speedy = 5 * self.speedScaler * (sin(self.facing)) + self.playerSpeedY
            self.image = pygame.transform.rotate(self.image, 315 - (180 * self.facing / math.pi))
        if self.change == 2:
            self.speedx = 4 * self.speedScaler * (cos(self.facing)) + self.playerSpeedX * 2
            self.speedy = 4 * self.speedScaler * (sin(self.facing)) + self.playerSpeedY
        if self.change == 3:
            self.speedx = 3 * self.speedScaler * (cos(self.facing)) + self.playerSpeedX * 2
            self.speedy = 3 * self.speedScaler * (sin(self.facing)) + self.playerSpeedY
        if self.change == 4:
            self.speedx = -3 * self.speedScaler * (cos(self.facing)) + self.playerSpeedX * 2
            self.speedy = -3 * self.speedScaler * (sin(self.facing)) + self.playerSpeedY
        if self.change == 5:
            self.speedx = -4 * self.speedScaler * (cos(self.facing)) + self.playerSpeedX * 2
            self.speedy = -4 * self.speedScaler * (sin(self.facing)) + self.playerSpeedY
        if self.change == 6:
            self.speedx = -5 * self.speedScaler * (cos(self.facing)) + self.playerSpeedX * 2
            self.speedy = -5 * self.speedScaler * (sin(self.facing)) + self.playerSpeedY
        self.change += 1/self.timeScaler
        # ~ print(self.change)
        # ~ print("sine of angle ", sin(self.facing), " cosine of angle ", cos(self.facing), " self.facing ", self.facing)
        # ~ print("Movement: " + str([self.movementX, self.movementX]))
        return self.change
        
            
    def update(self, player):
        if (3 * math.pi / 2) > self.facing > (math.pi / 2):
            self.frame = 0
        else:
            self.frame = 1
        adjacent = 1
        self.live += 1
        # ~ print("Mouse Pos: " + str(getScaledMouse()) + ", Player Pos: " + str(player.rect.center))
        diff = [(getScaledMouse()[0] - player.rect.center[0]), (getScaledMouse()[1] - player.rect.center[1])]
        adjacent = diff[0]
        if adjacent == 0:
            adjacent = .01
    
        self.facing = atan(diff[1] / adjacent)
        if (diff[0] < 0):
            self.facing += math.pi
        # ~ print("Facing: ", self.facing, "Adjacent: ", adjacent)
        
        # ~ if self.live == 1:
            # ~ self.speedx += player.speedx
            # ~ self.speedy += player.speedy
        # ~ print("-------> was: ", self.speedx, self.speedy)
        # ~ if player.speedy != self.playerSpeedY:
            # ~ self.speedy -= self.playerSpeedY
            # ~ self.playerSpeedY = player.speedy
            # ~ self.speedy += self.playerSpeedY
        # ~ if player.speedx != self.playerSpeedX:
            # ~ self.speedx -= self.playerSpeedX
            # ~ self.playerSpeedX = player.speedx
            # ~ self.speedx += self.playerSpeedX
        # ~ print("-------> now: ", self.speedx, self.speedy)
        self.playerSpeedX = player.speedx
        self.playerSpeedY = player.speedy
        self.animate()
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
# ~ class shield:
    # ~ pass
class shooter:
    def __init__(self, useSpeed = 1, 
                   startPos = [0, 1], 
                   angle = int(pi/3), 
                   name = "Soup Ladle",  
                   images = [pygame.image.load("Earth/SoupLadle/Images/SoupLadleLeft.png"), 
                            pygame.image.load("Earth/SoupLadle/Images/SoupLadleRight.png")
                            ]):
        self.images = [pygame.image.load("Earth/SoupLadle/Images/SoupLadleLeft.png"), pygame.image.load("Earth/SoupLadle/Images/SoupLadleRight.png")]
        self.facing = angle
        self.frame = 1
        print(self.images)
        self.image = self.images[self.frame]  
        self.rect = self.image.get_rect(center = startPos)
        #self.rect = self.rect.animate(startPos)
        self.useSpeed = useSpeed
        self.movementX = 0
        self.movementY = 0
        self.movement = [self.movementX, self.movementY]
        self.change = 1
        self.mass = .01
        self.damage = 9999
        adjacent = 100
        self.kind = "Popper"
        self.speedy = 0
        self.speedx = 0
        self.playerSpeedX = 0
        self.playerSpeedY = 0
        self.speedScaler = 2
        self.timeScaler = 3
        self.effectStart = pygame.mixer.Sound("Air/BubbleLauncher/Sounds")
        self.effectContinue = pygame.mixer.Sound("Air/BubbleLauncher/Sounds")
        self.specialeffectStart = pygame.mixer.Sound("Air/BubbleLauncher/Sounds")
        self.specialeffectContinue = pygame.mixer.Sound("Air/BubbleLauncher/Sounds")
        
    def move(self):
        self.image = pygame.transform.rotate(self.image, 315 - (180 * self.facing / math.pi))
        self.movement = [self.playerSpeedX, self.playerSpeedY]
        # ~ print("movement trying to go, movement = ", self.movement)
        self.rect = self.rect.move(self.movement)
        # ~ print("Rect: ", self.rect)
        
    def animate(self):
        self.effectStart.play()
        if self.live == 1:
            self.image = pygame.transform.rotate(self.image, 270 - (180 * self.facing / math.pi))
            self.previousRotation = 270 - (180 * self.facing / math.pi)
            self.pin += 1
            if self.pin == self.timeScaler:
                self.firing = True
                self.pin = 0
        else: 
            self.image = pygame.transform.rotate(self.image, 270 - (180 * self.facing / math.pi) - self.previousRotation)
            self.previousRotation = 270 - (180 * self.facing / math.pi) - self.previousRotation
            self.pin += 1
            if self.pin == self.timeScaler:
                self.firing = True
                self.pin = 0
        
    def update(self, player):
        if (3 * math.pi / 2) > self.facing > (math.pi / 2):
            self.frame = 0
        else:
            self.frame = 1
        adjacent = 1
        self.live += 1
        # ~ print("Mouse Pos: " + str(getScaledMouse()) + ", Player Pos: " + str(player.rect.center))
        diff = [(getScaledMouse()[0] - player.rect.center[0]), (getScaledMouse()[1] - player.rect.center[1])]
        adjacent = diff[0]
        if adjacent == 0:
            adjacent = .01
    
        self.facing = atan(diff[1] / adjacent)
        if (diff[0] < 0):
            self.facing += math.pi
        # ~ print("Facing: ", self.facing, "Adjacent: ", adjacent)
        
        if player.speedy != self.playerSpeedY:
            self.playerSpeedY = player.speedy
            self.speedy += self.playerSpeedY
        if player.speedx != self.playerSpeedX:
            self.playerSpeedX = player.speedx
            self.speedx += self.playerSpeedX 
        
        self.move()

class projectile:
    pass
