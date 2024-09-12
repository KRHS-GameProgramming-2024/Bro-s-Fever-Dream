from Weapons import *
from Bubble import * 

class BubbleLauncher(shooter):
    def __init__(self, startpos):
        shooter.__init__(self, startPos = startpos, name = "Bubble Launcher", 
                    images = ["Air/BubbleLauncher/Images/BubbleLauncherLeft.png", "Air/BubbleLauncher/Images/BubbleLauncherRight.png"])
        self.gravity = 0.001
        self.mass = 0.001
        self.damage = 0
        self.projVelo
        self.projectile = Bubble([self.rect.center[0], self.rect.center[1]], self.facing, self.projVelo, self.damage)
        