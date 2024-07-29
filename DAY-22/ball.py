from turtle import Turtle

class PongBall(Turtle):

    def __init__(self):
        super().__init__()
        self.body = Turtle()
        self.body.shape("circle")
        self.body.shapesize(stretch_wid=1, stretch_len=1)
        self.body.penup()
        self.body.color("red")
        self.body.goto(x=0, y=0)
        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.1

    def move(self):
        xPos = self.body.xcor() + self.xMove
        yPos = self.body.ycor() + self.yMove
        self.body.goto(x=xPos, y=yPos)

    def bounceY(self):
        self.yMove *= -1
    
    def bounceX(self):
        self.xMove *= -1
        if (self.moveSpeed > 0.025):
            self.moveSpeed *= 0.9
        else:
            self.moveSpeed = 0.025

    def reset(self):
        self.body.goto(x=0, y=0)
        self.bounceX()