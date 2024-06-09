"""
Aim: Sum of N number using while.
Author: Mehdiali
Date: 31 / May / 2024 - 05:37 PM
"""

number = int(input("Enter the number = "))

sumOfN = 0
count = 0

while (count <= number):
    sumOfN += count
    count += 1

print("The sum =", sumOfN)
