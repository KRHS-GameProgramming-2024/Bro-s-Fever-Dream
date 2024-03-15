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
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    levX = int(levX+1)
                print(str(world)+str(levX)+str(levY)+ ".lvl")
                
        screen.fill((97, 164, 229))
        for wall in walls:
            screen.blit(wall.image, wall.rect)
        pygame.display.flip()
        clock.tick(60)
    
