def fnListN(n):
    global z
    
    z = int(input("How much do you want :"))
    for i in range(z) : # ini buat ngulang teros
        inpt = input("enter number")
        x = int(inpt)
        n.append(x)
        
def fnSquare(n):
    for i in nNumbers:
        p = pow(i,2)
        n.append(p)

nNumbers= []
fnListN(nNumbers)
print(nNumbers)


nSquared= []
fnSquare(nSquared)
print(nSquared)