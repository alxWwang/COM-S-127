# <Nicholas Alexander Wang>             <10 Oct 202>
# <Assignment 4>

import random


#CombatFunctions
def combat(x):
    global turnA
    global humanInput
    global healthPower
    global humanStrength
    global humanHealth
    global gameOver
    global engaged
    global current_room
    global winLose
    turnA = 0
    comp = x
    winLose = 3
    engaged = 0
    
    
    while winLose == 3 :
        if turnA == 0 : #Human Turn
                print("========================================================")
                print("This is your Turn")
                print("Your HP is", humanHealth)
                print("Your Strength is", humanStrength)
                print()
                print("Attack [a]")
                if current_room != 6:
                    print("Flee [b]")
                humanInput = input("")
                
                while humanInput != "a" and humanInput != "b": #ini somehow bisa aku juga ga paham
                    if current_room == 6 and humanInput == "b":
                        print("This is not a valid input")
                    humanInput = input("")
                
                randHum = random.randint(0,humanAgility)
                randCom = random.randint(0,agility)
        
                if humanInput == "a":
                    if randHum < randCom :
                        print("The attack misses...")
                        print()
                        turnA += 1 
                        
                    elif randHum >= randCom:
                        print("The attack hits!!")
                        print()
                        healthPower -= humanStrength
                        turnA += 1
                if humanInput == "b" and current_room != 6:
                        print("The Human has Fleed!!!")
                        winLose = 2
                        break
                             
        if turnA == 1 : #Computer Turn
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
                        turnA -= 1
                        
                elif randHum <= randCom:
                        print("The {0}'s attack hits!!".format(comp))
                        humanHealth-=strength
                        turnA -= 1
        if healthPower <= 0 :
                    print("========================================================")                
                    print("The Human Has Won!")
                    print("========================================================")
                    winLose = 1
                    engaged = True
                    break
        if humanHealth <= 0 :
                    print("========================================================")
                    print("Oh no, the {0} won!".format(comp))
                    print("========================================================")
                    print()
                    print("Thanks for Playing!!!")
                    print()
                    
                    if humanHealth < 0:
                        humanHealth = 0
                    
                    print("You have collected {0} Gold".format(gulden))
                    print("You have {0} Health".format(humanHealth))
                    winLose = 0
                    engaged = True
                    gameOver = True
                    break
        
        else :
            continue
        
    return winLose, engaged
             
def enemy01():
    global strength
    global agility
    global healthPower
    global current_room
    global winLose
    global engaged
    
    print() #ini buat graphic nya mau dikasi apa
    
    if current_room == 6:
        print("The Final boss Mewtwo has appeared!!!")
        healthPower = 50
        strength = 30
        agility = 4
        
        print("Health : ", healthPower)
        print("Strength : ",strength)
        print("Agility : ",agility)
        
        combat("Mewtwo")
    else :
        rand = random.randint(1,5)
        if rand == 1 :
            print("A Wild Diglett appeared!!!")
            healthPower = 30
            strength = 15
            agility = 3
            
            print("Health : ", healthPower)
            print("Strength : ",strength)
            print("Agility : ",agility)
            
            combat("Diglett")
            
            
        if rand == 3 :
            print("A Wild Ratatta appeared!!! ")
            healthPower = 20
            strength = 15
            agility = 5
            
                    
            print("Health : ", healthPower)
            print("Strength : ",strength)
            print("Agility : ",agility)
            
            combat("Ratatta")
            
            
        if rand == 5 :
            print("A Wild Pidgey appeared!!! ")
            healthPower = 15
            strength = 20
            agility = 4
            
                    
            print("Health : ", healthPower)
            print("Strength : ",strength)
            print("Agility : ",agility)
            
            combat("Pidgey")          
    return winLose
#ItemFunctions   
def shop():
    global healthBars
    global redbull
    global bangEn
    global cheetos
    global whisky
    global gulden
    

    print("Welcome to the Tavern!!")
    
    
    print("You have {0} much money".format(gulden))
    print("Here is the list of items that we have:")
    print("1. Health bars")
    print("2. RedBull")
    print("3. Bang energy")
    print("4. Cheetos")
    print("5. Whisky")
    print()
    

        
    while True:
        x = input("Select or [q]uit : ")
        print()
        while x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "q":
            x = input("Select a valid answer")
        
        if x == "q":
            print()
            print("Thankyou for your purchase!!")
            print()
            break

        x = int(x)
        
        if x == 1 :
            print("That would be 10 Guldens")
            print()
            if gulden < 10 :
                print("That is not enough money")
            else :
                print("Thankyou for your purchase")
                gulden -= 10
                healthBars +=1
                
        if x == 2 :
            print("That would be 5 Guldens")
            print()
            if gulden < 5 :
                print("That is not enough money")
            else :
                print("Thankyou for your purchase")
                gulden -= 5
                redbull += 1
        if x == 3 :
            print("That would be 5 Guldens")
            print()
            if gulden <3 :
                print("That is not enough Money")
            else :
                print("Thankyou for your purchase")
                gulden -=3
                bangEn += 1
        if x == 4 :
            print("That would be 2 Guldens")
            print()
            if gulden <4:
                print("That is not enough money")
            else :
                print("Thankyou for your purchase")
                gulden -=4
                cheetos += 1
        if x == 5 :
            print("That would be 50 Guldens")
            print()
            if gulden <5 :
                print("That is no enough money")
            else :
                print("Thankyou for your purchase")
                gulden -= 5
                whisky += 1         
def items():
    global healthBars
    global redbull
    global bangEn
    global cheetos
    global whisky
    global humanHealth
    global humanAgility
    global gulden
    
    p = 0
    print("Here is the list of your items")
    if healthBars > 0 :
        print(healthBars,"xHealth bars [1]")
        p = 1
    if redbull>0:
        print(redbull, "xRedbull[2]")
        p = 1
    if bangEn >0:
        print(bangEn,"x Bang Energy[3]")
        p = 1
    if cheetos>0:
        print(cheetos,"x Cheetos[4]")
        p = 1
    if whisky>0:
        print(whisky,"x Whisky[5]")
        p = 1
        
    if p ==0 :
        print("You don't have any items")
    print()

    
    
    while True:
        print("Which one do you want to use, press [q] to quit :")
        x = input("")
        print()
        while x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "q":
            x = input("Select a valid answer")
        
        if x == "q":
            print("ok then bye")
            break

        x = int(x)
        
        if x == 1 :
            if healthBars == 0 :
                print("You have no Health Bars")
            print("This will add your Health")
            print("Do you want to continue?")
            print("[y]es or [n]o")
            y = input('')
            print()
            while y != "y" and y != "x":
                y = input("Please select a valid answer")
            
    
            if y == "y":
                humanHealth += 10
                healthBars -= 1
                
                print("Your health is now", humanHealth)
            else :
                print("Ok please select another option or quit")         
        if x == 2 :
            print("This will add your Agility")
            print("Do you want to continue?")
            print("[y]es or [n]o")
            y = input('')
            print()
            while y != "y" and y != "x":
                y = input("Please select a valid answer")
        
    
            if y == "y":
                humanAgility += 10
                redbull -= 1
                
                print("Your agility is now", humanAgility)
            else :
                healthBars +=1
        if x == 3 :
            print("This will add your Agility")
            print("Do you want to continue?")
            print("[y]es or [n]o")
            y = input('')
            print()
            while y != "y" and y != "x":
                y = input("Please select a valid answer")
            if y == "y":
                humanAgility += 10
                bangEn -= 1
                print("Your agility is now", humanAgility)
            else :
                bangEn +=1
        if x == 4 :
            print("This will add your Health")
            print("Do you want to continue?")
            print("[y]es or [n]o")
            y = input('')
            print()
            while y != "y" and y != "x":
                y = input("Please select a valid answer")
            if y == "y":
                humanHealth += 10
                cheetos -= 1
                print("Your health is now", humanHealth)
            else :
                cheetos
        if x == 5 :
            print("That would be 50 Guldens")
            print()
            if gulden <5 :
                print("That is no enough money")
            else :
                print("Thankyou for your purchase")
                gulden -= 5
                whisky += 1
                
#Rooms               
def shopRoom(): # ini work ngrubah current room
    global current_room
    global gameOver

    x = 0
    while gameOver == False:
        print("================================================================================================================")
        print("Welcome to the dungeon")
        print("Do you want to go to the [s]hop or [a]dventure or do you want to [q]uit?")
        x = input("")
            
        while x != "s" and x != "a" and x != "q":
            print("That is not an option")
            print("Do you want to go to the [s]hop or [a]dventure or do you want to [q]uit")
            x = input("")
            if x == "s" or x =="a" and x == "q" :
                break
        print()
        print("========================================================")
        

        if x == "s":
                shop()
        if x == "a":

            print("Which direction do you want to move")
            print("[n],[e],[s],[w], or [q]uit") 
            whc = input("")   
            while whc != "n" and whc != "e" and whc != "s" and whc != "w" and whc != "q":
                print("That is not a direction")
                whc = input("")
            
            roomMov = whc 

            while gameOver == False :
                if roomMov == "q":
                    break
                if roomMov == "n":
        
                    current_room = 4
     
                    break
                if roomMov == "e":
                
                    current_room = 3
  
                    break
                if roomMov == "s":
                    
                    current_room = 2
         
                    break
                if roomMov == "w":
                  
                    current_room = 1
            
                    break                      
        if x == "q":
                print("Good to see you!!")
                print()
                gameOver= True
                break
            
        return current_room

def room1(goldBrp,var1): #WORKS KONTOL SOME HOW ISO ASU IKI AKU RK PAHAM ANJING
    
    global gameOver
    global winLose
    global gulden
    global current_room
    
    gold = goldBrp
    
    print("Welcome to Room ", current_room)
    
    print("If you want to use your item press [i], if not press any key")
    y = input("")
    if y == "i":
        items()
    
    enemy01()

    if gameOver == False :
        
        if var1 == False and winLose != 2:
            print("The room has", gold, "gold pieces in it...")
            gulden += gold
            print("After taking the gold, you currently have", gulden, "gold pieces in your posession...")
            print()

        elif var1 == True :
            print("You have visited this room before")
            print()

        print("Which direction do you want to move")
        print("[n], [e]") 
        whc = input("")   
        while whc != "n" and whc != "e":
            print("That is not a direction")
            whc = input("")
                
        roomMov = whc               
        if roomMov == "n":
                current_room = 9
                
        if roomMov == "e":
                current_room = 0
                
    var1 = True
    return var1
                
def room2(goldBrp,var1): #WORKS KONTOL SOME HOW ISO ASU IKI AKU RK PAHAM ANJING
    
    global gameOver
    global winLose
    global gulden
    global current_room
    
    gold = goldBrp
    
    print("Welcome to Room ", current_room)
    
    print("If you want to use your item press [i], if not press any key")
    y = input("")
    if y == "i":
        items()
    
    enemy01()
      

        
    if gameOver == False :
        if var1 == False and winLose != 2 :
            print("The room has", gold, "gold pieces in it...")
            gulden += gold
            print("After taking the gold, you currently have", gulden, "gold pieces in your posession...")
            print()

        elif var1 == True :
            print("You have visited this room before")
            print()

        print("Which direction do you want to move")
        print("[n],[e],[s]") 
        whc = input("")   
        while whc != "n" and whc != "e" and whc != "s":
            print("That is not a direction")
            whc = input("")
                
        roomMov = whc  
        if roomMov == "n":

                current_room = 0            
        if roomMov == "e":

                current_room = 8

        if roomMov == "s":

                current_room = 5
        var1 = True
        return var1
             
def room3(goldBrp,var1): #WORKS KONTOL SOME HOW ISO ASU IKI AKU RK PAHAM ANJING
    
    global gameOver
    global winLose
    global gulden
    global current_room

    gold = goldBrp
    
    
    print("Welcome to Room ", current_room)
    
    print("If you want to use your item press [i], if not press any key")
    y = input("")
    if y == "i":
        items()
    
    enemy01()
        
        
    if gameOver == False :
        if var1 == False and winLose != 2 :
            print("The room has", gold, "gold pieces in it...")
            gulden += gold
            print("After taking the gold, you currently have", gulden, "gold pieces in your posession...")
            print()

        elif var1 == True :
            print("You have visited this room before")
            print()

        print("Which direction do you want to move")
        print("[w],[s]") 
        whc = input("")   
        while whc != "s" and whc != "w":
            print("That is not a direction")
            whc = input("")
                
        roomMov = whc               
        if roomMov == "w":

                current_room = 0

        if roomMov == "s":

                current_room = 8
    

    var1 = True
    return var1

def room4(goldBrp,var1): #WORKS KONTOL SOME HOW ISO ASU IKI AKU RK PAHAM ANJING
    
    global gameOver
    global winLose
    global gulden
    global current_room
    
    gold = goldBrp
    
    print("Welcome to Room ", current_room)
    
    print("If you want to use your item press [i], if not press any key")
    y = input("")
    if y == "i":
        items()
    
    enemy01()
    print(winLose)
      
        
    if gameOver == False :
        print(var1)
        if var1 == False and winLose != 2 :
            print("The room has", gold, "gold pieces in it...")
            gulden += gold
            print("After taking the gold, you currently have", gulden, "gold pieces in your posession...")
            print()

        elif var1 == True :
            print("You have visited this room before")
            print()

        print("Which direction do you want to move")
        print("[n],[e],[s]") 
        whc = input("")   
        while whc != "n" and whc != "e" and whc != "s":
            print("That is not a direction")
            whc = input("")
                
        roomMov = whc               
        if roomMov == "n":
                current_room = 7

        if roomMov == "e":

                current_room = 9
        if roomMov == "s":

                current_room = 0
                  
        var1 = True
        return var1
        
def room5(goldBrp,var1): #WORKS KONTOL SOME HOW ISO ASU IKI AKU RK PAHAM ANJING
    
    global gameOver
    global winLose
    global gulden
    global current_room
    
    gold = goldBrp
    
    print("Welcome to Room ", current_room)
    
    print("If you want to use your item press [i], if not press any key")
    y = input("")
    if y == "i":
        items()
    
    enemy01()
      

        
    if gameOver == False :
        if var1 == False and winLose != 2 :
            print("The room has", gold, "gold pieces in it...")
            gulden += gold
            print("After taking the gold, you currently have", gulden, "gold pieces in your posession...")
            print()

        elif var1 == True :
            print("You have visited this room before")
            print()
        
    
        print("Which direction do you want to move")
        print("[n],[e]") 
        whc = input("")   
        while whc != "n" and whc != "e":
            print("That is not a direction")
            whc = input("")
                
        roomMov = whc               
        if roomMov == "n":

                current_room = 2


        if roomMov == "e":

                current_room = 6


        var1 = True
        return var1

def finalRoom(goldBrp,var1): #WORKS KONTOL SOME HOW ISO ASU IKI AKU RK PAHAM ANJING
    
    global gameOver
    global winLose
    global gulden
    global current_room
    
    gold = goldBrp
    
    print("Welcome to the Final Room ")
    
    print("If you want to use your item press [i], if not press any key")
    y = input("")
    if y == "i":
        items()
    
    enemy01()
      

        
    if gameOver == False :
        if var1 == False :
            print("Congratulations!!!")
            print("You have Finished the game!")
            print()

        print("Thanks For playing!!")
        
        print("You have collected {0} Gold".format(gulden))
        print("You have {0} Health".format(humanHealth))
        
        print("[x]") 
        whc = input("")   
        while whc != "x":
            print("That is not an option")
            whc = input("")
                
        roomMov = whc               
        if roomMov == "x":
            gameOver = True
        var1 = True
        return var1

def room7(goldBrp,var1): #WORKS KONTOL SOME HOW ISO ASU IKI AKU RK PAHAM ANJING
    
    global gameOver
    global winLose
    global gulden
    global current_room
    
    gold = goldBrp
    
    print("Welcome to Room ", current_room)
    
    print("If you want to use your item press [i], if not press any key")
    y = input("")
    if y == "i":
        items()
    
    enemy01()

        
    if gameOver == False :
        if var1 == False and winLose != 2 :
            print("The room has", gold, "gold pieces in it...")
            gulden += gold
            print("After taking the gold, you currently have", gulden, "gold pieces in your posession...")
            print()

        elif var1 == True :
            print("You have visited this room before")
            print()

        print("Which direction do you want to move")
        print("[s]") 
        whc = input("")   
        while whc != "s" :
            print("That is not a direction")
            whc = input("")
                
        roomMov = whc               


        if roomMov == "s":

                current_room = 4


        var1 = True
        return var1
        
def room8(goldBrp,var1): #WORKS KONTOL SOME HOW ISO ASU IKI AKU RK PAHAM ANJING
    
    global gameOver
    global winLose
    global gulden
    global current_room
    
    gold = goldBrp
    
    print("Welcome to Room ", current_room)
    
    print("If you want to use your item press [i], if not press any key")
    y = input("")
    if y == "i":
        items()
    
    enemy01()

        
        
    if gameOver == False :
        if var1 == False and winLose != 2 :
            print("The room has", gold, "gold pieces in it...")
            gulden += gold
            print("After taking the gold, you currently have", gulden, "gold pieces in your posession...")
            print()

        elif var1 == True :
            print("You have visited this room before")
            print()

        print("Which direction do you want to move")
        print("[n],[w]") 
        whc = input("")   
        while whc != "n" and whc != "w":
            print("That is not a direction")
            whc = input("")
                
        roomMov = whc               
        if roomMov == "n":

                current_room = 3


        if roomMov == "w":
        
                current_room = 2
        var1 = True
        return var1
        
def room9(goldBrp,var1): #WORKS KONTOL SOME HOW ISO ASU IKI AKU RK PAHAM ANJING
    
    global gameOver
    global winLose
    global gulden
    global current_room
    
    gold = goldBrp
    
    print("Welcome to Room ", current_room)
    
    print("If you want to use your item press [i], if not press any key")
    y = input("")
    if y == "i":
        items()
    
    enemy01()

        
    if gameOver == False :
        if var1 == False and winLose != 2 :
            print("The room has", gold, "gold pieces in it...")
            gulden += gold
            print("After taking the gold, you currently have", gulden, "gold pieces in your posession...")
            print()

        elif var1 == True :
            print("You have visited this room before")
            print()

        print("Which direction do you want to move")
        print("[e],[s]") 
        whc = input("")   
        while whc != "w" and whc != "s" :
            print("That is not a direction")
            whc = input("")
                
        roomMov = whc               

        if roomMov == "w":
            
                current_room = 4

        if roomMov == "s":
            
                current_room = 1
        var1 = True
        return var1


"""
10 oct 2022
 ini to belom dikoreksi arah arah nya, dia output nya ke global current_room, sudah built in check visited. cuman kurang setting movement karena ternyata semuanya beda
 jadi harus dibikin satu satu kontol.
 
 TODO koreksi arah 

 TODO bikin main()
 TODO kasi graphic kalo niat
 
11 oct 2022
 Main nya sudah bisa dibuat sekarang, cuman diawali sama current_room berapa nanti dia link ke berapa pake while loop yang ngereturn current_room
 
 Untuk sekarang current room masih di set ke global, dont know apakah harus berubah, i thin k memang seharusnya dibuat di global kayak gini biar dia bisa ngrubah variabel awal nya.
 
 TODO ngrubah link current room ke proper (Bikin Map)
 TODO bikin main if statement
 TODO buat enemy
 
 PELAJARAN HARI INI : kalo bisa if statement itu inputnya ditaro di luar fungsi pake fungsi lagi, biar lebih gampang dan mudah dimengerti. pake return lebih banyak biar bisa kontrol yang masuk sama yang keluar

12 oct 2022
    Sudah di map 
    main seharusnya sudah work
    TODO bikin piq
    TODO cek variabel sama itung itungan
    TODO bikin Final Stage Room 6:
        - Final Boss
        - Final Score
        - gameOver switch

    
ini list yang harus dicek
- Gold
- items nya dirapiin
- stat player
- rapiin text

17 oct 2022
    SUDAH SELSAI KONTOL
    
    Story - 
    Combat :
        Final boss +
        Final Score +
        Turn +
        Randomizer +
        Health player +
        Pokemon Health +
    
    Shop:
        items +
        Buying +
        Using +
    
    gold :
        roomCheck +
        total gold +
        gold +
        
        
    gamover +
    
    arah +
    
    instruction -
    
    
    TODO bikin story
    TODO bikin Instruction
    TODO pastiin bener smua

 
"""

def main():
    global gulden
    global winLose
    
    global humanStrength
    global humanAgility
    global humanHealth
    
    global healthBars
    global redbull
    global bangEn
    global cheetos
    global whisky

    global current_room
    global gameOver
    
    global visited_1
    global visited_2
    global visited_3
    global visited_4
    global visited_5
    global visited_6
    global visited_7
    global visited_8
    global visited_9
    
    
    
    print("Welcome to Dungeon Crawl...")
    print()

    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: Nicholas Alexander Wang")
    print("[COM S 127 A")
    print()
            
    #MainLoop
    while True :    
        mainMenu = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        gameOver = False
        if mainMenu == "p":
            current_room = 0
            gulden = 0
            
            healthBars = 0
            redbull = 0
            bangEn = 0
            cheetos = 0
            whisky =0
                
            #GameVariables
                        
            gulden = 0 #total gold
            winLose = 3

            #Player stats
            humanStrength = 10
            humanHealth = 50
            humanAgility = 4

            #Items
            healthBars = 0
            redbull = 0
            bangEn = 0
            cheetos = 0 
            whisky = 0
            
            visited_1 = False
            visited_2 = False
            visited_3 = False
            visited_4 = False
            visited_5 = False
            visited_6 = False
            visited_7 = False
            visited_8 = False
            visited_9 = False    
            
            
            while gameOver == False :
                if current_room == 0 :
                    shopRoom()
                if current_room == 1 :
                    print()
                    print("================================================================================================================")
                    visited_1 = room1(10, visited_1)
                if current_room == 2 :
                    print()
                    print("================================================================================================================")
                    visited_2 = room2(20, visited_2)
                if current_room == 3 :
                    print()
                    print("================================================================================================================")
                    print()
                    visited_3 = room3(25, visited_3)
                if current_room == 4 :
                    print()
                    print("================================================================================================================")
                    visited_4 = room4(25, visited_4)
                if current_room == 5 :
                    print()
                    print("================================================================================================================")
                    visited_5 = room5(25, visited_5)
                if current_room == 6 :
                    print()
                    print("================================================================================================================")
                    visited_6 = finalRoom(25, visited_6)   
                if current_room == 7 :
                    print()
                    print("================================================================================================================")
                    visited_7 = room7(25, visited_7)
                if current_room == 8 :
                    print()
                    print("================================================================================================================")
                    visited_8 = room8(25, visited_8)
                if current_room == 9 :
                    print()
                    print("================================================================================================================")
                    visited_9 = room9(25, visited_9)

        if mainMenu == "i":
            print()
            print("Welcome to DungeonCrawl!!")
            print()
            print("You will be dropped in the Shop, Purchase your items, and start your adventure!!")
            print("Beware of monsters in the Dungeon..")
            print("Find the Final Room and fight the Final Boss!!")
            print()
            print("Goodluck!")
            print()
        if mainMenu == "q":
            quit()

if __name__ == "__main__":
    main()