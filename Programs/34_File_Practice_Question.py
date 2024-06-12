"""
AIM: Create the file and write the data
Author: Mehdiali
Date: 02 / June / 2024 - 05:41 PM
"""

file = open("Programs/practice.txt", "w")

dataToInsert = "Hi everyone\nWe are learning File I/O\nusing Java.\nI like programming in Java."

file.write(dataToInsert)

file.close()