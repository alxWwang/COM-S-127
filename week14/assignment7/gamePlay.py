# <Nicholas Alexander Wang>             <7 Dec 2022>
# Assignment #7 AnjayMan

import gameMap as gm
def humanInput(positionRow, positionCol):
    '''
    Using WASD to move.
    
    limiting the movement on the outer border so that the user dont go out of bounds.
    some of the code used in this assignment is based on the assignment 6 code which is tweaked and repurposed to fit the new game 
    
    '''
    
    while True:
        movement = input("Enter WASD to move :")

        if movement == "W" or movement == "w" and positionCol !=-1:
            positionCol -= 1
            break
        if movement == "A" or movement == "a" and positionRow !=-1:
            positionRow -=1
            break
        if movement == "S" or  movement == "s" and positionCol != 8:
            positionCol+=1
            break
        if movement == "D" or movement == "d" and positionRow != 18:
            positionRow += 1
            break
        
        else :
            print("You cannot move here! ")
        
    return positionRow,positionCol

def avatarView(size,gameboard,positionRow,positionCol,score):
    
    '''
    This section is so that the player is in the middle of the view
    
    i did this by:
    - finding the middle of the viewer, which is floor division of 2
    - putting the original value on another variable
    - changing that variable to the players Avatar
    - returning the original value after printing the viewer
    
    '''
    AvatarRow = positionRow + size//2
    AvatarCol = positionCol + size//2
    
    score = 0
    resetMap = gameboard[AvatarCol][AvatarRow]
    
    if gameboard[AvatarCol][AvatarRow] == "@":
        score += 1
        gameboard[AvatarCol][AvatarRow] = "+"
        resetMap = "+"
    
    
    gameboard[AvatarCol][AvatarRow] = "0"
    
    playView = gm.newView(size,gameboard,positionRow,positionCol)

    for s in playView:
        print(*s)

    gameboard[AvatarCol][AvatarRow] = resetMap
    
    return score

    
