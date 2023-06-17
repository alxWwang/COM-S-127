def answerTest(x) :
    if x == "A" or  x == "B" or  x == "a" or  x == "b" :
        return True
    else:
        return False
        



for i in range (5) :
    celFar = input("A. celcius \nB. farenheit \n\n")
    if answerTest(celFar) == True :
        break
    else :
        print("that is not a valid answer")

print("iso su")