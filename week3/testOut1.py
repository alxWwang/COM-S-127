
tes = int(input("mau berapa "))
tes += 1
print()
##sampe sini kita dapet list angka ne berapa aja

number = list(range(1, tes))
number.reverse()
print(number)


#loop dah bener jangan diubah ubah
for z in number : #kalo fungsine buat ngurangi, sama ngulangi print an e
    for y in number :
        print(y, end = " ") #ini fungsinya buat ngeprint 1 line doang
        
    tes -= 1
    number = list(range(1, tes))
    number.reverse()

    
    print()


    