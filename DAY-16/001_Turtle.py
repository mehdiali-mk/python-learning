"""
Aim: Turtle Class and its Objects.
Author: Mehdiali
Date: 20 / June / 2024 - 03:42 PM
"""

from turtle import Turtle, Screen

myTurtle = Turtle()
print(myTurtle)
myTurtle.shape("turtle")
myTurtle.color("blue")
myTurtle.shapesize(3)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(135)
myTurtle.forward(150)

myScreen = Screen()
print(myScreen.canvheight)
# myScreen.bgcolor("black")
myScreen.exitonclick()