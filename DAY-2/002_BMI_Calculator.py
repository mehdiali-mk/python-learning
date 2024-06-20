"""
Aim: BMI Calculator
Author: Mehdiali
Date: 07 / June / 2024 - 03:43 PM
"""

print("Welcome to BMI Calculator.\n")

weight = float(input("Enter your weight in (Kg) = "))
height = float(input("Enter your height in (m) = "))

bmi = round(weight / (height ** 2), 2)

print("\nYour BMI is:", bmi)

if (bmi < 18.5):
    print("You are in Under Weight.")
elif (bmi >= 18.5 and bmi < 25):
    print("You are in Normal Weight.")
elif (bmi >= 25 and bmi < 30):
    print("You are in Over Weight.")
elif (bmi > 30):
    print("You are Obese.")
else:
    print("\n~!ERROR~\nPlease enter the correct weight and height.")
