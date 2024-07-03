"""
Aim: Travel Log using nested list and dictionaries.
Author: Mehdiali
Date: 13 / June / 2024 - 12:36 PM
"""

key1 = "country"
key2 = "cities"
key3 = "noOfVisit"

travelLog = [
    {
        key1: "India",
        key2: ["Mumbai", "Ahmedabad", "Pune", "Rajkot"],
        key3: 4
    },
    {
        key1: "France",
        key2: ["Paris", "Lille", "Dijon"],
        key3: 2
    },
]

def addNewCountry(countryName, numberOfVisits, listOfCities):
    travelLog.append({
        key1: countryName,
        key2: listOfCities,
        key3: numberOfVisits
    })

addNewCountry("America", 8, ["New York", "Los Angels"])
# print(travelLog)

for element in travelLog:
    for key in element:
        print(f"{key}: {element[key]}")
    print("\n", end="")