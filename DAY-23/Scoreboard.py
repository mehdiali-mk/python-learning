from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def levelUp(self):
        self.level += 1
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)