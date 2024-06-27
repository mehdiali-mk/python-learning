"""
Aim: Treasure Map
Author: Mehdiali
Date: 09 / June / 2024 - 02:53 PM
"""

import os
os.system("cls")



row1 = ["💀", "💀", "💀"]
row2 = ["💀", "💀", "💀"]
row3 = ["💀", "💀", "💀"]

map = [row1, row2, row3]

print(f"\n\n{row1}\n{row2}\n{row3}")

while True:
    position = input("Where do you want to put the treasure?\nEnter the position = ")

    if (int(position[0]) >= 1 and int(position[1]) >= 1 and int(position[0]) <= 3 and int(position[1]) <= 3):
        break
    else:
        print("\nPlease choose the correct position.")

positionOfColumn = int(position[0])-1
positionOfRow = int(position[1])-1


map[positionOfRow][positionOfColumn] = "💛"
row1 = map[0]
row2 = map[1]
row3 = map[2]

print(f"\n\n{row1}\n{row2}\n{row3}")