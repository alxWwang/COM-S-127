#m = (y2 – y1) / (x2 – x1)

x1 = int(input("input x1 "))
y1 = int(input("input y1 "))

x2 = int(input("input x2 "))
y2 = int(input("input y2 "))



if(x2-x1) == 0:
    print("The line described by points ({0},{1}) and ({2},{3}) is ".format(x1,y1,x2,y2),"vertical.")
    quit()
elif(y2 - y1) == 0 :
    print("The line described by points ({0},{1}) and ({2},{3}) is ".format(x1,y1,x2,y2),"horizontal.")
else :
    m = (y2 - y1) / (x2 - x1)
    print("The line described by points ({0},{1}) and ({2},{3}) is ".format(x1,y1,x2,y2), m,".")

