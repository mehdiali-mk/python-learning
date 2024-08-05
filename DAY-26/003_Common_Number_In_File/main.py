"""
Aim: Find all the common numbers from two different files.
Author: Mehdiali
Date: 29 / June / 2024 - 09:58 PM
"""

with open("DAY-26/003_Common_Number_In_File/file1.txt") as file1:
    file1Data = file1.readlines()

with open("DAY-26/003_Common_Number_In_File/file2.txt") as file2:
    file2Data = file2.readlines()

commonNumbersList = [int(num) for num in file1Data if num in file2Data]

print(commonNumbersList)