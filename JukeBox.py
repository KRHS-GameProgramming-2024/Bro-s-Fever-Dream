import pygame
pygame.init()
pygame.mixer.init()

SONGEND = pygame.USEREVENT

def music(number): 
    if number == 1:
        print("music")
        pygame.mixer.music.load("Music/CaveThemeIntro.mp3")
        pygame.mixer.music.queue("Music/CaveThemeLoop.mp3", "mp3", -1)
        pygame.mixer.music.play()		
    elif number == 2:		
        pygame.mixer.music.load("Music/FinalBossIntro.mp3")
        pygame.mixer.music.queue("Music/FinalBossLoop.mp3", "mp3", -1)
        pygame.mixer.music.play()		
    elif number == 3:	
        pygame.mixer.music.load("Music/FinalBossLoop.mp3")
        pygame.mixer.music.play(-1)
    elif number == 4:		
        pygame.mixer.music.load("Music/SadThemeLoop.mp3")
        pygame.mixer.music.play(-1)
    elif number == 5:		
        pygame.mixer.music.load("Music/StarterEnemyThemeIntro.mp3")
        pygame.mixer.music.queue("Music/StarterEnemyThemeLoop.mp3", "mp3", -1)
        pygame.mixer.music.play()
    elif number == 6:
        pygame.mixer.music.load("Music/TheLava.mp3")
        pygame.mixer.music.play(-1)
    elif number == 7:
        pygame.mixer.music.load("Music/SeriousConversationIntro.mp3")
        pygame.mixer.music.queue("Music/SeriousConversationLoop.mp3", "mp3", -1)
        pygame.mixer.music.play()
    elif number == 0:	
        pygame.mixer.music.load("Music/Test1.mp3")
        pygame.mixer.music.queue("Music/Test2.mp3", "mp3", -1)
        pygame.mixer.music.play()



