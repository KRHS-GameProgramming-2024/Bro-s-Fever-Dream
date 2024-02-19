import math, pygame, sys, random
from Bro import*

pygame.init()

size = [1500,900]
screen = pygame.display.set_mode(size)

Clock = pygame.time.Clock();

player = Bro(8, [0,0], [1500/2, 900/2])
Bros = [player]
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				player.goKey("left")
			elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				player.goKey("right")
			elif event.key == pygame.K_w or event.key == pygame.K_UP:
				player.goKey("up")
			elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
				player.goKey("down")
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				player.goKey("sleft")
			elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				player.goKey("sright")
			elif event.key == pygame.K_w or event.key == pygame.K_UP:
				player.goKey("sup")
			elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
				player.goKey("sdown")	
	
	screen.fill((13, 54, 22))
	for Bro in Bros:
		screen.blit(Bro.image, Bro.rect)
	pygame.display.flip()
	Clock.tick(60);
	print(Clock.get_fps())

	for Bro in Bros:
		Bro.update(size)
