import ccircle

window = ccircle.Window("Tic Tac Toe", 600,600)
window.showMouse()

while window.isOpen():
    window.clear(1,1,1)

    #Tic Tac Toe Borders
    window.drawLine(200, 100, 200, 500, 5, 0,0,0)   #vertical left
    window.drawLine(350, 100, 350, 500, 5, 0,0,0)   #vertical right
    window.drawLine(75, 225, 475, 225, 5, 0,0,0)    #horizontal top
    window.drawLine(75, 375, 475, 375, 5, 0,0,0)    #horizontal bottom

    #mousePosX, mousePosY = window.getMousePos()
    #print(mousePosX, mousePosY)


    window.update()

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
