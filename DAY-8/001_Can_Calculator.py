"""
Aim: Can Calculator.

You are painting a wall. The instructions on the paint can says that 1 can of pant can cover 5 square meters of wall. Give a random height and width of wall, calculate hoy many cans of paint you'll need to buy

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

Author: Mehdiali
Date: 12 / June / 2024 - 03:12 PM
"""

# Function
def calculateNumberOfCans(height, width, coverage):
    areaOfWall = (height * width)
    numberOfCans = round(areaOfWall / coverage)

    print(f"\n{numberOfCans} number of cans required to paint the wall with area of {int(areaOfWall)}m per square.")



heightOfWall = float(input("Enter the height of your wall = "))
widthOfWall = float(input("Enter the width of your wall = "))
coveraceDoneByCan = 5

calculateNumberOfCans(heightOfWall, widthOfWall, coveraceDoneByCan)
