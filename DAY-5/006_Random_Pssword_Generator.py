"""
Aim: Random Password Generator.
Author: Mehdiali
Date: 10 / June / 2024 - 06:53 PM
"""

import string
import random
import os
os.system("cls")

alphabetsList = []
digitsList = []
symbolsList = []

for letter in string.ascii_uppercase + string.ascii_lowercase:
    alphabetsList.append(letter)

for digit in string.digits:
    digitsList.append(digit)

for symbol in string.punctuation:
    symbolsList.append(symbol)

print("\nWelcome to the Myown Password Generator.\n")

numberOfLetters = int(input("Enter the number of letters you want = "))
numberOfDigits = int(input("Enter the number of digits you want = "))
numberOfSymbols = int(input("Enter the number of symbols you want = "))

newPassword = []



for count in range(0, numberOfLetters):
    randomNumber = random.randint(0, len(alphabetsList) - 1)
    newPassword.append(alphabetsList[randomNumber])

for count in range(0, numberOfDigits):
    randomNumber = random.randint(0, len(digitsList) - 1)
    newPassword.append(digitsList[randomNumber])

for count in range(0, numberOfSymbols):
    randomNumber = random.randint(0, len(symbolsList) - 1)
    newPassword.append(symbolsList[randomNumber])



random.shuffle(newPassword)

newPasswordInString = ""
for letter in newPassword:
    newPasswordInString += letter

print(f"\n\nYour new generated strong password = {newPasswordInString}\n\n")