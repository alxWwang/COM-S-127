#Nicholas Alexander Wang          9-8-2022
# Lab Week 3 - Exercise #5

x = input("Enter a subject ")
y = input("Enter a subject ")
z = input("Enter a subject ")
xx = input("Enter a subject ")

print()

a = int(input("enter a grade "))
b = int(input("enter a grade "))
c = int(input("enter a grade "))
d = int(input("enter a grade "))

print()

print ("input class 1 : {0} \n"
       "Grade : {1}".format(x,a)
       )

print ("input class 2 : {0} \n"
       "Grade : {1}".format(y,b)
       )

print ("input class 3 : {0} \n"
       "Grade : {1}".format(z,c)
       )

print ("input class 4 : {0} \n"
       "Grade : {1}".format(xx,d)
       )

average = (a + b + c + d)/4

print("the average of {0}, {1}, {2}, {3} is {4}".format(x,y,z,xx,average))