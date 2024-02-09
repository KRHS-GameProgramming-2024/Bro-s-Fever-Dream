import math, pygame, sys, random
from Bro import*

pygame.init()

size = [1500,900]
screen = pygame.display.set_mode(size)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();
