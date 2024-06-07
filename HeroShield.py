from  Weapons import *

class HeroShield(shield):
    def __init__(self, startpos):
        shield.__init__(self, startPos = startpos, name = "Hero Shield", images = ["Earth/SoupLadle/Images/SoupLadleRight.png"])
        self.gravity = 2
        self.mass = 162
        self.didBounceY = False
        self.damage = 162
        self.speedScaler = 0.1
        self.timeScaler = 1  
