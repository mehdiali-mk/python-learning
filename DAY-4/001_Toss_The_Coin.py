"""
Aim: Toss the coin for Heads and Tails.
Author: Mehdiali
Date: 09 / June / 2024 - 09:38 PM
"""

import random

randomChoice = random.randint(0,1)

print("\nWelcome,\n")

while True:
    userChoice = input("""Choose "Heads" or "Tails" = """).lower()

    if (userChoice == "heads" or userChoice == "tails"):
        break
    else:
        print("\nPlease Choose correct choice.")

if (randomChoice == 0 and userChoice == "heads"):
    print("\nCoin gets: Heads\nYou Win...")
elif (randomChoice == 1 and userChoice == "tails"):
    print("\nCoin gets: Tails\nYou Win...")
elif (randomChoice == 0 and userChoice == "tails"):
    print("\nCoin gets: Heads\nYou Loose...")
elif (randomChoice == 1 and userChoice == "heads"):
    print("\nCoin gets: Tails\nYou Loose...")
else:
    print("\n\n~~ERROR~~")

                   