def main():
    print("helo")
    
def printint(y,z):
    x = y+z
    print(x)

if __name__== "__main__" :
    main()
    printint(2,3)
    
    
def passx():
    while True:
        x = input("enter the password number")
        if x == "123":
            break
    print("Password is correct")
    
passx()


def one(a,b):
    c = a + b
    return c

def main():
    data1 = 5
    data2 = 8
    x = one(data1,data2)
    print(x)
    
main()

