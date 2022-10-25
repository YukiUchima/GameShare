from turtle import Turtle, Screen
import random

SNAKE_SIZE = 4
move_distance = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
x_max = 280
x_min = -280
y_max = 230
y_min = -295


class Snake:
    def __init__(self):
        self.snake = []
        self.first_position = 0
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for snake_segment in range(SNAKE_SIZE):
            new_seg = self.grow()
            new_seg.setpos(x=self.first_position, y=0)
            self.snake.append(new_seg)
            self.first_position -= 20

    def delete_snake(self):
        for snake_segment in self.snake:
            snake_segment.reset()

    def new_tail(self):
        grow_tail = self.grow()
        grow_tail.setpos(self.snake[-1].pos())
        self.snake.append(grow_tail)

    def grow(self):
        grow_tail = Turtle()
        grow_tail.penup()
        grow_tail.color("white")
        grow_tail.shape("square")
        return grow_tail

    def ignore_boundary(self):
        if self.head.xcor() >= x_max:
            self.head.setx(x_min + 10)

        elif self.head.xcor() <= x_min:
            self.head.setx(x_max + 10)

        elif self.head.ycor() >= y_max:
            self.head.sety(y_min + 10)

        elif self.head.ycor() <= y_min:
            self.head.sety(y_max + 10)

    def move(self):
        xloc = self.head.xcor()
        yloc = self.head.ycor()
        # print([yloc, xloc])
        print(self.head.pos())

        for tail in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[tail - 1].xcor()
            new_y = self.snake[tail - 1].ycor()
            self.snake[tail].setpos(new_x, new_y)
        self.head.forward(move_distance)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
