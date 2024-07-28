"""
Aim: 7 Steps to build snake game.

1. Create a snake body.
2. Move the snake.
3. Create snake food.
4. Detect collision with food.
5. Create a scoreboard.
6. Detect collision with wall.
7. Detect collision with snake body.

Author: Mehdiali
Date: 25 / June / 2024 - 12:16 PM
"""


from turtle import Turtle, Screen
import time
from snakeClass import Snake
from foodClass import Food
from scoreboardClass import Scoreboard

# Setup a screen.
myScreen = Screen()
myScreen.setup(width=600, height=600)
myScreen.title("Snake Game.")
myScreen.bgcolor("black")
myScreen.tracer(0)

mySnake = Snake()
myFood = Food()
myScoreboard = Scoreboard()

# Updating the screen graphics.
myScreen.update()


# Control the snake body using arrows.
myScreen.listen()
myScreen.onkey(mySnake.up, "Up")
myScreen.onkey(mySnake.down,"Down")
myScreen.onkey(mySnake.left, "Left")
myScreen.onkey(mySnake.right, "Right")

# Moving the snake
isGameOn = True

while isGameOn:
    myScreen.update()
    time.sleep(0.12)

    mySnake.move()

    if (mySnake.head.distance(myFood) < 15):
        myFood.refresh()
        mySnake.extendBody()
        myScoreboard.increaseScore()

    mySnakeX = mySnake.head.xcor()
    mySnakeY = mySnake.head.ycor()

    if (mySnakeX > 280 or mySnakeX < -280 or mySnakeY > 280 or mySnakeY < -280):
        isGameOn = False
        myScoreboard.gameOver()

    for body in mySnake.snakeBody[1:]:
        if (mySnake.head.distance(body) < 10):
            isGameOn = False
            myScoreboard.gameOver()
    

myScreen.exitonclick()