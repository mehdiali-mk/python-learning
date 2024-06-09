"""
Aim: For Loops Practice Questions
Author: Mehdiali
Date: 31 / May / 2024 - 04:38 PM
"""

myList = [1,4,9,16,25,36,49,64,81,100]

for element in myList:
    print(element)

myTuple = (1,4,9,16,25,36,49,64,81,100)

elementToSearch = 16

for element in myTuple:
    if (elementToSearch == element):
        print("Element found")
        break
else:
    print("Element not found.")