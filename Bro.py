import math, pygame, sys, random

class Bro():
	def __init__(self, maxSpeed=4, startPos=[0,0]):
		self.images = [pygame.image.load("Bro/Images/BroLeft.png"),
					   pygame.image.load("Bro/Images/BroRight.png")]
		self.maxSpeed = maxSpeed
		self.image = self.images
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(startPos)
		self.speed = [self.speedx, self.speedy]
		self.kind = "Bro"
		
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
			
