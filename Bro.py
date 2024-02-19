import math, pygame, sys, random
	
size = [1500,900]	
		
class Bro():
	def __init__(self, maxSpeed=4, speed = [8,8], startPos=[0,1]):
		self.image = pygame.image.load("Bro/Images/BroLeft.png")
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(startPos)
		self.maxSpeed = maxSpeed
		self.speedx = speed[0]
		self.speedy = speed[1]
		self.speed = [self.speedx, self.speedy]
		self.kind = "Bro"
		
		self.didBounceX = False
		self.didBounceY = False
		self.wallCollide(size)	
		
	def move(self):
		self.speed = [self.speedx, self.speedy]
		self.rect = self.rect.move(self.speed)		

	def goKey(self, direction):
		if direction == "left":
			self.speedx = -self.maxSpeed
		elif direction == "right":
			self.speedx = self.maxSpeed
		elif direction == "up":
			self.speedy = -self.maxSpeed
		elif direction == "down":
			self.speedy = self.maxSpeed
		elif direction == "sleft":
			self.speedx = 0
		elif direction == "sright":
			self.speedx = 0
		elif direction == "sup":
			self.speedy = 0
		elif direction == "sdown":
			self.speedy = 0
			
	def wallCollide(self, size):
		width = size[0]
		height = size[1]
		if not self.didBounceY:
			if self.rect.bottom > height:
				self.speedy = -self.speedy
				self.move()
				self.speedy = 0
				self.didBounceY = True
			if self.rect.top < 0:
				self.speedy = -self.speedy
				self.move()
				self.speedy = 0
				self.didBounceY = True
				
		if not self.didBounceX:
			if self.rect.right > width:
				self.speedx = -self.speedx
				self.move()
				self.speedx = 0
				self.didBounceX = True
			if self.rect.left < 0:
				self.speedx = -self.speedx
				self.move()
				self.speedx = 0
				self.didBounceX = True
	def update(self, size):
		self.move()
		



