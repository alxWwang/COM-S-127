counter1 = int(input("Enter an integer :"))
reset = int(input("Enter an integer :"))

while counter1>0 :
    counter2 = reset #counter 2 dibalikin ke awal lagi
    while counter2 >0:
        print(counter1*counter2," ", end= "") #ini print an linenya
        counter2-=1 # ini buat decrement kesamping
    print() #habis ngeprint di enter
    counter1-=1 #ini buat kebawah 