import random


class Blob:

    def __init__(self, color, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.size = random.randrange(4,8)
        self.color = color


    def move(self):
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary

        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary
Next, within our original file, when we call the Blob class, it's expecting some values for those arguments, so you'd add those in the main function:

def main():
    blue_blobs = dict(enumerate([Blob(BLUE,WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([Blob(RED,WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    while True:
        ...
