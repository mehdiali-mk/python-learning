"""
Aim: Nato Project Game. (Try Except)
Author: Mehdiali
Date: 07 / July / 2024 - 05:10 PM
"""

import pandas

data = pandas.read_csv(f"DAY-30/Nato Project/nato_phonetic_alphabet.csv")

lettersList = data.letter.tolist()
wordsList = data.code.tolist()

wordsLetterDict = {lettersList[count]:wordsList[count] for count in range(0, len(lettersList))}

def takeUserChoice():
    userInput = input("\nEnter your name = ").upper()
    try: 
        outputList = {letter:wordsLetterDict[letter] for letter in userInput}
    except KeyError:
        print("Please enter the letters of alphabet only.")
        takeUserChoice()
    else:
        print(outputList)

takeUserChoice()