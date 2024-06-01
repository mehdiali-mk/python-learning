"""
Slicing
Author: Mehdiali
Date: 29 / May / 2024 - 10:14 PM
"""

string = "Mehdiali Kadiwala"
slicedStr = string[5:8]
print(slicedStr)

slicedStr = string[9:] # [5 : len(str)]
print(slicedStr)

slicedStr = string[:8] # [0 : 8]
print(slicedStr)

slicedStr = string[-8:]
print(slicedStr)