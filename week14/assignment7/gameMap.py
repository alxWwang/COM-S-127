# <Nicholas Alexander Wang>             <7 Dec 2022>
# Assignment #7 AnjayMan

boardLow = 1
boardHigh = 2

def loadGameBoard(gameboardChoice):
    '''
    opening the gameboard and adding to a list
    
    '''
    
    with open("map" + str(gameboardChoice) + ".txt", "r") as f:
        contents = f.readlines()
    
    gameBoard = []
    for line in contents:
        line = list(line)
        gameBoard.append(line[:len(line)-1])
    
    numTargets = 0
    for row in gameBoard:
        for character in row:
            if character == "@":
                numTargets += 1
    
    
    return gameBoard, numTargets

def mapChoice():
    while True:
        try:
            choice = int(input("Enter a map choice (" + str(boardLow) + " - " + str(boardHigh) + "): "))
            while choice <boardLow or choice > boardHigh:
                print("Enter another number")
                choice = int(input("Enter a map choice (" + str(boardLow) + " - " + str(boardHigh) + "): "))
            break
        except Exception as e:
            print("ERROR: chooseGameBoard - please enter an integer:", e)
            continue
        
    return choice
        
        

def newView(size,map, kanan, bawah):
    '''
    This is a view of the smaller map
    1. creating a reset variable for the row 
    2. looping the row and column, resetting the row after every column loop
    3. appending the results to a list
    '''
    viewList = []
    resetKanan = kanan
    for i in range(size):
        kanan = resetKanan
        a = ''
        for y in range(size):
            a = a + map[bawah][kanan] + ''
            kanan += 1
        viewList.append(a)
        bawah += 1
    return viewList
