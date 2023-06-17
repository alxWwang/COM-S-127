#Nicholas Alexander Wang          9-8-2022
# Lab Week 3 - Exercise #3
import math


a = int(input("input A"))
b = int(input("input B"))
c = int(input("input C"))

if c == 0 or a == c :
    print("enter a different number!")
    quit()


sumAbc = (a+b+c)

modAbc = a%c

mulAbc1 = (a*b)/c
mulAbc2 = c/mulAbc1

average = (a+b+c)/3


print(sumAbc,modAbc, mulAbc2,average)

print("the sum of a,b,c is ", sumAbc)
print("tme modulus of a mod c is ", modAbc)
print("the result of the calculation is ", mulAbc2)
print("the average of the numbers is ",average)

