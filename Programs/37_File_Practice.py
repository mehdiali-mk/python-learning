"""
AIM: Find Word in File and print its line number.
Author: Mehdiali
Date: 02 / June / 2024 - 05:41 PM
"""

def findWord(string, wordToFind):
    foundOrNot = string.find(wordToFind)
    return foundOrNot


file = open("Programs/practice.txt", "r")
data = True
line = 1

while data:
    data = file.readline()
    found = findWord(data, "learning")

    if (found != -1):
        print("Word 'learning' is found in", line, "line.")
        break
    
    line += 1

if (found == -1):
    print("Word 'learning' is not found in file.")
    
file.close()