"""
Taking inputs form user and print it.
Author: Mehdiali
Date: 29 / May / 2024 - 02:57 PM
"""

color = input("Enter the color of Light = ")

if (color == "red"):
    print("It indicates Stop")
elif(color == "yellow"):
    print("It indicates Wait.")
elif(color == "green"):
    print("It indicates Go.")
else:
    print("Light is broken.")

print("\n\nAnother example.")
marks = int(input("Enter the marks = "))

if (marks >= 90):
    print("\nYou got 'A' grade.")
elif (marks >= 80 and marks < 90):
    print("\nYou got 'B' grade.")
elif(marks >= 70 and marks < 80):
    print("\nYou got 'C' grade.")
else:
    print("You got D grade.")

print("\n\nAnother example.")
food = input("Enter the food = ")
eatOrNot = "Yes, I can eat." if (food == "cake") else "No, I cannot eat."
print(eatOrNot)

food = input("Enter the food = ")
print("It is sweet.") if (food == "cake") or (food == "jalebi") else print("It is not sweet.")

print("\n\nAnother example.")
age = int(input("Enter the age = "))
vote = ("no", "yes") [age >= 18]
print(vote)

income = int(input("Enter your income = "))
tax = income * (0.1, 0.2) [income >= 50000]
print("Your tax =", tax)