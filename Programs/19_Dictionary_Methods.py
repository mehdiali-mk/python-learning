"""
Aim: Dictionary Methods
Author: Mehdiali
Date: 30 / May / 2024 - 08:59 PM
"""

student = {
    "name": "Mehdiali",
    "subjects": {
        "maths": 99,
        "APC": 98,
        "WDT": 95,
        "DE": 96,
        "ES": 97,
        
    }
}

print(student)

print(list(student.keys()))
print(list(student.values()))
print(list(student.items())[0])
print(student.get("subjects"))


student.update({"age": 17, "city": "Ahmedabad"})
print(student)