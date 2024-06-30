"""
Aim: Hangman Game
Author: Mehdiali
Date: 11 / June / 2024 - 06:31 PM
"""

import random
import os

from hangman_package import (stages)
from hangman_package import (logo)

life = len(stages)
print(life)

from hangman_package import (listOfWords)
chosenWord = random.choice(listOfWords)

answerOfList = []
answerOfList += "_" * len(chosenWord)

print(f"The final answer is = {chosenWord}")



def takeAndCheck(lives):
    os.system("cls")
    print(logo)

    print(stages[lives - 1])
    print(f"\nThe word you are guessing = {displayGuessingWord()}")
    guess = input("Guess a letter = ").lower()

    if (chosenWord.find(guess) == -1):
        lives = lives - 1

    for count in range(0, len(chosenWord)):
        if (guess == chosenWord[count]):
            answerOfList[count] = guess

    return lives

def displayGuessingWord():
    guessingWord = ""

    for letter in answerOfList:
        guessingWord += letter
    
    return guessingWord

def checkBlank():
    count = 0
    
    for letter in (answerOfList):
        if (letter == "_"):
            count += 1
    return count
    

while checkBlank() > 0:
    if life > 1:
        life = takeAndCheck(life)
    else:
        os.system("cls")
        print(stages[life - 1])
        print("You Lose")
        break

if (life > 1):
    os.system("cls                                                              ")
    print("\nWOW, You Win!!!.")
    print(f"You have guessed the correct word '{displayGuessingWord()}'")