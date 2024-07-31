# To take cordinates.
# xCordinates = []
# yCordinates = []

# def getXY(x, y):
#     xCordinates.append(x)
#     yCordinates.append(y)
#     print(xCordinates, yCordinates)


# turtle.onscreenclick(getXY)
# turtle.mainloop()



# To check the placement of cordinates

# indianStatesData = pandas.read_csv("DAY-25\Map Game\Indian States.csv")

# xCordinates = indianStatesData.X.tolist()
# yCordinates = indianStatesData.Y.tolist()


# for count in range(0, len(xCordinates)):
#     myTurtle = turtle.Turtle()
#     myTurtle.penup()
#     myTurtle.shapesize(stretch_wid=0.4, stretch_len=0.4)
#     myTurtle.speed("fastest")
#     myTurtle.shape("circle")
#     myTurtle.goto(xCordinates[count], yCordinates[count])




# Here is the code for plot the name of state.
# statesName = indianStatesData["State"].tolist()
# xCordinates = indianStatesData["X"].tolist()
# yCordinates = indianStatesData["Y"].tolist()

# numberOfStates = len(statesName)


# for count in range(0, numberOfStates):
#     myTurtle = turtle.Turtle()
#     myTurtle.speed("fastest")
#     myTurtle.penup()
#     myTurtle.goto(xCordinates[count],yCordinates[count])
#     myTurtle.hideturtle()
#     myTurtle.write(f"{statesName[count]}", align="center", font=("Arial", 8, "normal"))