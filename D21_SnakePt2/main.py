from turtle import Screen
from food import Food
from snake import Snake
from time import sleep
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game Python")
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
screen.update()
score = Score()


def set_up():
    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_right, "Right")
    screen.onkey(snake.turn_up, "Up")
    screen.onkey(snake.turn_down, "Down")


def game_over(count):
    if count < 1:
        score.game_over()
        return True
    return False


# boundary_enabled = True
set_up()
game_on = True

while game_on:
    screen.update()
    snake.move()
    # snake.ignore_boundary()
    sleep(0.05)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.new_tail()
        food.refresh()
        score.point()
        # if score.score % 5 == 0:
        #     snake.move_distance += 5

    # Detect Wall Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.lives -= 1
        if game_over(lives):
            game_on = False
            break
        sleep(1)
        snake.delete_snake()
        snake = Snake()
        set_up()

    # Detect Snake Collision With Tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score.lives -= 1
            if game_over(lives):
                game_on = False
                break
            sleep(1)
            snake.delete_snake()
            snake = Snake()
            set_up()


        # for segment in snake.snake:
        #     if segment == snake.head:
        #         pass
        #     elif snake.head.distance(segment) < 15:
        #         game_on = False
        #         score.game_over()
        #         break
        
screen.exitonclick()
