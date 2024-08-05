"""
Aim: Convert celsius to Fahrenheit from a dictionary and store a result in a new dictionary
Author: Mehdiali
Date: 29 / June / 2024 - 10:26 PM
"""

dic = {
    "Monday": 36,
    "Tuesday": 38,
    "Wednesday": 41,
    "Thursday": 35,
    "Friday": 36,
    "Saturday": 37,
    "Sunday": 39
}

newDic = {day:((celsius * 9 / 5) + 32) for (day, celsius) in dic.items()}

print(newDic)