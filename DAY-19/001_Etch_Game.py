"""
Aim: Etch a Sketch Game.
Author: Mehdiali
Date: 23 / June / 2024 - 02:47 PM
"""

import turtle

myTurtle = turtle.Turtle()
myScreen = turtle.Screen()

penSize = 0

def forwardT():
    myTurtle.forward(20)
def backwardT():
    myTurtle.backward(20)
def leftT():
    newHeading = myTurtle.heading() + 10
    myTurtle.setheading(newHeading)
def rightT():
    newHeading = myTurtle.heading() - 10
    myTurtle.setheading(newHeading)
def clear():
    myTurtle.clear()
    myTurtle.penup()
    myTurtle.home()
    myTurtle.pendown()

turtle.onkey(forwardT, "Up")
turtle.onkey(backwardT, "Down")
turtle.onkey(leftT, "Left")
turtle.onkey(rightT, "Right")
turtle.onkey(clear, "c")

turtle.listen()

# myTurtle.onkeypress({
#     myTurtle.backward(10)
# }, "s")


myScreen.exitonclick()