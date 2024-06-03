"""
Aim: Dictionary Demo
Author: Mehdiali
Date: 30 / May / 2024 - 08:32 PM
"""

information = {
    "name": "Mehdi",
    "class": "CE - 2C",
    "subjects": ["Maths", "DE", "APC", "ES", "PP", "WDT"],
    "SPI": 96.4,
    "mobile": 1234567890,
    "isActive": True,
}

print(information)

information["name"] = "Mehdiali"
information["surname"] = "Kadiwala"

print(information["mobile"])
print("My name is", information["name"], information["surname"], ".\nI am a student of Class", information["class"], ".\nI sutdy", information["subjects"], "subjects.\nMy SPI is", information["SPI"], ".\nYou can contact me on", information["mobile"], ".\nMy active status is:", information["isActive"]) 