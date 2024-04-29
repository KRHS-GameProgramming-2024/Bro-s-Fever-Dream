from Enemy import *

class Gravestone(Charter):
    def __init__(self):
        Charter.__init__(self, name = "Gravestone", image = "Bro/Images/Gravestone.png")
        self.gravity = 2
        self.mass = 50
        self.damage = 604874893763838763637648657458437623761287432765432976865865431896
        self.didBounceY = False
        
        self.kind = "Gravestone"
        
    def move(self):
        self.speedx = 0
        
        
        self.rect = self.rect.move(self.speedx, self.speedy)
        
