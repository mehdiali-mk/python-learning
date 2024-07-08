"""
Aim: Higher Lower Game.
Author: Mehdiali
Date: 18 / June / 2024 - 07:16 PM
"""

import os
import random
from art import logo
from art import vs
from art import gameOver
from gameData import data


# This function returns the random number.
def getRandomNumber():
    return random.randint(0, len(data) - 1)

# This function returns 2 data.
def takeData():
    firstIndex = getRandomNumber()
    while True:
        secondIndex = getRandomNumber()
        if (secondIndex != firstIndex):
            break
    mainData = []
    mainData.append(data[firstIndex])
    mainData.append(data[secondIndex])

    return mainData
    
# This function displays the question.
def askQuestion(question):
    question1 = question[0]
    question2 = question[1]
    print(f"Compare A: {question1["name"]}, a {question1["description"]}, from {question1["country"]}")

    print(vs)

    print(f"\nCompare B: {question2["name"]}, a {question2["description"]}, from {question2["country"]}")


# This funciton retuns the correct answer.
def findAnswer(data):
    correctAnswer = ""
    if (data[0]["follower_count"] > data[1]["follower_count"]):
        correctAnswer = "A"
    elif (data[1]["follower_count"] > data[0]["follower_count"]):
        correctAnswer = "B"
    else:
        print("\nBoth have same followers!!")
    
    return correctAnswer

score = 0

while True:
    os.system("cls")
    print(logo)
    mainData = takeData()

    if (score != 0):
        print(f"You're right! Current Score = {score}")

    askQuestion(mainData)

    while True:
        userChoice = input("""\nWho has more followers? Type 'A' or 'B' = """).upper()

        if (userChoice == "A" or userChoice == "B"):
            break
        else:
            print("\nPlease enter the correct choice.")

    answer = findAnswer(mainData)

    if (userChoice == answer):
        score = score + 1
    else:
        break

os.system("cls")
print(gameOver)
print(f"\nSorry, That's wrong. Final Score: {score}")