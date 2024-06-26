"""
Aim: Myown Love Calculator.

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of time the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

Author: Mehdiali
Date: 08 / June / 2024 - 01:05 PM
"""

print("\nWelcome to the Myown Love Calculator.")
print("*************************************")

name1 = input("Enter your name = ")
name2 = input("Enter their name = ")

concateName = name1 + name2
lowercaseName = concateName.lower()

t = lowercaseName.count("t")
r = lowercaseName.count("r")
u = lowercaseName.count("u")
e = lowercaseName.count("e")
true = t + r + u + e

l = lowercaseName.count("l")
o = lowercaseName.count("o")
v = lowercaseName.count("v")
e = lowercaseName.count("e")
love = l + o + v + e
loveScore = int(str(true) + str(love))

if (loveScore < 10 or loveScore > 90):
    print(f"Your Score is {loveScore}%, you go together like coke and mentos.")
elif (loveScore > 40 or loveScore <= 50):
    print(f"Your Score is {loveScore}%, you are alright together.")
else:
    print(f"Your Score is {loveScore}%")