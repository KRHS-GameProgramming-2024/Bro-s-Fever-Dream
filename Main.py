import math, pygame, sys, random
from LevelLoader import *
from Bro import*
from Walls import*
from Enemy import *
from GoopyGlob import *
from JukeBox import *
from Hud import *
from HealthBar import *

pygame.init()

size = [1024,768]
screen = pygame.display.set_mode(size)

Clock = pygame.time.Clock();

tiles = loadLevel("levels/Template.lvl")
walls = tiles
counter = 0
walls = tiles
Death = Hud("", [1024/2 - 30, 768/2])
Health = Hud("Health: ", [500,500])
Healthbar = HealthBar(pygame.image.load("Bro/Images/HealthBar.png"), [500,500])

music(1)

player = Bro(5, [0,0], [1024/2, 768/2])
Bros = [player]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            print(event.key)
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
            elif event.key == pygame.K_i or event.key == pygame.K_SPACE:
                player.goKey("run")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")
            elif event.key == pygame.K_i or event.key == pygame.K_SPACE:
                player.goKey("srun")
    
    counter += 1
    #print(counter)
    if counter % 300 == 0:
        Bros += [GloopyGlob()]
        print("go")
    for Charter in Bros:
        if Charter.kind == "Bro":
            Charter.update(size)
        else:
            Charter.update(size, Bros[0].rect.x)
    #Health = Hud("Health: ", [player.rect.center[0] - 90, player.rect.center[1] - 70])
    Health.update(player.health)
    Death.update("")
    Healthbar = HealthBar(pygame.image.load("Bro/Images/HealthBar.png"), [player.rect.center[0] - 30, player.rect.center[1] - 55])
    if player.health > 0:
        Healthbar.update(pygame.transform.scale(pygame.image.load("Bro/Images/HealthBar.png"), [64 + (player.health - 100)/1.5625, 8]))     
    else:
        Death.update("You Died")
    #print(player.jumping, player.speedy)
    for Collision in Bros:
        for wall in walls:
            Collision.wallTileCollide(wall)    
        for wall in walls:
            Collision.wallTileCollide(wall)
        for Charter in Bros:
            Collision.charterChaterCollide(Charter)
    screen.fill((255, 255, 255))
    for Bro in Bros:
        screen.blit(Bro.image, Bro.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    screen.blit(Death.image, Death.rect)
    screen.blit(Healthbar.image, Healthbar.rect)
    pygame.display.flip()
    Clock.tick(60);
   
    #print(Clock.get_fps())


