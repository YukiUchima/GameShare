from turtle import Turtle, Screen

players = []
screen = Screen()
DISTANCE = 80


class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.setpos(xpos, ypos)
        players.append(self)

    def move_up(self):
        if self.ycor() < 220:
            UP = DISTANCE
            move = self.ycor() + UP
            self.sety(move)

    def move_down(self):
        if -220 < self.ycor():
            DOWN = -DISTANCE
            move = self.ycor() + DOWN
            self.sety(move)
