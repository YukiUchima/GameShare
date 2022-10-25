from turtle import Turtle


class Boundary(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.setpos(0, pos)
        self.shapesize(0.5, 40)
