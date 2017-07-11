import ccircle

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
