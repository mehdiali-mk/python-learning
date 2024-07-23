"""
Aim: Printing all the shapes using turtle class.
Author: Mehdiali
Date: 21 / June / 2024 - 06:39 PM
"""

from turtle import Turtle, Screen
from random import randint

myTurtle = Turtle()
myTurtle2 = Turtle()
myTurtle3 = Turtle()
myScreen = Screen()

myTurtle.speed("fastest")
myTurtle2.speed("fastest")
myTurtle3.speed("fastest")
myScreen.bgcolor("black")

colors = ["aquamarine", "blue", "chartreuse", "cyan", "DarkSeaGreen", "brown", "chocolate", "LightPink", "DodgerBlue4", "gold", "orange"]

myTurtle.backward(200)
myTurtle2.backward(100)
myTurtle3.backward(150)
myTurtle3.sety(50)
myTurtle.pencolor(colors[3])
myTurtle2.pencolor(colors[7])
myTurtle3.pencolor(colors[9])

for _ in range(90):
    myTurtle.forward(8)
    myTurtle.left(4)
    myTurtle2.forward(8)
    myTurtle2.left(4)
    myTurtle3.forward(2)
    myTurtle3.left(4)

myTurtle.left(90)
myTurtle2.left(90)
myTurtle.forward(50)
myTurtle2.forward(50)

for _ in range(45):
    myTurtle.forward(16)
    myTurtle.left(8)
    myTurtle2.forward(16)
    myTurtle2.right(8)

for _ in range(90):
    myTurtle.forward(8)
    myTurtle.right(4)
    myTurtle2.forward(8)
    myTurtle2.left(4)

myScreen.exitonclick()