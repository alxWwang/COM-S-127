def main():
    inpt1 = int(input("Input an integer"))
    binToDex(inpt1)


def binToDex(bin):
    binStr = str(bin)
    val = 0
    for i in binStr:
        i = int(i)
        val = val*2 +i
    print(val)
    

main()