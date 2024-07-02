"""
Aim: Students Grade Generator.
Author: Mehdiali
Date: 13 / June / 2024 - 12:36 PM
"""

from os import system
system("cls")

print("\nWelcome to the students grade generator.\n")

studetnsMarks = {
    "Mehdiali": 99,
    "Aayan": 78,
    "Man": 76,
    "Aman": 55,
    "Anvar": 82,
    "Jabir": 63,
    "Abbas": 45
}

studetnsGrade = {}
for key in studetnsMarks:
    marks = studetnsMarks[key]
    if (marks >= 91 and marks <= 100):
        studetnsGrade[key] = "Outstanding"
    elif (marks >= 81 and marks <= 90):
        studetnsGrade[key] = "Exceeds Expectations"
    elif (marks >= 71 and marks <= 80):
        studetnsGrade[key] = "Acceptable"
    elif (marks >= 0 and marks <= 70):
        studetnsGrade[key] = "Fail"
    else:
        studetnsGrade["Error"] = "Wrong marks"

print("Marks of students:")
for key in studetnsMarks:
    print(f"{key} = {studetnsMarks[key]}")

print("\nGrade as per marks:")
for key in studetnsGrade:
    print(f"{key} = {studetnsGrade[key]}")



