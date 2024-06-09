"""
Aim: Functions Practice Questions.
Author: Mehdiali
Date: 01 / June / 2024 - 10:17 AM
"""

def findLength(myList):
    count = 0
    for element in myList:
        count += 1
    
    return count

myList = [1,3,4,5,6,2]

print(myList)
print("Length of List =", findLength(myList))

def printElement(myList):
    for element in myList:
        print(element, end=", ")

printElement(myList)

def findFactorial(number):
    if (number <= 1):
        return 1
    return number * findFactorial(number - 1)

print("\nFactorial of 5 =", findFactorial(5))



def convertUSDtoINR(dollars):
    return dollars * 85

print("120 Dollars =", convertUSDtoINR(120), "Rupees")

number = 8

def findOddEven(number):
    if (number % 2 == 0):
        return "Even"
    else:
        return "Odd"
    
print("8 is", findOddEven(number), "number.")