import ccircle

window = ccircle.Window("Brooke's Window!",1000, 800)

while window.isOpen():
    window.clear((204/255), 1, (229/255))
    window.drawRect(250, 150, 500, 400, 1, 1, 1)

    #mousePosX, mousePosY = window.getMousePos()
    #print(mousePosX, mousePosY)

    #side RIGHT
    #750, 150 -> 750, 550
    # x3, y3 = center (680,280)
    yRight = 150
    while yRight <= 520:
        window.drawTri(750, yRight, 750, yRight + 30, 560, 340, 1, .5, 0)
        yRight += 37

    #side BOTTOM
    #250, 550 -> 750, 550
    xBottom = 250
    while xBottom <= 720:
        window.drawTri(xBottom, 550, xBottom + 30, 550, 560, 340, 1, .5, 0)
        xBottom += 38

    #side Left
    #250, 150 -> 250, 550
    yLeft = 150
    while yLeft <= 520:
        window.drawTri(250, yLeft, 250, yLeft + 30, 560, 340, 1, .5, 0)
        yLeft += 37

    i = 10
    j = 3
    for x in range(20):
        window.drawCircle(i, 200, x, (229/255), (204/255), 1)
        i += 40
        j += 50
    window.update()