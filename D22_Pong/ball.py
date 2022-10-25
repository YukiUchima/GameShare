from turtle import Turtle
from time import sleep

PAUSE = 0.5
score = 0

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.LEFT = False
        self.DOWN = False
        self.dist = 2
        self.y_dir = self.dist
        self.x_dir = self.dist
        self.score = 0
        self.shape("circle")
        self.color("orange")
        self.max_speed = 0
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_dir
        new_y = self.ycor() + self.y_dir
        self.setpos(new_x, new_y)

    def bounce(self, direction):
        if direction == "x":
            self.x_dir *= -1
        else:
            self.y_dir *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.max_speed = 0
        if self.LEFT:
            self.x_dir = -self.dist
        else:
            self.x_dir = self.dist
        if self.DOWN:
            self.y_dir = -self.dist
        else:
            self.y_dir = self.dist
        sleep(PAUSE)

    def speed_up(self):
        if self.x_dir < 0:
            self.x_dir -= 1
            self.LEFT = True
        else:
            self.x_dir += 1
            self.LEFT = False
        if self.y_dir < 0:
            self.y_dir -= 1
            self.DOWN = True
        else:
            self.y_dir += 1
            self.DOWN = False
