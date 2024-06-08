"""
Aim: Multiplication table.
Author: Mehdiali
Date: 31 / May / 2024 - 04:41 PM
"""


number = int(input("Enter the number = "))

count = 1

while (count <= 10):
    print(number, "x", count, "=",count * number)
    count += 1
