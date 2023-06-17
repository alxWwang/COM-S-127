

def kali(a,b):
    c = 0
    for i in range(b):
        i = a
        c += i
    return c
        

Int1 = int(input("Input an Integer: "))
Int2 = int(input("Input an Integer: "))
result = kali(Int1, Int2)

print("The product of {0} x {1} = {2}".format(Int1, Int2, result))