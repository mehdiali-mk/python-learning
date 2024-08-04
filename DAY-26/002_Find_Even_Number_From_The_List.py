"""
Aim: Find all even numbers from a list using list comprehension without for loop.
Author: Mehdiali
Date: 29 / June / 2024 - 08:33 PM
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
numberList = [findFibonacci(num) for num in range(1, 11)]

# Here the the list comprehension to minimize the code.
# Syntax = [newItem for item in list if condition]
evenNumberList = [num for num in numberList if (num % 2 == 0)]

print(f"\n\nOriginal List = {numberList}\n")
print(f"Even Number List = {evenNumberList}\n\n")


