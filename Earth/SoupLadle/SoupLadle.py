lass GloopyGlob(Charter):
    def __init__(self):
        Charter.__init__(self, name = "Goopy Glob", image = "Earth\GoopyGlob\Images\GoopyGlob.png")
        self.gravity = 2
        self.mass = 28
        self.didBounceY = False
        self.damage = 4
        
        self.kind = "Dagger"
