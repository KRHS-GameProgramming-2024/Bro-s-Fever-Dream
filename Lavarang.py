from  Weapons import *

class Lavarang(boomerang):
    def __init__(self, startpos):
        boomerang.__init__(self, startPos = startpos, name = "Lavarang", images = ["Fire/Lavarang/Images/Lavarang.png"])
        # ~ self.image = self.images[self.frame]  
        # ~ self.rect = self.image.get_rect(center = self.rect.center)
        
        self.gravity = 0.01
        self.mass = 100
        self.didBounceY = False
        self.damage = 80
        self.speedScaler = 5
        self.timeScaler = 7