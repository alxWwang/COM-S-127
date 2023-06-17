print("calculate whtvr u want")

def calcTest(x) :
    if x == "+" or  x == "-" or  x == "*" or  x == "/" :
        return True
    else:
        return False
    
def numberTest(x) :
    try :
        float(x)
        return True
    except ValueError:
        return False



for z in range (5) :
    num = input("enter a number :")        
    if numberTest(num) :
        break
    else :
        print("Enter a valid number")

numbers = float(num)


for y in range (5) :
    option = input(
    "+\n"
    "-\n"
    "*\n"
    "/\n\n")
    if calcTest (option) == True :
        break
    else :
        print("Try a valid calculation")
        

for a in range (5) :   
    num2 = input("Please enter another valid number")    
    if numberTest(num2) :
        break
    else :
        print("Enter a valid number")
        
numbers2 = float(num2)


if option == "+" :
    res = (numbers + numbers2)
elif option == "-" :
    res = (numbers - numbers2)
elif option == "*" :
    res= (numbers * numbers2)
elif option == "/" :
    res = (numbers//numbers2)
    
print(numbers, option, numbers2, "=",res)