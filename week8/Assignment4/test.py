import random
import sys

# GLOBAL CONSTANT VARIABLES
START_ROOM = 1
FINAL_ROOM = 9999

def room1(goldAmount, visited_room):
    direction = input("[n] [s] [e] [w]?: ")
    while direction != "n" and direction != "s" and direction != "e" and direction != "w":
        print("Invalid input...")
        direction = input("[n] [s] [e] [w]?: ")
    
    roomChoice = -1 # HINT: Once this section is encapsulated into a function, it would be wise to have a default roomChoice value outside that function.
    if direction == "n":
        roomChoice = 2
    elif direction == "s":
        roomChoice = 2
    elif direction == "e":
        roomChoice = 2
    elif direction == "w":
        roomChoice = 2
    
    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return roomChoice, goldAmount, visited_room

def room2(goldAmount, visited_room):
    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        gold = 20 # This is the amount of gold the room contains.

        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()

    # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    direction = input("[n] [s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n] [s]?: ")
    
    roomChoice = -1
    if direction == "n":
        roomChoice = FINAL_ROOM
    elif direction == "s":
        roomChoice = 1

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return roomChoice, goldAmount, visited_room

# Main function
def main():
    # Set to 'True' when the game is over.
    gameOver = False

    # Player status variables/ constants. 
    # HINT: If you have other player variables to use, such as health, damage, etc. add them here.
    START_GOLD = 0 # HINT: This is a 'constant' value. Notice how it is used to set/ reset the goldAmount value.
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    visited_room1 = False # HINT: Carefully study how these 'visited room' variables are used.
    visited_room2 = False

    print("Welcome to Dungeon Crawl...")
    print()

    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: <Student Name>")
    print("[COM S 127 <section>]")
    print()

    while gameOver == False:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": # (**"p" Section Tasks**)
            # TODO: Add at least four (4) additional rooms to the dungeon - creating a new 'room' function for each of them (1 pt.)
            #
            # HINT: This will require planning out the layout of your dungeon so that all the 'rooms' connect together correctly.
            #
            # HINT: Study this code carefully to see how the rooms connect, and which room the player is currently inside.
            #
            # NOTE: The other TODO tasks for this assignment can be found in the 'room1' function above.
            while currentRoom != FINAL_ROOM: # HINT: When implmenting combat, if the player's health is <= 0, this loop should not execute.
                if currentRoom == 1:
                    currentRoom, goldAmount, visited_room1 = room1(goldAmount, visited_room1)
                elif currentRoom == 2:
                    currentRoom, goldAmount, visited_room2 = room2(goldAmount, visited_room2)
                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()
            
            # HINT: If the player's health is > 0 when they escape the dungeon print a message like this one. 
            # Otherwise print a message stating that they perished in the dungeon.
            print()
            print("You have escaped with", goldAmount, "gold from the dungeon!")
            print()

            # Reset player values back to their original state
            # HINT: If you add other player values, you will have to reset them to their original values to restart the game.
            #
            # HINT: You can create 'constants' that you can assign to these variables. Doing so means you will only need to 
            # change the values you want to use in one place if you wish to change them.
            goldAmount = START_GOLD
            currentRoom = START_ROOM
            visited_room1 = False
            visited_room2 = False
        elif choice == "i": # (**"i" Section Tasks**)
            # TODO: Delete the following 'pass' statement and print out instructions for how to play the game. (1 pt.)
            # NOTE: Please feel free to use your imagination here.
            pass
        elif choice == "q": # (**"q" Section Tasks**)
            # TODO: Delete the following 'pass' statement and set the gameOver variable to be 'True' (0.5 pt.)
            # TODO: Print out a 'goodbye' message to the player. (0.5 pt.)
            pass
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()