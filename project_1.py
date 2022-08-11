# player 1 = s
# player 2 = O
import random

player1 = [1, 2, 0, -1]
player2 = [1, 2, 0, -1]


def game(player1, player2):
    currentPlayer = player1
    currentPlayerName = "S"
    printBoard(player1, player2)
    print("It is S's turn")
    while [player1[0], player1[1]] != [2, 2] and [player2[0], player2[1]] != [2, 2]:
        advanceGame(currentPlayer)

        if player1 == player2 and currentPlayerName == "O":
            player1 = [1, 2, 0, -1]
            print("O has \033[33mkilled\033[0;0m S")


        elif player1 == player2 and currentPlayerName == "S":
            player2 = [1, 2, 0, -1]
            print("S has \033[33mkilled\033[0;0m O")
        printBoard(player1, player2)
        if currentPlayerName == "S" and [player1[0], player1[1]] != [2, 2]:
            currentPlayer = player2
            currentPlayerName = "O"
            print("It is O's turn")

        elif currentPlayerName == "O" and [player2[0], player2[1]] != [2, 2]:
            currentPlayer = player1
            currentPlayerName = "S"
            print("It is S's turn")

    if currentPlayer == player1:
        print("\033[0;32m S has won the game!")
        print("\033[0;0m============================")
    else:
        currentPlayer = player1
        print("\033[0;32m O has won the game!")
        print("\033[0;0m============================")


def advanceGame(currentPlayer):
    input("Press enter to roll dice")
    print("Rolling Dice...")
    currentRoll = random.randint(1, 3)
    print("The result is ", currentRoll)
    if (currentPlayer[0] == 2 and currentPlayer[1] == 3 and currentRoll > 2) or (
            currentPlayer[0] == 1 and currentPlayer[1] == 3 and currentRoll > 1):
        print("\033[1;31m You rolled too high. Turn has been skipped.\033[0;0m")
        pass

    else:
        move(currentPlayer, currentRoll)


def move(currentPlayer, currentRoll):
    for i in range(1, currentRoll + 1):
        if currentPlayer[0] == 1 and currentPlayer[1] == 1:
            currentPlayer[2] = 1
            currentPlayer[3] = 0
        elif currentPlayer[0] == 3 and currentPlayer[1] == 1:
            currentPlayer[2] = 0
            currentPlayer[3] = 1
        elif currentPlayer[0] == 3 and currentPlayer[1] == 3:
            currentPlayer[2] = -1
            currentPlayer[3] = 0
        elif currentPlayer[0] == 1 and currentPlayer[1] == 3:
            currentPlayer[2] = 1
            currentPlayer[3] = -1
        currentPlayer[0] += currentPlayer[2]
        currentPlayer[1] += currentPlayer[3]


def printBoard(player1, player2):
    print("-------------")
    for i in range(1, 4):
        print("|", end="")
        for j in range(1, 4):
            print(getPattern(4 - i, j, player1, player2), end="|")
        print("\n-------------")
    print("============================")


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


game(player1, player2)

'''
initialise player1 and player2 with their starting position
call game()
print(Initial Board)
while (No player has landed on finishing tile)
    call advanceGame()
        rollDice
        if player roll is too high
            skip
        else
            move
    check if a player killed another player
    print(New board state)
A player has won print(Board) and winning player                  
'''