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
Date: 24 / June / 2024 - 07:34 AM
"""


from turtle import Turtle, Screen
import time
from snakeClass import Snake

# Setup a screen.
myScreen = Screen()
myScreen.setup(width=600, height=600)
myScreen.title("Snake Game.")
myScreen.bgcolor("black")
myScreen.tracer(0)

mySnake = Snake()

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
    

myScreen.exitonclick()