"""
AIM: Replace the word Java with Python in file
Author: Mehdiali
Date: 02 / June / 2024 - 05:41 PM
"""

def replaceWord(string, oldWord, newWord):
    string = string.replace(oldWord, newWord)
    return string




file = open("Programs/practice.txt", "r")

data = file.read()
newString = replaceWord(data, "Java", "Python")

file.close()

file = open("Programs/practice.txt", "w")

file.write(newString)

file.close()