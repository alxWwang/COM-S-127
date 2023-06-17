import math

nameList = []
xCoordList = []
yCoordList = []
listDistance = []
result=[]


def main():
    while True:
        name = input("Enter Name :")
        if name == "*":
            break
        xCoord = int(input("Enter X coordinate :"))
        yCoord = int(input("Enter Y coordinate :"))
        
        
        nameList.append(name)
        xCoordList.append(xCoord)
        yCoordList.append(yCoord)
    
        
    resListX, resListY, resList = calculateDistance(nameList, xCoordList, yCoordList)

    a = resList.index(min(resList))
    print(resListX[a], resListY[a], resList[a])   

        
def calculateDistance(nameList, xCoordList,yCoordList):
    
    resListX = []
    resListY = []
    resList = []
    for x in range(len(nameList)):
        for y in range(len(nameList)):
            y2 = pow(xCoordList[x] - xCoordList[y],2)
            x2 = pow(yCoordList[x]- yCoordList[y],2)
        
            z2 = y2 + x2
            z = math.sqrt(z2)
        
            if nameList[x] != nameList[y]:    
                resListX += nameList[x]
                resListY += nameList [y]
                resList += [z]
                
                
            y+= 1
        print()
        x+= 1
    
    return resListX,resListY,resList
        
        
main()
