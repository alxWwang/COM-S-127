import random
def x():
    global strength
    global agil
    print() #ini buat graphic nya mau dikasi apa
    rand = random.randint(1,8)
    strength = 3
    agil= 0
    
    if rand == 2 :
        print("A Wild Diglett appeared!!!")
        strength = 3
        agil = 1

        
    if rand == 5 :
        print("A Wild Ratatta appeared!!! ")
    if rand == 7 :
        print("A Wild Pidgey appeared!!! ")
        
        
        
x()

print(strength)