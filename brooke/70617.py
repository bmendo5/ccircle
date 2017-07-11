import ccircle
from math import *

window = ccircle.Window()
window.toggleMaximized()
window.hideMouse()

points = []

while window.isOpen():
    print(points)
    window.clear(1, 1, 1)
    mx, my = window.getMousePos()

    if ccircle.isMouseDown('left'):
        points.append((mx, my))

    for point in points:
        window.drawCircle(point[0], point[1], 8, .1, .5, 1)

 #   if len(points) > 6:
  #      window.drawCircle(points[6][0], points[6][1], 16, 1, .3, .1)

    window.drawCircle(mx, my, 8, .1, .5, 1)
    window.update()