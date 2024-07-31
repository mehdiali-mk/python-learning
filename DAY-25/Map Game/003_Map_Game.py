"""
Aim: Map Game (Guess the name of Indian Sates)
Author: Mehdiali
Date: 29 / June / 2024 - 01:45 PM
"""

import turtle
import pandas

myScreen = turtle.Screen()
myScreen.title("Guess the name of Indian States.")
imagePath = "DAY-25\Map Game\indianMap-01.gif"
myScreen.addshape(imagePath)
turtle.shape(imagePath)
myScreen.setup(width=800, height=800)
myScreen.tracer(0)

indianStatesData = pandas.read_csv("DAY-25\Map Game\Indian States.csv")

statesName = indianStatesData["State"].tolist()
xCordinates = indianStatesData["X"].tolist()
yCordinates = indianStatesData["Y"].tolist()

guessedStates = []

def plotTheState(stateName):
    index = statesName.index(stateName)
    x = xCordinates[index]
    y = yCordinates[index]
    myTurtle = turtle.Turtle()
    myTurtle.penup()
    myTurtle.goto(x,y)
    myTurtle.hideturtle()
    myTurtle.write(f"{stateName}", align="center", font=("Arial", 8, "normal"))
    myScreen.update()

myScoreTurtle = turtle.Turtle()

def displayScore():
    myScoreTurtle.clear()
    myScoreTurtle.penup()
    myScoreTurtle.goto(-325,325)
    myScoreTurtle.hideturtle()
    myScoreTurtle.write(f"{len(guessedStates)} / 37", align="center", font=("Arial", 24, "normal"))
    myScreen.update()

displayScore()
myScreen.update()
while len(guessedStates) < 37:
    userGuess = myScreen.textinput(f"{len(guessedStates)} / 37 States correct!", "Enter the name of Indian State: ").title()

    if userGuess == "Exit":
        missingState = []
        for state in statesName:
            if state not in guessedStates:
                missingState.append(state)
        myScreen.bye()
        break
    if userGuess in statesName:
        plotTheState(stateName=userGuess)
        guessedStates.append(guessedStates)
        displayScore()
