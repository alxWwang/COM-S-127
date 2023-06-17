def userinput():
    inpt1 = int(input("Enter an int :"))
    inpt2 = int(input("Enter an int :"))
    
    res = inpt1 + inpt2
    return res

def countOddDigits(userinput):
    userinputStr = str(userinput)
    counter = 0 
    
    print()
    print(userinputStr)
    
    for i in userinputStr:
        iInt = int(i)
        if iInt %2 == 1:
            counter += 1
    return counter

def countOddDigits2(num): 
    oddCount = 0 
    while num > 0: 
        if num % 2 == 1: 
            oddCount += 1 
        num //= 10 
    return oddCount
    
def main():
    userinputX = userinput()
    print(countOddDigits(userinputX))
    print(countOddDigits2(userinputX))
    
if __name__ == "__main__":
    main()