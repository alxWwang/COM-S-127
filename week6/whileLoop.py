x = input("kontol float isinen")

try: #ini apa yang mau dilakukan
    x= float(x)
except :
    print('bedo goblok')
    

num_low = 0
num_high = 100

while True :
    num = input("enter an integer")
    try :
        num = int(num)
    except :
        print("change your input")
    if num<num_low or num>num_high :
        print("enter a valid number")
        continue
    break

print("your input is", num)
print("jadi ini begini ges")
