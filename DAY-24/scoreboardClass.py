from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        with open(f"D:\Study\Mehdiali\My Python Learning\python-learning\DAY-24\data.txt", "r") as file:
            self.highScore = int(file.read())
        self.hideturtle()
        self.goto(x=0, y= 260)
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.write(f"High Score: {self.highScore} Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if (self.score > self.highScore):
            self.highScore = self.score
            with open(f"D:\Study\Mehdiali\My Python Learning\python-learning\DAY-24\data.txt", "w") as file:
              file.write(f"{self.highScore}")
        self.score = 0
        self.updateScoreBoard()

    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)


    def increaseScore(self):
        self.score += 1
        self.updateScoreBoard()