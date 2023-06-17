def main():
    inpt1 = int(input("Input an integer"))
    decToBin(inpt1)
    
def decToBin(num):
    if num > 1:
        decToBin(num // 2)
    print(num % 2, end = '')

main()