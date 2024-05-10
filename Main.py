import math, pygame, sys, random
from LevelLoader import *
from Bro import*
from Walls import*
from Enemy import *
from GoopyGlob import *
from Gravestone import *
from JukeBox import *
from Hud import *
from HealthBar import *

pygame.init()

size = [1024,768]
screen = pygame.display.set_mode(size)



Clock = pygame.time.Clock();




mode = "screen"

while True:
    while mode == "screen":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_SPACE:
                    mode = "game"
        
        timage = pygame.image.load("temporary.png")
        trect = timage.get_rect()
            
        screen.blit(timage, trect)
            
        pygame.display.flip()
        Clock.tick(60)

    
    backgrounds = [pygame.image.load("Backgrounds/Cavebackground1.jpg"),
    pygame.image.load("Backgrounds/Cavebackground2.jpg"),
    pygame.image.load("Backgrounds/Cavebackground3.jpg"),
    pygame.image.load("Backgrounds/SurfaceNight.jpg"),
    pygame.image.load("Backgrounds/SurfaceDawn+Dusk.jpg"),
    pygame.image.load("Backgrounds/SurfaceDay.png")
    ]
    
    Stones = []
    GraveCount = 0

    world = 1
    levX = 0
    levY = 0
    LevelChange = False

    tiles = loadLevel(str(world)+str(levX)+str(levY)+ ".lvl")
    walls = tiles
    counter = 0
    walls = tiles
    Death = ImageHud(pygame.image.load("Bro/Images/YouDied.png"), [1024/2, 768/2])
    Health = Hud("Health: ", [500,500])
    Healthbar = ImageHud(pygame.image.load("Bro/Images/HealthBar.png"), [500,500])
    PlayerLiving = True

    music(1)

    player = Bro(5, [0,0], [1024/2, 768/2])
    Bros = [player]
    
    
    while mode == "game":
        
        prev = (world, levX, levY)
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
        
       
                
                
                
        if player.rect[0] > 1024:
                levY = int(levY+1)
                player.rect[0] = 0
                LevelChange = True
                    
        elif player.rect[0] < 0:
                if levY > 0:
                    levY = int(levY-1)
                player.rect[0] = 1024
                LevelChange = True

        elif player.rect[1] < 0:
                if levX > 0:
                    levX = int(levX-1)
                player.rect[1] = 768
                LevelChange = True

        elif player.rect[1] > 768:
                levX = int(levX+1)
                player.rect[1] = 0
                LevelChange = True

       

        if LevelChange == True:
            try:
                walls = loadLevel(str(world)+str(levX)+str(levY)+ ".lvl")
                LevelChange = False
            except:
                world, levX, levY = prev
        #print(str(world)+str(levX)+str(levY)+ ".lvl")       
            
        # ~ if world == 1:
            # ~ bg = Background("Cavebackground2.jpg")
        # ~ if world == 2:
            # ~ bg = Background("SurfaceNight.jpg")
        # ~ elif world == 3:
            # ~ bg = Background("Cavebackground3.jpg")

        counter += 1
        #print(counter)
        if counter % 300 == 0:
            Bros += [GoopyGlob()]
            print("go")
        for Charter in Bros:
            if Charter.kind == "Bro":
                Charter.update(size)
            else:
                Charter.update(size, Bros[0].rect.x)
        for Grave in Stones:
            Grave.update()
        #Health = Hud("Health: ", [player.rect.center[0] - 90, player.rect.center[1] - 70])
        Health.update(player.health)

        Healthbar = ImageHud(pygame.image.load("Bro/Images/HealthBar.png"), [player.rect.center[0] - 30, player.rect.center[1] - 55])
        if player.health > 0:
            Healthbar.update(pygame.transform.scale(pygame.image.load("Bro/Images/HealthBar.png"), [64 + (player.health - 100)/1.5625, 8]))     
        else:
            Death.update(pygame.image.load("Bro/Images/YouDied.png"))
            PlayerLiving = False
            if GraveCount == 0:
                Stones += [Gravestone(player.rect.center)]
                GraveCount = 1
            else:
                pass
        #print(player.jumping, player.speedy)
        for Collision in Bros:
            for wall in walls:
                Collision.wallTileCollide(wall)    
            for wall in walls:
                Collision.wallTileCollide(wall)
            for Charter in Bros:
                Collision.charterChaterCollide(Charter)
        for wall in walls:
            for Grave in Stones:
                Grave.wallTileCollide(wall)
        
        screen.blit(backgrounds[0], [0,0])
        for Bro in Bros:
            if Bro.kind == "Bro":
                if PlayerLiving == True:
                    screen.blit(Bro.image, Bro.rect)
            if Bro.kind == "GoopyGlob":
                screen.blit(Bro.image, Bro.rect)
        for wall in walls:
            screen.blit(wall.image, wall.rect)
        for Grave in Stones:
            screen.blit(Grave.image, Grave.rect)
        screen.blit(Death.image, Death.rect)
        screen.blit(Healthbar.image, Healthbar.rect)
        pygame.display.flip()
        Clock.tick(60);
       
        #print(Clock.get_fps())


