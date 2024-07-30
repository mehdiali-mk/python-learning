from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):

    def __init__(self):
        self.allCars = []
        self.carSpeed = STARTING_MOVE_DISTANCE
    
    def createCar(self):
        choice = random.randint(1,6)
        if (choice == 1):
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randomY = random.randint(-250, 250)
            newCar.goto(300, randomY)
            self.allCars.append(newCar)        

    def moveCars(self):
        for cars in self.allCars:
            cars.backward(self.carSpeed)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT