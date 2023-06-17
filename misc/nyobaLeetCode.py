from operator import index


'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
'''


nums = []
z = int(input("input target"))
while True : # ini buat ngulang teros
    inpt = input("enter number")
    if inpt == "x" :
        break
    x = int(inpt)
    nums.append(x)
    
print(nums)

for i in nums:
    for y  in nums: ### 2 for i ini buat nyari semua kombinasi yang mungkin didapat
        if i+y == z: #kalo dia nemu kombinasi nya dia berhenti
            break
print(nums.index(i), nums.index(y)) #dia ngeprint kombinasi itu di nomer berapa