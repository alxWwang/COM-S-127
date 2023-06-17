'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


'''
x = int(input("input a number :"))

xStr = str(x)
xList = list(xStr)
xListR = list(reversed(xList))

pal = 0
noPal = 0

for i in range(len(xList)):
    if xList[i] == xListR [i] :
        pal += 1
    else:
        noPal += 1
        
if noPal > 0:
    print("this is not a palindrome")
else:
    print("this is a palindrome") 