"""
Aim: Read and find the number of different fur colors of squirrel and make a new csv.
Author: Mehdiali
Date: 29 / June / 2024 - 11:10 AM
"""

import pandas
import math

data = pandas.read_csv("DAY-25/squirrel/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

primaryFurColorList = data["Primary Fur Color"].unique().tolist()
primaryFurList = data["Primary Fur Color"].tolist()


numberOfSquirrel = []
for color in primaryFurColorList:
    numberOfSquirrel.append(primaryFurList.count(color))


for count in range(0, len(primaryFurColorList)):
    if (type(primaryFurColorList[count]) == float):
        if (math.isnan(primaryFurColorList[count])):
            primaryFurColorList[count] = "unrecognized"

print(f"\n\n{primaryFurColorList}")

print(numberOfSquirrel, "\n\n\n")
dictionaryOfSquirrel = {
    "Fur Color": primaryFurColorList,
    "Count": numberOfSquirrel
}



squirrelData = pandas.DataFrame(dictionaryOfSquirrel)
squirrelData.to_csv("DAY-25/squirrel/colorData.csv", index=False)