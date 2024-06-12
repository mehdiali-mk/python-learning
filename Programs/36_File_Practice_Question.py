"""
AIM: Find the word in file
Author: Mehdiali
Date: 02 / June / 2024 - 05:41 PM
"""

def findWord(string, wordToFind):
    foundOrNot = string.find(wordToFind)
    return foundOrNot




file = open("Programs/practice.txt", "r")

data = file.read()
found = findWord(data, "learning")

if (found != -1):
    print("Word 'learning' is found in file.")
else:
    print("Word 'learning' is not found in file.")

file.close()