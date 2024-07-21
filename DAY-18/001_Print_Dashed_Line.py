"""
Aim: Print Dashed Line using turtle class.
Author: Mehdiali
Date: 21 / June / 2024 - 06:39 PM
"""

from turtle import Turtle, Screen

myTurtle = Turtle()
myScreen = Screen()

for _ in range(4):
    for _ in range(5):
        myTurtle.pendown()
        myTurtle.forward(20)
        myTurtle.penup()
        myTurtle.forward(20)

    myTurtle.left(90)

myScreen.exitonclick()