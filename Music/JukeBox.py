import pygame
pygame.init()
pygame.mixer.init()

while True:
	number = input("Press a number: ")

	if number == "1":
		print("Cave Theme")
		pygame.mixer.music.load("CaveTheme.mp3")
		pygame.mixer.music.play(-1)	
	elif number == "2":
		print("Final Boss")
		pygame.mixer.music.load("FinalBoss.mp3")
		pygame.mixer.music.play()
		pygame.mixer.music.queue("FinalBossLoop.mp3")
		pygame.mixer.music.play(-1)	
	elif number == "3":
		print("Final Boss 2nd Phase")
		pygame.mixer.music.load("CaveTheme.mp3")
		pygame.mixer.music.play(-1)
	elif number == "4":
		print("Sad Theme")
		pygame.mixer.music.load("SadTheme.mp3")
		pygame.mixer.music.play(-1)




