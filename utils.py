class Robot:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.position = [self.x, self.y]

    def get_position(self):
        return self.position

class Obstacle:
    pass
