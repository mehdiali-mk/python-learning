import time
from turtle import Screen
from Player import Player
from carManager import CarManager
from Scoreboard import Scoreboard

myScreen = Screen()
myScreen.setup(width=600, height=600)
myScreen.tracer(0)
    
myTurtle = Player()
myCars = CarManager()
myScoreboard = Scoreboard()

myScreen.listen()
myScreen.onkeypress(myTurtle.move, "Up")

isGameOn = True
while isGameOn:
    time.sleep(0.1)
    myScreen.update()

    myCars.createCar()
    myCars.moveCars()

    for cars in myCars.allCars:
        if (cars.distance(myTurtle) < 20):
            myScoreboard.gameOver()
            isGameOn = False

    if (myTurtle.isFinished()):
        myTurtle.setStartPosition()
        myCars.levelUp()
        myScoreboard.levelUp()


myScreen.exitonclick()