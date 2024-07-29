"""
Aim: 8 Steps to build Pong Game.

1. Create the Screen.
2. Create and move a paddle
3. Create another paddle.
4. Create the ball and make it move.
5. Detect collision with wall and bounce.
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep score

Author: Mehdiali
Date: 26 / June / 2024 - 07:26 AM
"""

from turtle import Turtle, Screen
from paddles import Paddle
from ball import PongBall
import time
from scoreboard import ScoreBoard

myScreen = Screen()
myScreen.bgcolor("black")
myScreen.setup(width=800,height=600)
myScreen.title("Pong Game : by Mehdiali Kadiwala")
myScreen.listen()
myScreen.tracer(0)

myPaddleRight = Paddle(xCordinate=350, yCordinate=0)
myPaddleLeft = Paddle(xCordinate=-350, yCordinate=0)
myBall = PongBall()
myScoreboard = ScoreBoard()

myScreen.onkeypress(myPaddleRight.moveUp, "Up")
myScreen.onkeypress(myPaddleRight.moveDown, "Down")

myScreen.onkeypress(myPaddleLeft.moveUp, "w")
myScreen.onkeypress(myPaddleLeft.moveDown, "s")

isGameOn = True

while isGameOn:
    time.sleep(myBall.moveSpeed)
    myScreen.update()
    myBall.move()

    if (myBall.body.ycor() > 280 or myBall.body.ycor() < -280):
        myBall.bounceY()
    

    if (myBall.body.distance(myPaddleRight.body) < 70 and myBall.body.xcor() == 320) or (myBall.body.distance(myPaddleLeft.body) < 70 and myBall.body.xcor() == -320):
        myBall.bounceX()

    elif (myBall.body.xcor() > 420):
        myBall.reset()
        myScoreboard.scoreOfLeftPlayer += 1
    elif (myBall.body.xcor() < -420):
        myBall.reset()
        myScoreboard.scoreOfRightPlayer += 1
    
    myScoreboard.updateScore()

myScreen.exitonclick()