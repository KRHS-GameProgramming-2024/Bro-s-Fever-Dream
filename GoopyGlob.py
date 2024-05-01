from Enemy import *

class GloopyGlob(Charter):
    def __init__(self):
        Charter.__init__(self, name = "Goopy Glob", image = "Earth\GoopyGlob\Images\GoopyGlob.png")
        self.gravity = 2
        self.mass = 28
        self.didBounceY = False
        self.damage = random.randint(1,250)
        self.health = 50
        
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
        
         

