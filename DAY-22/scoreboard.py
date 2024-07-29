from turtle import Turtle



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scoreOfRightPlayer = 0
        self.scoreOfLeftPlayer = 0
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-130, 180)
        self.write(self.scoreOfLeftPlayer, align="center", font=("Arial", 50, "normal"))
        self.goto(130, 180)
        self.write(self.scoreOfRightPlayer, align="center", font=("Arial", 50, "normal"))