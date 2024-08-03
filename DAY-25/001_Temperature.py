"""
Aim: Read the CSV file of temperatureData
Author: Mehdiali
Date: 28 / June / 2024 - 06:16 PM
"""

# temperatureDetails = []

# with open("DAY-25/temperatureData.csv", "r") as file:
#     lines = file.readlines()

#     for line in lines:
#         line = line.replace("\n", "")
#         temperatureDetails.append(line)

# print(temperatureDetails)

# import csv

# temperatures = []
# with open("DAY-25/temperatureData.csv", "r") as file:
#     data = csv.reader(file)

#     for row in data:
#         if (row[1] != "Temperature"):
#             temperatures.append(row[1])

# print(temperatures)

import os
import pandas
os.system("cls")

data = pandas.read_csv("DAY-25/temperatureData.csv")


mondayData = data[data["DAY"] == "Monday"]
temperature = int(mondayData["Temperature"].to_list()[0])


temperatureInF = (9 / 5) * temperature + 32
print(f"\n\n\nTemperature in Fahrenheit = {temperatureInF}\n\n\n")