# Abraham Aldaco
# Nov 12, 2022

# Files & Matrix

#%%
# Step 1 : Prepare the matrix A, B, C 

matrixA3x3=[]
matrixB3x3=[]
matrixC3x3=[[0,0,0],[0,0,0],[0,0,0]]


#%%
# Step 2 : Read the file matrixA3x3.txt  

fo = open("matrixA3x3.txt", "r")

while True:
    line = fo.readline()

    if (not line):
        break
    everyLineList = line.split(' ')
    #print(line)
    #print(listaLine)
    matrixA3x3.append(everyLineList)

fo.close()

print(matrixA3x3)

# %%
# Step 3 : Read the file matrixB3x3.txt  


fo = open("matrixB3x3.txt", "r")

while True:
    line = fo.readline()

    if (not line):
        break
    everyLineList = line.split()
    #print(line)
    #print(listaLine)
    matrixB3x3.append(everyLineList)

fo.close()

print(matrixB3x3)


# %%
# Step 4 : Sum matrixA3x3 to matrixB3x3 = matrixC3x3 


for i in range(len(matrixC3x3)):
    for j in range(len(matrixC3x3[0])):
        matrixC3x3[i][j] = int(matrixA3x3[i][j]) + int(matrixB3x3[i][j])
        
print(matrixC3x3)


# %%
# Step 5 : Write matrixC3x3 to a File. 

fo = open("matrixC3x3.txt", "a")

for row in range(len(matrixC3x3)):
    data=''
    for col in range(len(matrixC3x3[0])):
        data=data+' '+str(matrixC3x3[row][col])
    
    fo.write(data)
    fo.write('\n')

# close
fo.close()


