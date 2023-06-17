
#Jumlah
x = int(input("isi angka ya :"))
y = int(input("isi angka ya :"))

res = (x+y)

print(res)

#kurang
x = int(input("isi angka ya :"))
y = int(input("isi angka ya :"))

res = (x-y)

print(res)



#kali
x = int(input("isi angka ya :"))
y = int(input("isi angka ya :"))

res = (x*y)

print(res)



#bagi
x = int(input("isi angka ya :"))
y = int(input("isi angka ya :"))

res = (x//y)

print(res)


#exponents
x = int(input("isi angka ya :"))
y = int(input("isi angka ya :"))

res = (x**y)

print(res)

x = int(input("isi angka ya :"))
y = int(input("isi angka ya :"))

print(pow(x,y))

#format cok iki kudune dinggo wingi
num = int(input("jajal"))
sq = pow(num,2)
print("smt smt smt {0} dan {1}".format(num,sq))

#nyari minimum
num = [1,2,3,4,5]
print("minimum nya {0}".format(min(num)))

#nyari max

num = [1,2,3,4,5]
print("maksnya itu {0}".format(max(num)))

#pembulatan
pecahan = float(input("kasi pecahan"))
print(round(pecahan,1)) #,1 itu jumlh desimalnya mauberapa

#sum
angka = int(input("isinen angka"))
angka2 = int(input("isinen angka"))
angka3 = int(input("isinen angka"))

box = [angka, angka2, angka3]

print("ini jumlah nya {0}". format(sum(box)))


