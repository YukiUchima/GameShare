from turtle import Turtle
import random

TOP_BORDER = 215
BOTTOM_BORDER = -280
LEFT_BORDER = -280
RIGHT_BORDER = 280
COLORS = ["red", "yellow"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)  # default 20x20 size (halved here)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.refresh()

    def set_new_pos(self):
        x_new = random.randint(LEFT_BORDER, RIGHT_BORDER)
        y_new = random.randint(BOTTOM_BORDER, TOP_BORDER)
        return [x_new, y_new]

    def refresh(self):
        x_new_pos = self.set_new_pos()[0]
        y_new_pos = self.set_new_pos()[1]

        while x_new_pos == self.xcor():
            x_new_pos = self.set_new_pos()[0]
        while y_new_pos == self.ycor():
            x_new_pos = self.set_new_pos()[1]
        self.goto(x_new_pos, y_new_pos)
        self.change_color()

    def change_color(self):
        self.color(random.choice(COLORS))
