import math, pygame, sys, random
from LevelLoader import *
from Bro import*
from Walls import*
from Enemy import *
from GoopyGlob import *
from JukeBox import *

pygame.init()

size = [1024,768]
screen = pygame.display.set_mode(size)

Clock = pygame.time.Clock();

tiles = loadLevel("levels/Template.lvl")
walls = tiles
counter = 0
walls = tiles

music(1)

player = Bro(8, [0,0], [1024/2, 768/2])
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
    
    counter += 1
    #print(counter)
    if counter % 300 == 0:
        #Bros += [GloopyGlob()]
        print("go")
    for Charter in Bros:
        if Charter.kind == "Bro":
            Charter.update(size)
        else:
            Charter.update(size, Bros[0].rect.x)
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
    pygame.display.flip()
    Clock.tick(60);
   
    #print(Clock.get_fps())


