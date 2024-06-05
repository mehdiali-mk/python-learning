"""
Aim: Sets Methods.
Author: Mehdiali
Date: 30 / May / 2024 - 10:37 PM
"""

mySet = {1,2,3,2,3,"Python", "Python", "Mehdiali"}

print(mySet)

mySet.add("Mehdiali")
mySet.add("Kadiwala")

print(mySet)

mySet.remove(1)
mySet.remove(2)

print(mySet)

print(mySet.pop())
print(mySet.pop())


myNewSet = {440, 429}
combinedSet = mySet.union(myNewSet)

print(combinedSet)

intersectionSet = combinedSet.intersection(mySet)

print(intersectionSet)

mySet.clear()

print(mySet)
