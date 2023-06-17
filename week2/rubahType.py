
#INI CARA MILIH TIPE DATA NE, DITAMBAHI DEPANE INT FLOAT ATAU STR

from xmlrpc.client import boolean


string = input("jajal huruf :")
print(type(string))

#INI NGRUBAH JADI INT
stringINT = int(input("jajal keki angka :"))
print(type(stringINT))

#INI NGRUBAH JADI FLOAT
stringFLOAT = float(input("jajal keki angka PAKE KOMA mneh :"))
print(type(stringFLOAT))

stringBOOL = bool(input("tulisen True or False :"))
#hasilnya pasti true kecuali 0
print(stringBOOL)

print(string)


#type check example
name = input("enter a name :")
salary = input("enter salary :")
company = input("input company :")

print("type of name", type(name))
print("type of salary", type(salary))
print("type of company", type(company))


#type conversion
number1 = int(input("enter some number"))
number2 = int(input("enter some number again"))
sum = number1 + number2

print(sum)

numberX = float(input("enter some number"))
numberY = float(input("enter some number again"))
print(numberX,type(numberX),numberY,type(numberY))

sum = number1 + number2

print(sum)