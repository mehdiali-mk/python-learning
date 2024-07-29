from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, xCordinate, yCordinate):
        super().__init__()
        self.body = Turtle()
        self.body.shape("square")
        self.body.color("white")
        self.body.penup()
        self.body.speed("fastest")
        self.body.shapesize(stretch_wid=1, stretch_len=5)
        self.body.goto(x=xCordinate, y=yCordinate)
        self.body.setheading(90)
        self.drawBox()
    
    def moveUp(self):
        self.body.forward(20)
    
    def moveDown(self):
        self.body.backward(20)

    def drawBox(self):
        box = Turtle()
        box.hideturtle()
        box.penup()
        box.color("white")
        box.speed("fastest")
        box.goto(-400,-300)
        box.pendown()
        box.goto(400,-300)
        box.goto(400,300)
        box.goto(-400,300)
        box.goto(-400,-300)