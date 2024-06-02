"""
Greatest among three number
Author: Mehdiali
Date: 29 / May / 2024 - 10:34 PM
"""

num1 = int(input("Enter the 1st number = "))
num2 = int(input("Enter the 2nd number = "))
num3 = int(input("Enter the 3rd number = "))

if (num1 > num2):
    if (num1 > num3):
        print(num1, "is greatest number.")
    else:
        print(num3, "is greatest number.")
else:
    if (num2 > num3):
        print(num2, "is greatest number.")
    else:
        print(num3, "is greatest number.")