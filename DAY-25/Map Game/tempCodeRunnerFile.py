xCordinates = indianStatesData.X.tolist()
yCordinates = indianStatesData.Y.tolist()


for count in range(0, len(xCordinates) - 1):
    myTurtle = turtle.Turtle()
    myTurtle.penup()
    myTurtle.shapesize(stretch_wid=0.4, stretch_len=0.4)
    myTurtle.speed("fastest")
    myTurtle.shape("circle")
    myTurtle.goto(xCordinates[count], yCordinates[count])