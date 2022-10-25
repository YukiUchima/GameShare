from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
POS_TOP = 270

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.penup()
        self.color("white")
        self.goto(0, POS_TOP)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} ~ Lives: {self.lives}/3", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_score()
