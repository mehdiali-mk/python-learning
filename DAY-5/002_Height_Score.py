"""
Aim: Find the highest score from the list.
Author: Mehdiali
Date: 10 / June / 2024 - 06:38 PM
"""

studentsScore = input("""Enter the score of students separated by " " =  """).split(" ")

for index in range(0, len(studentsScore)):
    studentsScore[index] = int(studentsScore[index])

highestScore = studentsScore[0]
for score in studentsScore:
    if (score > highestScore):
        highestScore = score

print(f"\nThe highest score in the class is: {highestScore}")