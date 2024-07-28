from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakeBody = []
        self.createSnake()
        self.head = self.snakeBody[0]
    
    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.addSnakeBody(position)

    
    def addSnakeBody(self, position):
        newTurtle = Turtle("square")
        newTurtle.penup()
        newTurtle.color("white")
        newTurtle.goto(position)

        self.snakeBody.append(newTurtle)

    def extendBody(self):
        self.addSnakeBody(self.snakeBody[-1].position())

    def move(self):
        for snakePieceNumber in range(len(self.snakeBody) - 1, 0, -1):
            newX = self.snakeBody[snakePieceNumber - 1].xcor()
            newY = self.snakeBody[snakePieceNumber - 1].ycor()
            self.snakeBody[snakePieceNumber].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)