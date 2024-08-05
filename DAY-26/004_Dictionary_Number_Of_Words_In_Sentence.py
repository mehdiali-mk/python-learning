"""
Aim: Find the number of letters of each words in the given sentence.
Author: Mehdiali
Date: 29 / June / 2024 - 10:19 PM
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"


dic = {words:len(words) for words in sentence.split(" ")}

print(dic)