"""
Aim: Square of Each List Items using list comprehension without for loop
Author: Mehdiali
Date: 29 / June / 2024 - 08:15 PM
"""

import os
os.system("cls")

def findFibonacci(number):
    a, b = 1, 0
    count = 0
    sumOfNum = 0
    while (number > count):
        sumOfNum = a + b
        a = b
        b = sumOfNum
        count += 1
    return sumOfNum

# Here the the list comprehension to minimize the code.
# Syntax = [newItem for item in list]
number = [findFibonacci(num) for num in range(1, 11)]

squareOfNumber = [num ** 2 for num in number]

print(f"\n\nOriginal List = {number}\n")
print(f"Squared List = {squareOfNumber}\n\n")


