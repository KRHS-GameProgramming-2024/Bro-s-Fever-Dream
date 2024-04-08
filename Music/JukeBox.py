import pygame
pygame.init()
pygame.mixer.init()


if music == "1":
    pygame.mixer.music.load("CaveThemeIntro.mp3")
    pygame.mixer.music.queue("CaveThemeLoop.mp3", "mp3", -1)
    pygame.mixer.music.play()		
elif music == "2":
    pygame.mixer.music.load("FinalBossIntro.mp3")
    pygame.mixer.music.queue("FinalBossLoop.mp3", "mp3", -1)
    pygame.mixer.music.play()		
elif music == "3":
    pygame.mixer.music.load("FinalBossLoop.mp3")
    pygame.mixer.music.play(-1)
elif music == "4":
    pygame.mixer.music.load("SadThemeLoop.mp3")
    pygame.mixer.music.play(-1)
elif music == "5":
    pygame.mixer.music.load("StarterEnemyThemeIntro.mp3")
    pygame.mixer.music.queue("StarterEnemyThemeLoop.mp3", "mp3", -1)
    pygame.mixer.music.play()
elif music == "6":
    pygame.mixer.music.load("TheLava.mp3")
    pygame.mixer.music.play(-1)
elif music == "7":
    pygame.mixer.music.load("SeriousConversationIntro.mp3")
    pygame.mixer.music.queue("SeriousConversationLoop.mp3", "mp3", -1)
    pygame.mixer.music.play()
elif muusic == "0":
    pygame.mixer.music.load("Test1.mp3")
    pygame.mixer.music.queue("Test2.mp3", "mp3", -1)
    pygame.mixer.music.play()


