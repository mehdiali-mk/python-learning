"""
Aim: Random Directions using turtle class.
Author: Mehdiali
Date: 21 / June / 2024 - 09:19 PM
"""
from turtle import Turtle, Screen, colormode
from random import randint

myTurtle = Turtle()
myScreen = Screen()
myScreen.bgcolor("black")
myTurtle.speed("fastest")
colormode(255)

def generateColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b) 
    return color

def drawSpirograph(gap):
    for _ in range(int(360 / gap)):
        myTurtle.color(generateColor())
        myTurtle.circle(150)
        myTurtle.setheading(myTurtle.heading() + gap)

drawSpirograph(5)

myScreen.exitonclick()