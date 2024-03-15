from Enemy import *

class GloopyGlob(Charter):
    def __init__(self):
        Charter.__init__(self, name = "Goopy Glob", damage = random.randint(1,6), health = 50, image = "Earth\GoopyGlob\Images\GoopyGlob.png")

    def move(self):
        pass
