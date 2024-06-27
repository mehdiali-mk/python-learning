"""
Aim: Banker Roulette.
Author: Mehdiali
Date: 09 / June / 2024 - 02:30 PM
"""

import random

names = input("Enter names separated by comma: ")
namesList = names.split(", ")

indexOfName = random.randint(0, len(namesList) - 1)

print(f"\n{namesList[indexOfName]} is going to buy the meal today!")