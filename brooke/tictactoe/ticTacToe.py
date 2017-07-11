import ccircle

# use 0 and 1 for player 1 and player 2
playerInputs = [2,3,4,5,6,7,8,9,10]
turn = True
while checkWin(playerInputs):
    turn = not turn # swaps turns
    input()

if turn:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")

def checkWin(playerInputs):
    if playerInputs[0] == playerInputs[1] == playerInputs[2]:
        return True
    elif playerInputs[2] == playerInputs[5] == playerInputs[8]:
        return True
    elif playerInputs[6] == playerInputs[7] == playerInputs[8]:
        return True
    elif playerInputs[0] == playerInputs[3] == playerInputs[6]:
        return True
    elif playerInputs[0] == playerInputs[4] == playerInputs[8]:
        return True
    elif playerInputs[2] == playerInputs[4] == playerInputs[6]:
        return True
    return False
