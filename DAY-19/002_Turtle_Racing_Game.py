"""
Aim: Turtle Racing Game.
Author: Mehdiali
Date: 23 / June / 2024 - 04:43 PM
"""

# import turtle
from turtle import Turtle, Screen
from random import randint

myScreen = Screen()
myScreen.setup(width=500, height=400)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]

while True:
    userChoice = myScreen.textinput(title="Make your choice.", prompt="Which turtle will win the race? Enter the color:\nred, orange, yellow, green, blue, or purple\n\n").lower()

    if colors.count(userChoice) == 0:
        print("\nEnter the correct choice")
    else:
        break


distances = [25, -25, 100, -100, 150, -150]
myTurtle = []

finishLine = Turtle()
finishLine.speed("fastest")
finishLine.penup()
finishLine.goto(x=210, y=200)
finishLine.right(90)
finishLine.pendown()
finishLine.goto(x=210, y=-210)
finishLine.penup()

for index in range(0, 6):
    myNewTurtle = Turtle(shape="turtle")
    myNewTurtle.color(colors[index])
    myNewTurtle.penup()
    myNewTurtle.goto(x = -230, y = distances[index])

    myTurtle.append(myNewTurtle)

raceOn = True
while raceOn:

    for turtle in myTurtle:
        if turtle.xcor() > 185:
            raceOn = False
            winnerTurtleColor = turtle.pencolor()   
            if (winnerTurtleColor == userChoice):
                print(f"\n\nYou have win the race!!\nThe {winnerTurtleColor} turtle is the winner.\n\n")
            else:
                print(f"\n\nYou have loose the race!!\nThe {winnerTurtleColor} turtle is the winner.\n\n")

        randomDistance = randint(1, 10)
        turtle.forward(randomDistance)


myScreen.exitonclick()