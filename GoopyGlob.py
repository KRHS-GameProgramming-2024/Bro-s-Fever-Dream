from Enemy import *

class GoopyGlob(Charter):
    def __init__(self, startPos = [500, 500]):
        Charter.__init__(self, startPos = [500, 500], name = "Goopy Glob", image = "Earth\GoopyGlob\Images\GoopyGlob.png")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(startPos)
        self.gravity = 2
        self.mass = 28
        self.didBounceY = False
        self.damage = 20
        self.health = 20
        
        self.kind = "GoopyGlob"
    
        
    def move(self):
        if random.randint(1, 250) == 1:
            if self.rect.x > self.playerpos:
                self.speedx = random.randint(-25, 0)
                self.speedy = -30
            elif self.rect.x < self.playerpos:
                self.speedx = random.randint(0, 25)
                self.speedy = -30
        if self.speedy == 28:
            self.speedx = 0
            
            
        self.rect = self.rect.move(self.speedx, self.speedy)
        
         

