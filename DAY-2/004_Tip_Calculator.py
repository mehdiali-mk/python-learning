"""
Aim: Tip Calculator
Author: Mehdiali
Date: 07 / June / 2024 - 04:27 PM
"""

print("\n\nWelcome to Tip Calculator App.")

totalBill = float(input("\nEnter your total bill = "))

percentageOfTip = int(input("Enter the percentage of Tip to give, 10, 12 or 15 = "))

peoplesToSplit = int (input("Enter the number of members to split the bill = "))

billWithTip = round(totalBill + totalBill * (percentageOfTip / 100), 2)
eachToPay = billWithTip / peoplesToSplit

print(f"\nTotal bill including tip = {billWithTip}")
print(f"Each Person should pay: {eachToPay}\n\n")
