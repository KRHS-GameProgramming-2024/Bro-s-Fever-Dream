from  Weapons import *

class HeroShield(shield):
    def __init__(self, startpos):
        shield.__init__(self, startPos = startpos, name = "Hero Shield", images = [pygame.image.load("Earth/Shield/Images/HeroShieldRight.png"), 
                                                                                   pygame.image.load("Earth/Shield/Images/HeroShieldLeft.png")])
        self.gravity = 2
        self.mass = 81
        self.didBounceY = False
        self.damage = 0
        self.speedScaler = 0.1
        self.timeScaler = 0.5
