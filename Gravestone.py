from Enemy import *

class Gravestone():
    def __init__(self, startPos = [300,500], speed = [8,8]):
        self.image = pygame.image.load("Bro/Images/Gravestone.png")
        self.gravity = 2
        self.mass = 50
        self.didBounceY = False
        self.didBounceX = False
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rect = self.image.get_rect()
        self.rect.center = startPos
        self.kind = "Gravestone"
        
    def move(self):
        self.speedx = 0
        self.rect = self.rect.move(self.speedx, self.speedy)
        
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:   
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.speedx = -self.speedx
                        self.speedy = -self.speedy
                        self.move()
                        self.speedx = 0
                        self.speedy = 0
                        self.didBounceX = True
                        self.didBounceY = True
                        return True
    
    def update(self):
        self.speedy += self.gravity
        self.move()
        self.didBounceX = False
        self.didBounceY = False
