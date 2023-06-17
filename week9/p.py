animal = input('animal :')
list1 = []

for i in range(len(animal)):
    x =  int(input("huruf berapa :"))
    while x >= len(animal):
        print()
        x = int(input('huruf berapa :'))        
        break
    
    list1.append(animal[x])

for i in list1:
    print(i, end ="")