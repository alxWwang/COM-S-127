def swapFn(a,b):
    c = a
    a =b
    b = c
    
    return a,b

masuk = int(input("Enter an integer: "))
masuk2 = int(input("Enter an integer: "))

res = swapFn(masuk,masuk2)

print("The Swapped values are",res)