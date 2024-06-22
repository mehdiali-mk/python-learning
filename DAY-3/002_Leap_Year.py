"""
Aim: Leap Year or not
Author: Mehdiali
Date: 08 / June / 2024 - 12:08 PM
"""

print("Leap year or not.")
yearToCheck = int(input("Enter the year to check = "))

if (yearToCheck % 4 == 0):
    if (yearToCheck % 100 == 0):
        if (yearToCheck % 400 == 0):
            print(f"\n{yearToCheck} is a Leap Year.")
        else:
            print(f"\n{yearToCheck} is not a Leap Year.")
    else:
        print(f"\n{yearToCheck} is a Leap Year.")
else:
    print(f"\n{yearToCheck} is not a Leap Year.")
