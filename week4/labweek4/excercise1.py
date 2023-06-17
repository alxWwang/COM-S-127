leng = int(input("Input the length "))
heig = int(input("Input the height "))



if leng == heig :
    print("the perimeter is a square with perimeter {0}".format(2 * (leng + heig)))
else :
   print("the perimeter is a rectangle with perimeter {0}".format(2 * (leng + heig)))