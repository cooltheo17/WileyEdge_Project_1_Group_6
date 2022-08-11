# player 1 = s
# player 2 = O
# Import random used to roll dice
import random

# Initialise players starting position (1,2) and direction (0,-1)
player1 = [1, 2, 0, -1]
player2 = [1, 2, 0, -1]

# Takes the player1 and player2 starting position as arguments
def game(player1, player2):
    currentPlayer = player1
    currentPlayerName = "S"
    # Print initial board
    printBoard(player1, player2)
    print("It is S's turn")
    # Loop will keep running until a player has reached the end tile
    while [player1[0], player1[1]] != [2, 2] and [player2[0], player2[1]] != [2, 2]:
        # Call advanceGame with the current player as an argument
        advanceGame(currentPlayer)
        # Check if player O has landed on S
        if player1 == player2 and currentPlayerName == "O":
            player1 = [1, 2, 0, -1]
            print("O has \033[33mkilled\033[0;0m S")
        # Check if player S has killed player O
        elif player1 == player2 and currentPlayerName == "S":
            player2 = [1, 2, 0, -1]
            print("S has \033[33mkilled\033[0;0m O")

        printBoard(player1, player2)
        # Check which player's turn it is
        if currentPlayerName == "S" and [player1[0], player1[1]] != [2, 2]:
            currentPlayer = player2
            currentPlayerName = "O"
            print("It is O's turn")
        elif currentPlayerName == "O" and [player2[0], player2[1]] != [2, 2]:
            currentPlayer = player1
            currentPlayerName = "S"
            print("It is S's turn")
    # Check if player won the game
    if currentPlayer == player1:
        print("\033[0;32m S has won the game!")
        print("\033[0;0m============================")
    else:
        currentPlayer = player1
        print("\033[0;32m O has won the game!")
        print("\033[0;0m============================")

# Handles the rolling of the dice mechanic
def advanceGame(currentPlayer):
    input("Press enter to roll dice")
    print("Rolling Dice...")
    currentRoll = random.randint(1, 3)
    print("The result is ", currentRoll)
    # Check if a player rolled too high
    if (currentPlayer[0] == 2 and currentPlayer[1] == 3 and currentRoll > 2) or (
            currentPlayer[0] == 1 and currentPlayer[1] == 3 and currentRoll > 1):
        print("\033[1;31m You rolled too high. Turn has been skipped.\033[0;0m")
        pass
    # Otherwise call the move method for the player
    else:
        move(currentPlayer, currentRoll)

def move(currentPlayer, currentRoll):
    for i in range(1, currentRoll + 1):
        # Check if user is on the first corner, if yes turn direction 90 degrees
        if currentPlayer[0] == 1 and currentPlayer[1] == 1:
            currentPlayer[2] = 1
            currentPlayer[3] = 0
        # Check if user is on the second  corner, if yes turn direction 90 degrees
        elif currentPlayer[0] == 3 and currentPlayer[1] == 1:
            currentPlayer[2] = 0
            currentPlayer[3] = 1
        # Check if user is on the third corner, if yes turn direction 90 degrees
        elif currentPlayer[0] == 3 and currentPlayer[1] == 3:
            currentPlayer[2] = -1
            currentPlayer[3] = 0
        # Check if user is on the last corner, if yes move player on the finish block
        elif currentPlayer[0] == 1 and currentPlayer[1] == 3:
            currentPlayer[2] = 1
            currentPlayer[3] = -1
        currentPlayer[0] += currentPlayer[2]
        currentPlayer[1] += currentPlayer[3]

# Two nested loops to cycle through a 3 by 3 matrix
def printBoard(player1, player2):
    print("-------------")
    for i in range(1, 4):
        print("|", end="")
        for j in range(1, 4):
            print(getPattern(4 - i, j, player1, player2), end="|")
        print("\n-------------")
    print("============================")

# Gets the pattern for a specific tile depending on how many players are on it
def getPattern(i, j, p1, p2):
    if j == p1[0] and i == p1[1] and j == p2[0] and i == p2[1]:
        pattern = " \033[1;36mSO\033[0;0m"
    elif j == p1[0] and i == p1[1]:
        pattern = " \033[1;36mS\033[0;0m "
    elif j == p2[0] and i == p2[1]:
        pattern = " \033[1;36mO\033[0;0m "
    else:
        pattern = "   "
    return pattern

# Start game
game(player1, player2)