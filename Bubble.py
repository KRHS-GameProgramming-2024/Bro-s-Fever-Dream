from Weapons import *

class Bubble(projectile):
    def __init__(self, startpos):
        projectile.__init__(self, startPos = startpos, name = "Bubble", images = ["Air/BubbleLauncher/Images/Bubble.png"])