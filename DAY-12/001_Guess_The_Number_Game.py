"""
Aim: Guess The number.
Author: Mehdiali
Date: 16 / June / 2024 - 05:01 PM
"""


from guessArt import mainLogo
import os
import random

os.system("cls")
print(mainLogo)



GUESSED_NUNBER = random.randint(1, 100)
numberOfAttempts = 0

print("\nWelcome, to Guess The Number game.")
while True:
    diffecultLevel = input("Choose the medium of level (low / hard): ").lower()

    if diffecultLevel == "low" or diffecultLevel == "hard":
        break
    print("\nPlease choose the appropriate choice.")

if (diffecultLevel == "low"):
    numberOfAttempts = 10
else:
    numberOfAttempts = 5

while True:
    print(f"\nYou have {numberOfAttempts} remaining to guess the number.")

    userGuess = int(input("Make a guess = "))

    if (userGuess == GUESSED_NUNBER):
        print(f"\nYou got it! The answer was = {GUESSED_NUNBER}")
        break
    elif (userGuess > GUESSED_NUNBER):
        print(f"Your guess is TOO HIGH.")
        numberOfAttempts -= 1
    elif (userGuess < GUESSED_NUNBER):
        print(f"Your guess is TOO LOW.")
        numberOfAttempts -= 1
    else:
        print("\n~~ERROR~~")

    if (numberOfAttempts == 0):
        print("\nYou loose,\nyou don't have any attempts.")
        break
    

