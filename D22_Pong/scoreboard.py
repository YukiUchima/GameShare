from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.updateBoard()
        # self.scoreSetup()

    def points(self, player):
        self.clear()
        if player == "one":
            self.score1 += 1
        else:
            self.score2 += 1
        self.updateBoard()

    def updateBoard(self):
        self.goto(-100, 200)
        self.write(self.score1, align="Center", font=('Arial', 40, 'bold'))
        self.goto(100, 200)
        self.write(self.score2, align="Center", font=('Arial', 40, 'bold'))
