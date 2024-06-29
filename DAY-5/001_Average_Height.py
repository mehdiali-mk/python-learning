"""
Aim: Calculate Average Height.
Author: Mehdiali
Date: 10 / June / 2024 - 06:31 PM
"""

heightOfStudents = [180, 124, 165, 173, 189, 169, 146]

totalheight, numberOfStudents = 0, 0 
for height in heightOfStudents:
    totalheight += height
    numberOfStudents += 1


averageHeight = round(totalheight / numberOfStudents, 2)

print(f"The average height is {averageHeight}")