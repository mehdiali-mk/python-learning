from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        randomX = random.randint(-260, 260)
        randomY = random.randint(-260, 260)

        self.goto(randomX, randomY)