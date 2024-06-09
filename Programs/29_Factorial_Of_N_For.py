"""
Aim: Factorial of given number using for loop.
Author: Mehdiali
Date: 31 / May / 2024 - 05:40 PM
"""

number = int(input("Enter the number = "))

fact = 1

for i in range(1, number+1):
    fact *= i

print("The factorial =", fact)
