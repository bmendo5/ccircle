import ccircle
import cloud
import world
import random
import time

window = ccircle.Window('Lab 4', 800, 600)
my_world = world.World('MY WORLD')

for i in range(1000):
    x = random.randint(0, 800)
    y = random.randint(100, 200)
    size = 25 + 75.0 * (random.uniform(0,1) **2)
    vx = random.uniform(0,50)
    my_world.add(cloud.Cloud(x, y, size))

my_world.add(ball.Ball(400, 300))

start = time.time()
dt = 1.0 / 60.0
while window.isOpen():
    window.clear(0.1, 0.1, 0.1)
    my_world.draw(window)
    my_world.update()
    window.update()

    now = time.time()
    dt = now - start
    start = now