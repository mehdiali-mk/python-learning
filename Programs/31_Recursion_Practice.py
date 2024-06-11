"""
Aim: Recursion Practice Questions.
Author: Mehdiali
Date: 01 / June / 2024 - 11:46 AM
"""

number = 5

def sumToN(number):
    if (number == 1):
        return 1
    return number + sumToN(number - 1)

print("Sum of 5 Natural Number =", sumToN(number))

myList = [3,4,5,1,6,2]
index = 0

def printElements(myList, index):
    if (index == len(myList)):
        return
    print(myList[index], end=" ")
    printElements(myList, index+1)

printElements(myList, index)
