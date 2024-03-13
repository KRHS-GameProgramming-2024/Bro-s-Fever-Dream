import math, pygame, sys, random
from Bro import*
from Walls import*
from Enemy import *

pygame.init()

size = [1500,900]
screen = pygame.display.set_mode(size)

Clock = pygame.time.Clock();

walls = [Wall([0,0]),
         Wall([75,75])]

player = Bro(8, [0,0], [1500/2, 900/2])
Bros = [player]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
                player.look("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
                player.look("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("up")
                print(player.jumping, player.speedy)
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
        
    for Charter in Bros:
        Charter.update(size)
    #print(player.jumping, player.speedy)
        
    screen.fill((255, 255, 255))
    for Bro in Bros:
        screen.blit(Bro.image, Bro.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    Clock.tick(60);
    #print(Clock.get_fps())

def GoopyGlobSpawn():
    Bros += [Enemy(name = "Goopy Glob", damage = random.randint(1,6), health = 50, image = "Earth\GoopyGlob\Images\GooppyGlob.png")]
