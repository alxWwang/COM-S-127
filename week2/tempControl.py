def isfloat(x) :
    try:
        float(x)
        return True
    except ValueError :
        return False
    
def answerTest(x) :
    if x == "A" or  x == "B" or  x == "a" or  x == "b" :
        return True
    else:
        return False
         

for i in range (5) :
    temprature = input("Whats the temprature :")
    if isfloat (temprature) == True :
        break
    else :
        print("Thats not a number! \n")


        
print("is it in celcius or farenheit :")
tempFloat = float(temprature)


for i in range (5) :
    celFar = input("A. celcius \nB. farenheit \n\n")
    if answerTest(celFar) == True :
        break
    else :
        print("That is not a valid answer!\n")


convCel = tempFloat*9/5+32 
convFar = (tempFloat-32)/9*5 

print()

if celFar == "A"  or celFar == "a":
    
    print("it is", tempFloat, "degrees celcius and it is", convCel,"degrees farenheit")
    if tempFloat <= 18:
        print("it is really cold there")
    elif tempFloat >18 and tempFloat <24 :
        print("the weather is nice")
    else :
        print("damn thats sweaty")
        
elif celFar == "B" or celFar == "b":
    print("it is", tempFloat, "degrees farenheit and it is", convFar, "degrees celcius")
    if tempFloat<= 18*9/5+32  :
        print("it is really cold there")
    elif tempFloat>18*9/5+32 and tempFloat <24*9/5+32   :
        print("the weather is nice")
    else :
        print("damn thats sweaty")
else :
    print("thats not a valid option!")