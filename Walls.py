import pygame, math, sys, random

class Wall():
	def __init__(self,  pos=[25,2]):
		self.image = pygame.image.load("Blocks/Dirt/Images/Dirt.png")
		self.rect = self.image.get_rect(center = pos)
		
		self.kind = "wall"
			
	def update(self, size):
		pass
