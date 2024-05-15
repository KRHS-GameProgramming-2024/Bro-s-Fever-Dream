import math, pygame, sys, random
#enemies
from Gravestone import *
from Enemy import *
    #air
    
    #earth
from GoopyGlob import *    
    #fire
    
    #water
    
#friendlies
    #player
from Bro import*
    #NPCs

#weapons
from Weapons import *
    #daggers
from SoupLadle import *
    #swords
    
    #ranged

#action files
    #interfaces
from HealthBar import *
from Hud import *
    #world load and generation
from Walls import*
from LevelLoader import *
from JukeBox import *








pygame.init()

size = [1024,768]
screen = pygame.display.set_mode(size)

backgrounds = [pygame.image.load("Backgrounds/Cavebackground1.jpg"),
pygame.image.load("Backgrounds/Cavebackground2.jpg"),
pygame.image.load("Backgrounds/Cavebackground3.jpg"),
pygame.image.load("Backgrounds/SurfaceNight.jpg"),
pygame.image.load("Backgrounds/SurfaceDawn+Dusk.jpg"),
pygame.image.load("Backgrounds/SurfaceDay.png")
]

Clock = pygame.time.Clock();

Stones = []
GraveCount = 0

world = 1
levX = 0
levY = 0
LevelChange = False

level = loadLevel(str(world)+str(levX)+str(levY)+ ".lvl")
walls = level[0]
GoopyGlobs = level[1]
counter = 0
Death = ImageHud(pygame.image.load("Bro/Images/YouDied.png"), [1024/2, 768/2])
Health = Hud("Health: ", [500,500])
Healthbar = ImageHud(pygame.image.load("Bro/Images/HealthBar.png"), [500,500])

music(1)

player = Bro(5, [0,0], [1024/2, 768/2])
Bros = [player]
weaponsActive = []
def use(self, direction):
    if using == True:
        weaponsActive += self.equipped
        player.equipped.animate()
        using = False
        print("see soupp ladle if nothing else happened.")
        
while True:
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[2]:
                print("mouse click works")
                weaponsActive += [SoupLadle(player.rect.center)]
                print("see soup ladle if nothing else happened.")

    #print(event.button)
    
                
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

    # ~ elif event.key == pygame.K_1:
            # ~ world = 1
            # ~ levX = 0
            # ~ levY = 0

    # ~ elif event.key == pygame.K_2:
            # ~ world = 2
            # ~ levX = 0
            # ~ levY = 0

    # ~ elif event.key == pygame.K_3:
            # ~ world = 3
            # ~ levX = 0
            # ~ levY = 0

    if LevelChange == True:
        try:
            level = loadLevel(str(world)+str(levX)+str(levY)+ ".lvl")
            walls = level[0]
            GoopyGlobs = level[1]
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
        #Bros += [GoopyGlob()]
        print("go")
    for Charter in Bros:
        if Charter.kind == "Bro":
            Charter.update(size)
        else:
            Charter.update(size, Bros[0].rect.x)
    for Charter in GoopyGlobs:
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
        player.living = False
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
        for GoopyGlob in GoopyGlobs:
            Collision.charterChaterCollide(GoopyGlob)
        for Charter in Bros:
            Collision.charterChaterCollide(Charter)
            for weapon in weaponsActive:
                Collision.charterWeaponCollide(weapon)
    for Collision in GoopyGlobs:
        for wall in walls:
            Collision.wallTileCollide(wall)
        for Charter in GoopyGlobs:
            Collision.charterChaterCollide(Charter)
            for weapon in weaponsActive:
                Collision.charterWeaponCollide(weapon)
    for wall in walls:
        for Grave in Stones:
            Grave.wallTileCollide(wall)
    screen.blit(backgrounds[0], [0,0])
    for Bro in Bros:
        if Bro.kind == "Bro":
            if player.living == True:
                screen.blit(Bro.image, Bro.rect)
        # ~ if Bro.kind == "GoopyGlob":
            # ~ screen.blit(Bro.image, Bro.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    for GoopyGlob in GoopyGlobs:
        screen.blit(GoopyGlob.image, GoopyGlob.rect)
    for Grave in Stones:
        screen.blit(Grave.image, Grave.rect)
        player.rect = Grave.rect

    for weapon in weaponsActive:
        screen.blit(weapon.image, weapon.rect)
        weapon.update(player)
        if weapon.kind == "Dagger": 
            # ~ print("ok so we got the kind now")
            if weapon.change > 6: 
                # ~ print("dawg what")
                weaponsActive.remove(weapon)
    screen.blit(Death.image, Death.rect)
    screen.blit(Healthbar.image, Healthbar.rect)
    pygame.display.flip()
    Clock.tick(60);
   
    #print(Clock.get_fps())
#
