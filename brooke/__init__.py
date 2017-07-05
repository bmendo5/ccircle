import ccircle

window = ccircle.Window("Brooke's Window!",1000, 800)

while window.isOpen():
    window.clear((204/255), 1, (229/255))
    window.drawRect(250, 150, 500, 400, 1, 1, 1)
    i = 10
    j = 3
    for x in range(20):
        window.drawCircle(i, 200, x, (229/255), (204/255), 1)
        i += 40
        j += 50
    mousePosX, mousePosY = window.getMousePos()
    window.update()
