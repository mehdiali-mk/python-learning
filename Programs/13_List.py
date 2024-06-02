"""
Aim: List Operations
Author: Mehdiali
Date: 30 / May / 2024 - 11:56 AM
"""

myList = [95, 98.5, 96.8, 45.6, 56.8] # Normal List.

print(len(myList))

myList[1] = "Mehdiali" # Different datatypes are allowed.

print(myList)

print(myList[1:4]) # ["Mehdiali", 96.8, 45.6]

print(myList[-3:-2]) # [96.8]