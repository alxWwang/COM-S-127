# Nicholas Alexander Wang            8-11-2022
# Assignment #6 Naval Battle

import gameBoard
import gameInput

def _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets):
    """This function controls what happens when it is the human's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numComputerTargets (int): The number of computer targets remaining.
    
    Returns:
        list of lists, list of lists, list of lists, int: All of the relevant gameboards and the number of computer targets remaining.
    """
    # TODO: Complete the logic below so that the human can take a turn attacking the computer. (1 pt.)

    # Print out that it's the human's turn, as well as the targetBoard and humanGameBoard.
    
    print("This is Human's Turn")
    
    gameBoard.printBoard(targetBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)
    print()
    gameBoard.printBoard(humanGameBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)
    print()
    print("You have ",numComputerTargets,"Targets to hit")
    
    pass

    # Call gameInput.getHumanInput() to get input for where to attack (row and column).
    # Do input validation to make sure that the row/ column on the targetBoard is not already 'X' or 'O'
    # if it is, get new input.
    
    while True :
        row,col = gameInput.getHumanInput()
        if targetBoard[row][col] == "X" or targetBoard[row][col] == '0' :
            print()
            print("You have already attacked this coordinate")
            print()
        else :
            break
    pass
    
    # Print out the coordinates the human is targeting.
    print(row,col)
    pass
    
    # Check to see if the row and column on the computerGameBoard contains an '@'.
    # If it does, set it to 'X' on both computerGameBoard and targetBoard, print 'HIT',
    # and decrease the numComputerTargets variable by 1 (as that target has been hit).
    # Else, set that space on the computerGameBoard and targetBoard to 'O' and print 'MISS'.
    pass
    if computerGameBoard[row][col] == '@':
        targetBoard[row][col] = 'X'
        computerGameBoard[row][col] = 'X'
        print("HIT")
        numComputerTargets -=1
        print()
    else :
        computerGameBoard[row][col] = "0"
        targetBoard[row][col] = '0'
        print("MISS")
        print()

    
    
    return humanGameBoard, targetBoard, computerGameBoard, numComputerTargets

def _computerTurn(humanGameBoard, numHumanTargets):
    """This function controls what happens when it is the computer's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets remaining.
    
    Returns:
        list of lists, int: All of the relevant gameboards and the number of human targets remaining.
    """
    # TODO: Complete the logic below so that the computer can take a turn attacking the human. (1 pt.)

    # Print out that it's the computer's turn.
    print("This is Computers Turn")
    
    print()
    print("The Computer have ",numHumanTargets,"Targets to hit")
    pass

    # Call gameInput.getComputerInput() to get input for where to attack (row and column).
    # Do input validation to make sure that the row/ column on the humanGameBoard is not already 'X' or 'O'
    # if it is, get new input.
    while True :
        row,col = gameInput.getComputerInput()
        if humanGameBoard[row][col] == "X" or humanGameBoard[row][col] == '0' :
            continue
        else :
            break
    
    pass

    # Print out the coordinates the computer is targeting.
    print(row,col)
    pass

    # Check to see if the row and column on the humanGameBoard contains an '@'.
    # If it does, set it to 'X' on the humanGameBoard, print 'HIT', 
    # and decrease the numHumanTargets variable by 1 (as that target has been hit).
    # Else, set that space on the computerGameBoard to 'O' and print 'MISS'.
    if humanGameBoard[row][col] == '@':
        humanGameBoard[row][col] = 'X'
        print("HIT")
        numHumanTargets -=1
        print()
    else :
        humanGameBoard[row][col] = "0"
        print("MISS")
        print()
    pass
    
    return humanGameBoard, numHumanTargets

def _printWinner(numComputerTargets, computerGameBoard):
    """This function prints out which player has won the game, depending on the numComputerTargets remaining.

    Args:
        numComputerTargets (int): The number of computer targets left. If there are none, the human wins. Else - the computer wins.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.
    """
    # TODO: Complete the logic below so that the player can see who won the game. (1 pt.)

    # Check if numComputerTargets is zero (0). If it is, print that the human has won.
    # Otherwise, print that the computer has won.
    
    if numComputerTargets == 0:
        print("The Human has Won!")
    else:
        print("The Computer has Won!!")
    
    pass
    
    # Print the computer's gameboard for the player to see using the printBoard method of the gameBoard module.
    
    gameBoard.printBoard(computerGameBoard,gameBoard.GAME_BOARD_WIDTH,gameBoard.GAME_BOARD_HEIGHT)
    print()
    pass

    return

def runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets):
    """This function controls the flow of the game and switches turns between the human and the computer.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets left.

        numComputerTargets (int): The number of computer targets left.
    """
    currentTurn = 0 # 0 = human, 1 = computer

    # play the game (HUMAN goes first)
    while numHumanTargets > 0 and numComputerTargets > 0:
        if currentTurn == 0:
            humanGameBoard, targetBoard, computerGameBoard, numComputerTargets = _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets)
        else:
            humanGameBoard, numHumanTargets = _computerTurn(humanGameBoard, numHumanTargets)

        # switch whose turn it is
        currentTurn += 1
        currentTurn %= 2
    
    # print the winner once the game is over
    _printWinner(numComputerTargets, computerGameBoard)

    return


