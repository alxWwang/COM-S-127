# <Nicholas Alexander Wang>             <7 Dec 2022>
# Assignment #7 AnjayMan

import gameMap as gm
import gamePlay as gp

'''
This 'game' is a basic pacman style game where we read from a map an only show a snippet of that map for the player to roam around and collect gold
The game finishes when the player has collected all the gold in the map, and the counter is down to 0

The Map:
    - The map is formatted in a way, so that the viewers can go to the edge, but still know where the boundaries are.
    - there are 2 rows on top and the bottom, and 1 column on the left and right of the map marking the boundaries for a 5x5 viewer
    - The players spawn position can be changed in the main() variable spawnRow, and spawnCol
    
The viewer is integral to the function of the game, the viewer itself is made by
    - creating a reset variable for the row 
    - looping the row and column, resetting the row after every column loop, while limiting the loop range to the size wanted (which is 5)
    - appending the results to a list
    
The viewer is coded so that the player is in the middle of the view
    i did this by:
    - finding the middle of the viewer, which is floor division of 2 (AvatarRow,AvatarCol) from to size of the map
    - putting the original value on another variable
    - changing that variable to the players Avatar
    - returning the original value after printing the viewer

adding the score is by :
    - gettting the AvatarRow, and AvatarCol, and wrote an if statement if they are '@' a point is added
    - that coordinate will be changed into '+' marking that was a score 

'''

def main():
    print("Welcome to AnjayMan")
    print()

    print("By: Nicholas Alexander Wang")
    print("[COM S 127 A]")
    print()
    gameOver = False

    while gameOver == False:
        gold = 0
        spawnRow = 1
        spawnCol = 1
        
        
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": 
            mapChoice = gm.mapChoice()
            gameMap, goldCount = gm.loadGameBoard(mapChoice)
            while True :
                goldA = gold    
                print("---------------------------------------------")
                gold = goldA + gp.avatarView(5,gameMap,spawnRow-1,spawnCol-1,gold)
                a = goldCount - gold
                
                print()
                print("There are", a,"Gold left")
                print("You have collected:",gold,"Gold")
                print()
                
                if a == 0:
                    print()
                    print("That was a good one, Thanks for playing!!")
                    print()
                    break
                else :
                    spawnRow,spawnCol = gp.humanInput(spawnRow,spawnCol)
                print("---------------------------------------------")
                
        elif choice == "i":
            # TODO: Print out the instructions for the game (1 pt.)
            print("Move around the Map")
            print("Use WASD to move")
            print("collect all the gold indicated with '@' ")
            print("Collect them all !!")
            print("")
            pass
        elif choice == "q":
            # TODO: set gameOver to be True and print a 'goodbye' message to the player (1 pt.)
            print()
            print("OK Thanks for playing this game !!")
            gameOver = True
            pass
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()