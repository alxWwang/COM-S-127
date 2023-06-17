import random


def excersise1a(a,b,list1):
    aB = a+b

    list1.append(a) #0
    list1.append(b) #1
    list1.append(aB)#2
    
    print(list1)
    return list1
    


def excercise1b (list1,list2):
    for i in range(0,list1[2]):
        i = random.randint(list1[0],list1[2])
        list2.append(i)  
    return list2

list3=[]
list4 = []

excersise1a(5,6,list3)
print(excercise1b(list3,list4))