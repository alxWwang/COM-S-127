import math


#Nicholas Alexander Wang          9-8-2022
# Lab Week 3 - Exercise #1

a = int(input("Enter A value :"))
b = int(input("Enter B value :"))
c = int(input("Enter C value :"))

s = (a + b + c)/2
area1 = s*(s-a)*(s-b)*(s-c)

print(math.sqrt(area1))

