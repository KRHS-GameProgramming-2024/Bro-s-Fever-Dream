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
m1=10
m2=50
v10=4
v20=-5

def elasticCollision(m1=1, m2=2, v10=3, v20=4):
    ke10=(m1*v10^2)/2
    ke20=(m2*v20^2)/2
    p10=m1*v10
    p20=m2*v20
    v11=(2 * m2 * v20 + (m1 - m2) * v10)/(m1 + m2) + v10 - v20
    v21=(2 * m1 * v10 + (m2 - m1) * v20)/(m2 + m1) + v20 - v10
    # ~ ke10+ke20=ke11+ke21
    # ~ p10+p20=p11+p21
    #print(str(v11) + " is first velo" + "\n" + str(v21) + " is second velo")
    return [
        v11,
        m1,
        v21,
        m2]
    
    
    
def inelasticCollision(m1=1, m2=2, v10=3, v20=4):
    v11=(m1*v10+m2*v20)/(m1+m2)
    v21=v11
    print(v11)
    return [
        v11,
        m1,
        v21,
        m2]

# ~ print(inelasticCollision(m1, m2, v10, v20))
# ~ n1=inelasticCollision(m1, m2, v10, v20)
# ~ v11=n1[0]
# ~ m1=n1[1]
# ~ v21=n1[2]
# ~ m2=n1[3]
# ~ print(v11, "veolocity object one after collision")
# ~ print(m1, "mass object one after collision")
# ~ print(v21, "velocity object two after collision")
# ~ print(m2, "mass object two after collision")

# ~ All this stuff works, inelastic collisions are good

# ~ print(elasticCollision(m1, m2, v10, v20))
# ~ v11=n1[0]
# ~ m1=n1[1]
# ~ v21=n1[2]
# ~ m2=n1[3]
# ~ print(v11, "veolocity object one after collision")
# ~ print(m1, "mass object one after collision")
# ~ print(v21, "velocity object two after collision")
# ~ print(m2, "mass object two after collision")

