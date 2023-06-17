def sortir(a,b,c):
    res1 =0
    res2 =0
    res3 =0
    if a < b and a<c:
        res1 = a
    if a < b and a>c:
        res2 = a 
    if a> b and a<c:
        res2 = a
    if a>b and a>c:
        res3 = a
    
    if b < a and b<c:
        res1 = b
    if b < a and b>c:
        res2 = b
    if b > a and b<c:
        res2 = b
    if b>a and b>c:
        res3 = b
    
    if c < a and c<b:
        res1 = c
    if c < a and c > b:
        res2 = c
    if c > a and c < b:
        res2 = c
    if c>a and c>b:
        res3 = c
        
    return res1,res2,res3
        

masuk = int(input("Enter an integer: "))
masuk2 = int(input("Enter an integer: "))
masuk3 = int(input("Enter an integer: "))

res = sortir(masuk, masuk2, masuk3)

print("The sorted values are :",res)