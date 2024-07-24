"""
Aim: Random Directions using turtle class.
Author: Mehdiali
Date: 21 / June / 2024 - 08:42 PM
"""

from turtle import Turtle, Screen
from random import randint

myTurtle = Turtle()
myScreen = Screen()
myScreen.bgcolor("black")

colors = ["aquamarine", "blue", "chartreuse", "cyan", "DarkSeaGreen", "brown", "chocolate", "LightPink", "DodgerBlue4", "gold", "orange"]

direction = [0, 90, 180, 270]
myTurtle.pensize(15)
myTurtle.speed("fastest")
for _ in range(500):
    directionNumber = randint(0, 3)
    color = colors[randint(0, len(colors) - 1)]
    myTurtle.color(color)
    myTurtle.forward(50)
    myTurtle.left(direction[directionNumber])



myScreen.exitonclick()