import pygame
pygame.init()
pygame.mixer.init()

SONGEND = pygame.USEREVENT

print("1: Cave Theme \n2: Final Boss\n3: Final Boss 2nd Phase\n4: Sad Theme\n5: Starter Enemy Theme\n6: The Lava")

while True:
	number = input("Press a number: ")


	if number == "1":
		print("Cave Theme")
		pygame.mixer.music.load("CaveThemeIntro.mp3")
		pygame.mixer.music.queue("CaveThemeLoop.mp3", "mp3", -1)
		pygame.mixer.music.play()		
	elif number == "2":
		print("Final Boss")
		pygame.mixer.music.load("FinalBossIntro.mp3")
		pygame.mixer.music.queue("FinalBossLoop.mp3", "mp3", -1)
		pygame.mixer.music.play()		
	elif number == "3":
		print("Final Boss 2nd Phase")
		pygame.mixer.music.load("FinalBossLoop.mp3")
		pygame.mixer.music.play(-1)
	elif number == "4":
		print("Sad Theme")
		pygame.mixer.music.load("SadTheme.mp3")
		pygame.mixer.music.play(-1)
	elif number == "5":
		print("Starter Enemy Theme")
		pygame.mixer.music.load("StarterEnemyTheme.mp3")
		pygame.mixer.music.play(-1)
	elif number == "6":
		print("The Lava")
		pygame.mixer.music.load("TheLava.mp3")
		pygame.mixer.music.play(-1)
	elif number == "0":
		print("Test")
		pygame.mixer.music.load("Test1.mp3")
		pygame.mixer.music.queue("Test2.mp3", "mp3", -1)
		pygame.mixer.music.play()



