"""
Aim: Find the sum of even number between 1 to 100.
Author: Mehdiali
Date: 10 / June / 2024 - 06:53 PM
"""

totalOfEvenNumber = 0
for evenNumber in range(2, 101, 2):
    totalOfEvenNumber += evenNumber

print(f"The sum of even number between 1 to 100 = {totalOfEvenNumber}")