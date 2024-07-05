"""
Aim: Find the Days of Month in a particular year.
Author: Mehdiali
Date: 13 / June / 2024 - 05:29 PM
"""

def isLeapYear(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def daysInMonth(year, month):
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (isLeapYear(year) and month == 2):
        return 29
    else:
        return daysOfMonths[month - 1]
    

year = int(input("Enter the year = "))

while True:
    month = int(input("Enter the month = "))

    if (month >= 1 and month <= 12):
        break
    else:
        print("\nPlease enter the correct month number between 1 to 12.")

print(f"\nThe number of days in {month} = {daysInMonth(year, month)}")
