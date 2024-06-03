"""
Aim: List Practice Question
Author: Mehdiali
Date: 30 / May / 2024 - 01:01 PM
"""

myList = [2,3,8,4,3,2]

newMyList = myList.copy()
newMyList.reverse()

if (myList == newMyList):
    print("List is palindrome.")
else:
    print("List is not palindrome.")