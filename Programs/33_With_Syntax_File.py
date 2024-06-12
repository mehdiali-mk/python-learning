"""
AIM: With Syntax of FILE
Import OS is a module in PY.
Author: Mehdiali
Date: 02 / June / 2024 - 05:28 PM
"""

import os

# in With syntax we don't have to close the file it will done automatically.
data = "Hello\n"
with open("Programs/demo1.txt", "a") as file:
    file.write(data)

with open("Programs/demo1.txt", "r") as file:
    data = file.read()

print(data)


deleteOrNot = int(input("Enter '1' to delete the file = "))

if (deleteOrNot):
    os.remove("Programs/demo1.txt")
