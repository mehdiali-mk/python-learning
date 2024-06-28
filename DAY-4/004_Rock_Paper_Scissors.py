"""
Aim: Rock Paper Scissors Game.
Author: Mehdiali
Date: 09 / June / 2024 - 02:53 PM
"""

import os
import random
os.system("cls")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choicesToChoice = [rock, paper, scissors]


print("Welcome to the Rock Paper Scissors Game:\nChoose the following number to play the game as:\n1 -> Rock\n2 -> Paper\n3 -> Scissors.\n")

while True:
    userChoice = int(input("Enter your choice = ")) - 1

    if (userChoice >= 0 and userChoice <= 2):
        break
    else:
        print("\nPlease Enter the correct choice.")
    
computerChoice = random.randint(0, 2)

print("\nYou Choice:")

print(choicesToChoice[userChoice])

print("\nComputer Choice:")

print(choicesToChoice[computerChoice])


if (userChoice == computerChoice):
    print("\nIt's draw")
elif (userChoice == 0 and computerChoice == 2):
    print("\nYou Win!!!, Computer Loose.")
elif (userChoice == 2 and computerChoice == 0):
    print("\nYou Loose, Computer Win!!!")
elif (userChoice > computerChoice):
    print("\nYou Win!!!, Computer Loose.")
elif (userChoice < computerChoice):
    print("\nYou Loose, Computer Win!!!")
else:
    print("\n~~ERROR~~")

# [rock, paper, scissors]
#   0     1       2