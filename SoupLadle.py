from  Weapons import *

class SoupLadle(dagger):
    def __init__(self, startpos):
        dagger.__init__(self, startPos = startpos, name = "Soup Ladle", images = ["Earth/SoupLadle/Images/SoupLadleRight.png"])
        self.gravity = 2
        self.mass = 28
        self.didBounceY = False
        self.damage = 4
        

        
        
