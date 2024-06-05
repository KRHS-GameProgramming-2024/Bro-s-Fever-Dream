from math import * 
#                               **ANYBODY WORKING ON THIS DOCUMENT, READ BELOW**    
#For inelastic cololisions
#momentum formula, as momentum is convserved in all linear collisions. There wil be no angular collisions becasue I am not adept with those.
#   m(10)v(10)+m(20)v(10)=m(1+2)v(1)
#we do not need kinetic energy for e\inelastic collisions. 
#
#For elastic collisions:
#momentum formula, as momentum is conserved in all linear collisions
#   m(10)v(10)+m(20)v(20)=m(11)v(11)=m(21)v(21)
#Kinetic energy formula, as kinetic energy is conserved ni elastic collisions. this is important because both velocities will change after the collision and we need to form a system of equations to find both.
#If you chgange anything, one must substitute into the other. Good Luck.
#   K=(mv^2)/2
#Kinetic energy must transfer between objects, which means that all energy levels will be diffferent before and after the collision.
#
#you will know the math works if, when you run a inelastic collision, the objects both have the same velociy after
#                                              an  elastic collision, the objects have separate velocities, not necessarily traveling antiparallel.
#               have fun lmao I had to google it to find out
mass1=10
mass2=50
initialVelocity1=4
initialVelocity2=-5

def elasticCollision(mass1=1, mass2=2, initialVelocity1=3, initialVelocity2=4):
    # ~ ke10=(mass1*initialVelocity1**2)/2
    # ~ ke20=(mass2*initialVelocity2**2)/2
    # ~ p10=mass1*initialVelocity1
    # ~ p20=mass2*initialVelocity2
    
    finalVelocity1=(2 * mass2 * initialVelocity2 + (mass1 - mass2) * initialVelocity1)/(mass1 + mass2) + initialVelocity1 - initialVelocity2
    finalVelocity2=(2 * mass1 * initialVelocity1 + (mass2 - mass1) * initialVelocity2)/(mass2 + mass1) + initialVelocity2 - initialVelocity1
    # ~ ke10+ke20=ke11+ke21
    # ~ p10+p20=p11+p21
    #print(str(finalVelocity1) + " is first velo" + "\n" + str(finalVelocity2) + " is second velo")
    return finalVelocity2
    
    
    
def inelasticCollision(mass1=1, mass2=2, initialVelocity1=3, initialVelocity2=4):
    finalVelocity1=(mass1*initialVelocity1+mass2*initialVelocity2)/(mass1+mass2)
    finalVelocity2=finalVelocity1
    #print(finalVelocity1)
    return finalVelocity2

# ~ print(inelasticCollision(mass1, mass2, initialVelocity1, initialVelocity2))
# ~ n1=inelasticCollision(mass1, mass2, initialVelocity1, initialVelocity2)
# ~ finalVelocity1=n1[0]
# ~ mass1=n1[1]
# ~ finalVelocity2=n1[2]
# ~ mass2=n1[3]
# ~ print(finalVelocity1, "veolocity object one after collision")
# ~ print(mass1, "mass object one after collision")
# ~ print(finalVelocity2, "velocity object two after collision")
# ~ print(mass2, "mass object two after collision")

# ~ All this stuff works, inelastic collisions are good

# ~ print(elasticCollision(mass1, mass2, initialVelocity1, initialVelocity2))
# ~ finalVelocity1=n1[0]
# ~ mass1=n1[1]
# ~ finalVelocity2=n1[2]
# ~ mass2=n1[3]
# ~ print(finalVelocity1, "veolocity object one after collision")
# ~ print(mass1, "mass object one after collision")
# ~ print(finalVelocity2, "velocity object two after collision")
# ~ print(mass2, "mass object two after collision")

