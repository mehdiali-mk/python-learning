"""
AIM: Find Even Number Seperated From File
Author: Mehdiali
Date: 02 / June / 2024 - 05:41 PM
"""

with open("Programs/numbers.txt", "r") as file:
    
    data = file.read()
    data = data.replace(",", "\n")
    print(data)

    number = ""
    count = 0
    for i in range(len(data)):
        if (data[i] == "\n"):
            if (int(number) % 2 == 0):
                count += 1
            number = ""
        else:
            number += data[i]

    print("There are", count, "even numbers.")
            

    
# print("Even numbers =", count)


