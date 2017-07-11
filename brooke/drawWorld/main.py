import ccircle
import cloud
import world
import ball
import random
import time

window = ccircle.Window('Lab 4', 800, 600)
my_world = world.World('MY WORLD')

for i in range(100):
    x = random.randint(0, 800)
    y = random.randint(100, 200)
    size = 25 + 75.0 * (random.uniform(0,1) **2)
    vx = random.uniform(0,50)
    my_world.add(cloud.Cloud(x, y, size, vx))

my_ball = ball.Ball(200,300)
my_world.add(my_ball)

start = time.time()
dt = 1.0 / 60.0
while window.isOpen():
    window.clear(0.1, 0.1, 0.1)
    my_ball.apply_force(0, -9.8)
    my_ball.apply_force(100, 0)
    my_world.update(dt)
    my_world.draw(window)
    window.update()

    now = time.time()
    dt = now - start
    start = now