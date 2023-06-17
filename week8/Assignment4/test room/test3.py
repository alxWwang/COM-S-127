import random
gameOver = False 

gulden = 10
roomAwal =0
combat = 0

humanStrength = 10
humanHealth = 50
humanAgility = 4

        
healthBars = 5
redbull = 1
bangEn = 4
cheetos = 3 
whisky = 1


current_room = 1

visited_shop = False
visited_1 = False



def combat(x):
    global turnA
    global humanInput
    global healthPower
    global humanStrength
    global humanHealth
    global gameOver
    global winLose
    
    turnA = 0
    comp = x
    winLose = 0
    while True :

            if turnA == 0 : #Human Turn
                print("========================================================")
                print("This is your Turn")
                print("Your HP is", humanHealth)
                print("Your Strength is", humanStrength)
                print()
                print("Attack [a]")
                print("Flee [b]")
                humanInput = input("")
                
                while humanInput != "a" and humanInput != "b": #ini somehow bisa aku juga ga paham
                    print("This is not a valid input")
                    humanInput = input("")
                
                randHum = random.randint(0,humanAgility)
                randCom = random.randint(0,agility)
        
                if humanInput == "a":
                    if randHum < randCom :
                        print("The attack misses...")
                        print()
                        
                    elif randHum >= randCom:
                        print("The attack hits!!")
                        print()
                        healthPower -= humanStrength
                if humanInput == "b":
                    print("The Human has Fleed!!!")
                    break
                turnA += 1              
            else : #Computer Turn
                print("========================================================")
                print("This is {0} turn".format(comp))
                print("This {0}'s HP is {1}".format(comp,healthPower))
                print("This {0}'s Strength is {1}".format(comp,strength))
                print()
                
                randHum = random.randint(0,humanAgility)
                randCom = random.randint(0,agility)
                

                if randHum > randCom :
                        print("The attack misses...")
                        print()
                        
                elif randHum <= randCom:
                        print("The {0}'s attack hits!!".format(comp))
                        humanHealth-=strength
                turnA -= 1
                
                
            if healthPower <= 0 :
                    print("========================================================")                
                    print("The Human Has Won!")
                    winLose = 1
                    break
        
            if humanHealth <= 0 :
                    print("========================================================")
                    print("Oh no, the {0} won!".format(comp))
                    winLose = 0
                    break
       
       
def enemy01():
    global strength
    global agility
    global healthPower
    
    print() #ini buat graphic nya mau dikasi apa
    rand = random.randint(1,5)
    strength = 0
    agility = 0
    if rand == 1 :
        print("A Wild Diglett appeared!!!")
        healthPower = 30
        strength = 15
        agility = 3
        
        print("Health : ", healthPower)
        print("Strength : ",strength)
        print("Agility : ",agility)
        
        combat("Diglett")
        print(winLose)
        
    if rand == 3 :
        print("A Wild Ratatta appeared!!! ")
        healthPower = 20
        strength = 15
        agility = 5
        
                
        print("Health : ", healthPower)
        print("Strength : ",strength)
        print("Agility : ",agility)
        
        combat("Ratatta")
        print(winLose)
        
    if rand == 5 :
        print("A Wild Pidgey appeared!!! ")
        healthPower = 15
        strength = 20
        agility = 4
        
                
        print("Health : ", healthPower)
        print("Strength : ",strength)
        print("Agility : ",agility)
        
        combat("Pidgey")
        print(winLose)       
enemy01()