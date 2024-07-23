"""
Aim: Printing all the shapes using turtle class.
Author: Mehdiali
Date: 21 / June / 2024 - 06:39 PM
"""

from turtle import Turtle, Screen
from random import randint



myTurtle = Turtle()
myTurtle2 = Turtle()
myScreen = Screen()

myTurtle.speed("fast")
myTurtle2.speed("fast")
myScreen.bgcolor("grey")

colors = ["aquamarine", "blue", "chartreuse", "cyan", "DarkSeaGreen", "brown", "chocolate", "LightPink", "DodgerBlue4", "gold", "orange"]

myTurtle.backward(30)
myTurtle2.backward(30)

for shapes in range(3, 11):
    randomNumber = randint(0, len(colors) - 1)
    color = colors[randomNumber]
    myTurtle.pencolor(color)
    myTurtle2.pencolor(color)
    for _ in range(0, shapes):
        myTurtle.forward(100), myTurtle2.forward(100)
        myTurtle.right(360 / shapes), myTurtle2.left(360 / shapes)


myScreen.exitonclick()