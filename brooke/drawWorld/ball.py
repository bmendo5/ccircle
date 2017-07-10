class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.fx = 0
        self.fx = 0
        self.mass = 1

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):
        window.drawCircle(self.x, self.y, 16, 1, 1, 0.25)

    def update(self, dt):
        self.x += dt * self.vx
        self.y += dt * self.vy
        accel_x = self.fx / self.mass
        accel_y = self.fy / self.mass
        self.vx += dt * accel_x
        self.vy += dt * accel_y
        self.fx = 0
        self.fy = 0