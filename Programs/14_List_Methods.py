"""
Aim: List Methods
Author: Mehdiali
Date: 30 / May / 2024 - 12:46 PM
"""

myList = [5, 3, 6, 8, 2]

myList.reverse()
print(myList)

myList.append(4)

print(myList)


myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)

myList.insert(1,3)
print(myList)

myList.remove(3) # Delete the first occurrence of list.
print(myList)

myList.pop(1) # Removes by index
print(myList)

yourList = ["Ahesan", "Mohsin", "Najar", "Mehdi", "Husena", "Sugra", "Sabera"]

yourList.sort()
print(yourList)