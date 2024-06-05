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
screen = pygame.Surface(size)
window = pygame.display.set_mode(size, flags = pygame.RESIZABLE)

backgrounds = [pygame.image.load("Backgrounds/Cavebackground1.jpg"),
pygame.image.load("Backgrounds/Cavebackground2.jpg"),
pygame.image.load("Backgrounds/Cavebackground3.jpg"),
pygame.image.load("Backgrounds/SurfaceNight.jpg"),
pygame.image.load("Backgrounds/SurfaceDawn+Dusk.jpg"),
pygame.image.load("Backgrounds/SurfaceDay.png")
]

Clock = pygame.time.Clock();

RESPAWN = pygame.USEREVENT

# ~ Stones = []
# ~ GraveCount = 0

StartScreen = True
MainGame = False
BareWare = True
Title = False
TitleWait = False
Delay1 = True
StartMusic = True
MainMusic = True
Timer = True
MainReload = False

# ~ world = 1
# ~ levX = 0
# ~ levY = 0
# ~ LevelChange = False

# ~ level = loadLevel(str(world)+str(levX)+str(levY)+ ".lvl")
# ~ walls = level[0]
# ~ GoopyGlobs = level[1]
# ~ counter = 0
# ~ Death = ImageHud(pygame.image.load("Bro/Images/YouDied.png"), [1024/2, 768/2])
# ~ Health = Hud("Health: ", [500,500])
# ~ Healthbar = ImageHud(pygame.image.load("Bro/Images/HealthBar.png"), [500,500])


# ~ player = Bro(5, [0,0], [1024/2, 768/2])
# ~ Bros = [player]
# ~ weaponsActive = []
def use(self, direction):
    if using == True:
        weaponsActive += self.equipped
        player.equipped.animate()
        using = False
        #print("see soupp ladle if nothing else happened.")
        
while True:
    while StartScreen == True:
        screen.fill((0,0,0))
        if StartMusic == True:
            music(8)
            StartMusic = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     StartScreen = False
                     MainGame = True
                     MainReload = True
                
        
        
        if Delay1 == True:
            pygame.time.delay(1600)
        
        if TitleWait == True:
            Title = True
        
        if BareWare == False:
            TitleWait = True
        
        if Title == True:
            screen.blit(pygame.image.load("TitleScreen/TitleScreen.png"),[(1024-952)/2, (768-714)/2])
            screen.blit(pygame.image.load("TitleScreen/TitleText.png"), [(1024-929)/2, (768-228)/3])
            Delay1 = False
        
        if BareWare == True:
            screen.blit(pygame.image.load("TitleScreen/BareWareBig.png"),[(1024-120)/2, (768-236)/2])
            BareWare = False
            Delay1 = True
            pygame.time.delay(1000)
        
        width, height = pygame.display.get_surface().get_size()
        width = width/size[0]
        height = height/size[1]
        if width == height:
            window.blit(pygame.transform.scale(screen, [width*size[0], height*size[1]]), [0,0])
        elif width > height:
            window.blit(pygame.transform.scale(screen, [height*size[0], height*size[1]]), [(width-height)*(size[0]/2),0])
        elif width < height:
            window.blit(pygame.transform.scale(screen, [width*size[0], width*size[1]]), [0,(height-width)*(size[1]/2)])
        
        pygame.display.flip()
        Clock.tick(60)
        
    while MainGame == True:
        if MainReload == True:
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


            player = Bro(5, [0,0], [1024/2, 768/2])
            Bros = [player]
            weaponsActive = []
            MainReload = False
            Timer = True
        
        if MainMusic == True:
            music(1)
            MainMusic = False
        prev = (world, levX, levY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == RESPAWN:
                pygame.event.clear(RESPAWN)
                screen.fill((0,0,0))
                StartScreen = True
                MainGame = False
                BareWare = True
                Title = False
                TitleWait = False
                Delay1 = True
                StartMusic = True
                MainMusic = True
                print("!")
            elif event.type == pygame.KEYDOWN:
                #print(event.key)
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("left")
                    player.look("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("right")
                    player.look("right")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.goKey("up")
                    #print(player.jumping, player.speedy)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.goKey("down")
                elif event.key == pygame.K_i or event.key == pygame.K_SPACE:
                    player.goKey("run")
                elif event.key == pygame.K_ESCAPE:
                    sys.exit();
                elif event.key == pygame.K_1:
                    player.weaponSwap(0)
                elif event.key == pygame.K_2:
                    player.weaponSwap(1)
                elif event.key == pygame.K_3:
                    player.weaponSwap(2)
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
                    
                    if player.rect.center[0]>getScaledMouse()[0]:
                        player.look("left")
                    if player.rect.center[0]<getScaledMouse()[0]:
                        player.look("right")
                    #print("mouse click works")
                    weaponsActive += [player.equipped([player.rect.center[0] - 13, player.rect.center[1]])]
                    using = True
                    #print("see soupp ladle if nothing else happened.")

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


        for Charter in Bros:
            if Charter.kind == "Bro":
                if player.living == True:
                    Charter.update(size)
                else:
                    pass
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
        if player.living == False and Timer == True:
            pygame.time.set_timer(RESPAWN, 5000, 1)
            Timer = False
            print("?")
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
            if player.living == True:
                screen.blit(weapon.image, weapon.rect)
                weapon.update(player)
                if weapon.kind == "Dagger": 
                    # ~ print("ok so we got the kind now")
                    if weapon.change > 6: 
                        # ~ print("dawg what")
                        weaponsActive.remove(weapon)
                if weapon.kind == "Popper":
                    if weapon.firing == True:
                        pass
                if weapon.kind == "Boomerang": 
                    # ~ print("ok so we got the kind now")
                    if (weapon.live)/(weapon.timeScaler) > 6: 
                        # ~ print("dawg what")
                        weaponsActive.remove(weapon)
        screen.blit(Death.image, Death.rect)
        screen.blit(Healthbar.image, Healthbar.rect)
        
        
        width, height = pygame.display.get_surface().get_size()
        width = width/size[0]
        height = height/size[1]
        if width == height:
            window.blit(pygame.transform.scale(screen, [width*size[0], height*size[1]]), [0,0])
        elif width > height:
            window.blit(pygame.transform.scale(screen, [height*size[0], height*size[1]]), [(width-height)*(size[0]/2),0])
        elif width < height:
            window.blit(pygame.transform.scale(screen, [width*size[0], width*size[1]]), [0,(height-width)*(size[1]/2)])
            
            
        
        
        pygame.display.flip()
        Clock.tick(60);
       


    #print(Clock.get_fps())
    #
