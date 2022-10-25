from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from boundary import Boundary
from scoreboard import Scoreboard

LEFT = -350
RIGHT = 350
TOP = 290
BTM = -290

# TODO - Create Screen
WIDTH = 800
HEIGHT = 600
screen = Screen()

screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Python PONG")
screen.tracer(0)
score = Scoreboard()
screen.listen()

pong = Ball()

top = Boundary(TOP)
btm = Boundary(BTM)

# TODO - Create and move PADDLES
l_paddle = Paddle(LEFT, 0)
r_paddle = Paddle(RIGHT, 0)
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# TODO - Scoreboard
game_on = True
hit = True
move_speed = 0.005

while game_on:
    screen.update()

    # TODO - Create Ping Pong and make it move
    pong.move()

    # TODO - Detect collision with wall and bounce
    if pong.ycor() > 270 or pong.ycor() < -270:
        pong.bounce("y")

    # TODO - Detect collision with PADDLE
    if (pong.distance(l_paddle) < 50 or pong.distance(r_paddle) < 50) and (pong.xcor() > 320 or pong.xcor() < -320) \
            and hit:
        hit = False
        pong.bounce("x")
        if pong.max_speed < 6:
            pong.max_speed += 1
            pong.speed_up()

    # TODO - Detect when paddle misses
    if pong.xcor() > 360:
        pong.ball_reset()
        score.points("one")

    if pong.xcor() < -360:
        pong.ball_reset()
        score.points("two")

    # TODO - Detect when it is away from paddle
    if pong.distance(l_paddle) > 100 and pong.distance(r_paddle) > 100:
        hit = True

    sleep(move_speed)

screen.exitonclick()
