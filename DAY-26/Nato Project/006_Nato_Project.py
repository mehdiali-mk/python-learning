"""
Aim: Nato Project Game.
Author: Mehdiali
Date: 30 / June / 2024 - 07:11 PM
"""

import pandas

data = pandas.read_csv(f"DAY-26/Nato Project/nato_phonetic_alphabet.csv")

lettersList = data.letter.tolist()
wordsList = data.code.tolist()

wordsLetterDict = {lettersList[count]:wordsList[count] for count in range(0, len(lettersList))}

userInput = input("\nEnter your name = ").upper()

outputList = {letter:wordsLetterDict[letter] for letter in userInput}

print(outputList)