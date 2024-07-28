from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y= 260)
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)


    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()