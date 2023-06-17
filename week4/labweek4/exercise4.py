import math


#angle = math.atan((m1 – m2) / (1 + m1 * m2))

m1 = float(input(" input slope value"))
m2 = float(input(" input slope value"))


#perlu ini buat ketentuannya gaboleh dibagi 0, brati kalo bginian biasain nyari pengecualiannya dl
if m1*m2 == -1:
    print("The lines with slopes {0}, and {1} is perpendicular".format(m1,m2))
    quit()

angle = math.atan((m1 - m2) / (1 + m1 * m2))
angle *= 180/math.pi

if m1 == m2 :
    print("The lines with slopes {0}, and {1} is parallel".format(m1,m2))

elif angle == 90 :
    print("The lines with slopes {0}, and {1} is perpendicular".format(m1,m2))
else :
    print("The lines with slopes {0}, and {1} is {2}".format(m1,m2,angle))