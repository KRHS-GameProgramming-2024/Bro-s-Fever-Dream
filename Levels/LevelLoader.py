import pygame, sys, math
from Walls import *

def loadLevel(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()

    size = 32
    offset = size/2
    tiles = []
    
    newLines = []
    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":
                newLine += c
        newLines += [newLine]
        
    lines = newLines

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                tiles += [Wall([x*size+offset, y*size+offset])]
                
    return tiles
    
if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock();
    
    world = 1
    levX = 0
    levY = 0

    walls = loadLevel(str(world)+str(levX)+str(levY)+ ".lvl")

    size= [1024,768]
    screen = pygame.display.set_mode(size)
    
    while True:
        prev = (world, levX, levY)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    levY = int(levY+1)

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if levY > 0:
                        levY = int(levY-1)

                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if levX > 0:
                        levX = int(levX-1)
                                
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    levX = int(levX+1)
                    
                elif event.key == pygame.K_1:
                    if world >= 1:
                        world = int(world-1)
                        levX = 0
                        levY = 0
                
                elif event.key == pygame.K_2:
                    if world >= 1:
                        world = int(world+1)
                        levX = 0
                        levY = 0

                try:
                    walls = loadLevel(str(world)+str(levX)+str(levY)+ ".lvl")
                except:
                    world, levX, levY = prev
                print(str(world)+str(levX)+str(levY)+ ".lvl")

        screen.fill((97, 164, 229))
        for wall in walls:
            screen.blit(wall.image, wall.rect)
        pygame.display.flip()
        clock.tick(60)
