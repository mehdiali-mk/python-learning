"""
Aim: Calculator App.
Author: Mehdiali
Date: 13 / June / 2024 - 09:19 PM
"""

import os

# Here is the function of addition.
def addition(num1, num2):
    return num1 + num2

# Here is the function of subtraction.
def subtraction(num1, num2):
    return num1 - num2

# Here is the function of multiplication.
def multiplication(num1, num2):
    return num1 * num2

# Here is the function of division
def division(num1, num2):
    return num1 / num2

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

os.system("cls")
print("\nWelcome to the calculator app.\n")
def calculator():
    num1 = float(input("Enter the 1st number = "))

    while True:
        print("Operations you can choose =", end=" ")
        for key in operations:
            print(f"{key}", end= ", ")

        print("\n")

        while True:
            operationSymbol = input("Enter your operation = ")

            if (operationSymbol == "+" or operationSymbol == "-" or operationSymbol == "*" or operationSymbol == "/"):
                break
            else:
                print("\nEnter the valid operation.")
                
        num2 = float(input("Enter the 2nd number = "))



        answer = operations[operationSymbol](num1, num2)

        print(f"\n{num1} {operationSymbol} {num2} = {answer}\n")

        print("""\nPress ("Y") to calculate with the last answer.""")
        print("""Press ("N") for the fresh calculation.""")
        print("""Press ("E") for EXIT.""")
        while True:
            repeat = input(f"What is your choice = ").lower()

            if (repeat == "y" or repeat == "n" or repeat == "e"):
                break
            else:
                print("\nPlease enter the correct choice.")

        if (repeat == "y"):
            num1 = answer
            os.system("cls")
            print(f"\nYour last answer = {answer}")
        elif (repeat == "n"):
            os.system("cls")
            calculator()
        else:
            break

calculator()