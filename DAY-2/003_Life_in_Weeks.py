"""
Aim: Life in weeks. (Take current age as an input and calculate days, weeks, and months left to live upto 90 years)
Author: Mehdiali
Date: 07 / June / 2024 - 04:15 PM
"""

print("\nLife in week.")

currentAge = int(input("Enter your current age = "))

yearsLeft = 90 - currentAge
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

print(f"\nYour have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")