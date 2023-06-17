# <Nicholas Alexander Wang>             <28 Nov 2022>
# Assignment #6 Naval Battle

# TODO: Ensure that the assignment is turned in by the due date AND Ensure that the files that gets submitted are called 
# 'navalBattle.py', 'gameBoard.py', 'gameInput.py', 'gamePlay.py', 'targetBoard.txt', 'board1.txt', and 'board2.txt'.
# These files should be included in a .zip file called 'navalBattle.zip' (1 pt.)

# NOTE: All of the 'TODO' statements are contained in navalBattle.py, gamePlay.py and gameInput.py.

import gameBoard
import gamePlay

def main():
    """This is the main function of the game. It controls the flow/ execution of the entire script.
    """
    gameOver = False

    gameboardChoice = 0
    humanGameBoard = None
    targetBoard = None
    computerGameBoard = None
    
    numHumanTargets = 0
    numComputerTargets = 0
    
    print("Welcome to Naval Battle!")
    print()
    
    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: Nicholas Alexander Wang")
    print("[COM S 127 A]")
    print()

    while gameOver == False:
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": 
            '''
            a = gameBoard.chooseHumanGameBoard()
            gameBoards,numTarget = gameBoard.loadGameBoard(a)
            targetnya = gameBoard.loadTargetBoard()


            b = gameBoard.chooseComputerGameBoard()
            compGameBoards,numTargetComp = gameBoard.loadGameBoard(b)

            while True:
                gamePlay._humanTurn(gameBoards,targetnya,compGameBoards,numTargetComp)
                gamePlay._computerTurn(gameBoards,numTarget)
                break
            '''
            # TODO: Fill out the data structures necessary to play the game by calling the methods referenced below. (1 pt.)

            # Choose which gameboard to use for the HUMAN player with the chooseHumanGameBoard method in the gameBoard module. 
            # Assign this to choice to the gameboardChoice variable.
            gameboardChoice = gameBoard.chooseHumanGameBoard()
            pass

            # Load the gameboard for the HUMAN player with the loadGameBoard method in the gameBoard module.
            # Assign the output of this method to the humanGameBoard and numHumanTargets variables.
            humanGameBoard,numHumanTargets = gameBoard.loadGameBoard(gameboardChoice)
            pass

            # Choose which gameboard to use for the COMPUTER player with the chooseComputerGameBoard method in the gameBoard module.
            # Assign this to choice to the gameboardChoice variable.
            ComputerGameboardChoice= gameBoard.chooseComputerGameBoard()
            pass

            # Load the gameboard for the COMPUTER player with the loadGameBoard method in the gameBoard module.
            # Assign the output of this method to the computerGameBoard and numComputerTargets variables.
            computerGameBoard,numComputerTargets = gameBoard.loadGameBoard(ComputerGameboardChoice)
            pass

            # Load the 'target board' for the HUMAN player to use with the loadTargetBoard method in the gameBoard module. 
            # Assign this to choice to the targetBoard variable.
            targetBoard = gameBoard.loadTargetBoard()
            pass

            # Run the game by passing in the relevant data to the runGame method of the gamePlay module.
            gamePlay.runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets)
        elif choice == "i":
            # TODO: Print out the instructions for the game (1 pt.)
            print("Enter the board you choose")
            print("Enter the coordinate which you want to attack your opponent in")
            print("The selected target will appear in the Top grid")
            print("The computer will take turns hitting you")
            print("if the attack hits it will show as X, if it misses it will show as 0")
            print("Goodluck !!")
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