#y = a * x ** 2 + b * x + c

a = int(input("input a value"))
b = int(input("input b value"))
c = int(input("input c value"))
print()
x = int(input("input x point"))
y = int(input("input y point"))


if y == a * (x ** 2) + b * x + c :
    print("the point ({0},{1}) sits on the parabola described by y = ".format(x,y),a,"*x**2 + ",b," *x +",c)
else :
    print("the point ({0},{1}) is not on the parabola described by ".format(x,y), a, "*x**2 + ",b," *x +",c)
