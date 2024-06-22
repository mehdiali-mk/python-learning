"""
Aim: Rollercoaster ticket management.
Author: Mehdiali
Date: 08 / June / 2024 - 12:13 PM
"""

print("\nWelcome to the Rollercoaster Ticket management app.\n")


height = float(input("Enter your height in (cm) = "))


if (height >= 120):
    age = int(input("Enter your age = "))
    if (age < 12):
        totalPrice = 5
    elif (age >= 12 and age < 18):
        totalPrice = 7
    elif (age >= 18 and age < 45):
        totalPrice = 12
    elif (age >= 45 and age < 55):
        totalPrice = 0
    else:
        print("Please Enter the correct age.")
    
    if (totalPrice != 0):
        while True:
            isPhoto = input("Do you what to take Photo (Y/N) = ")
            if (isPhoto == "y" or isPhoto == "Y" or isPhoto == "n" or isPhoto == "N"):
                break
            else:
                print("\nPlease enter correct choice.")
    else:
        isPhoto = "n"

    if (isPhoto == "y" or isPhoto == "Y"):
        totalPrice += 3
        print(f"\nYour ticket price = {totalPrice}")
    else:
        print(f"\nYour ticket price = {totalPrice}")
else:
    print("\nSORRY! You are not eligible for this ride.")