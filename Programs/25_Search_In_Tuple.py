"""
Aim: Search Element in Tuple.
Author: Mehdiali
Date: 31 / May / 2024 - 04:41 PM
"""

myTuple = (1,4,9,16,25,36,49,64,81,100)


numberToSearch = int(input("Enter the number to search = "))

count = 0
found = False

while (count < 10 and found == False):
    if (numberToSearch == myTuple[count]):
        print("Element found at", count, "index")
        found = True
    count+=1

if (not found):
    print("Element is not found")
