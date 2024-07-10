"""
Aim: Coffee Machine.
Author: Mehdiali
Date: 19 / June / 2024 - 05:04 PM
"""

import os
from menu import MENU
from menu import resources

moneyColleted = 0


# This function is used to display the current report of the machine.
def displayReport():
    print("\nReport:")
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ₹{moneyColleted}")

# This function is used to return the availability of drink.
def isAvailable(required, current):
    if (required[0] > current[0]):
        print("Sorry there is not enough water.")
        return 0
    elif (required[1] > current[1]):
        print("Sorry there is not enough milk.")
        return 0
    elif (required[2] > current[2]):
        print("Sorry there is not enough coffee.")
        return 0
    else:
        return 1

def getIngredient(ingredientName, userChoice):
    return MENU[userChoice]["ingredients"][ingredientName]

# This function is used to check the availability of this drink.
def checkAvailable(userChoice):
    requiredWater = getIngredient("water", userChoice)
    if (userChoice == "espresso"):
        requiredMilk = 0
    else:
        requiredMilk = getIngredient("milk", userChoice)
    requiredCoffee = getIngredient("coffee", userChoice)

    requiredStock = []
    requiredStock.append(requiredWater)
    requiredStock.append(requiredMilk)
    requiredStock.append(requiredCoffee)

    currentWater = resources["water"]
    currentMilk = resources["milk"]
    currentCoffee = resources["coffee"]

    currentStock = []
    currentStock.append(currentWater)
    currentStock.append(currentMilk)
    currentStock.append(currentCoffee)

    return isAvailable(requiredStock, currentStock)


# This function is used to calculate money.
"""
def calculateMoney(money):
    totalMoney = 0
    totalMoney = totalMoney + (money[0] * 0.25)
    totalMoney = totalMoney + (money[1] * 0.10)
    totalMoney = totalMoney + (money[2] * 0.05)
    totalMoney = totalMoney + (money[3] * 0.01)

    return totalMoney
"""

# This function is used to insert coins from the user.
def insertCoins(userChoice):
    while True:
        print("\nPlease insert the coins:")
        numberOfQuarters = abs(int(input("How many Quarters? = "))) * 0.25
        numberOfDimes = abs(int(input("How many Dimes? = "))) * 0.10
        numberOfNickels = abs(int(input("How many Nickels? = "))) * 0.05
        numberOfPennies = abs(int(input("How many Pennies? = "))) * 0.01

        # money = [numberOfQuarters, numberOfDimes, numberOfNickels, numberOfPennies]

        totalMoney = numberOfQuarters + numberOfDimes + numberOfNickels + numberOfPennies
        requiredMoney = MENU[userChoice]["cost"]
        if (totalMoney < requiredMoney):
            print("\nSorry that's not enough money. Money refunded.")
        else:
            break
    
    global moneyColleted
    moneyColleted = round(moneyColleted + requiredMoney, 2)
    change = round(totalMoney - requiredMoney, 2)
    
    if change > 0:
        print(f"Here is ₹{change} in change.")


# This function is used to deduct the resource used by as per the order.
def deductResources(userChoice):
    resources["water"] = resources["water"] - getIngredient("water", userChoice)
    if (userChoice != "espresso"):
        resources["milk"] = resources["milk"] - getIngredient("milk", userChoice)
    resources["coffee"] = resources["coffee"] - getIngredient("coffee", userChoice)

while True:
    while True:
        userChoice = input("\n--> Espresso\n--> Latte\n--> Cappuccino\n--> Report\n\nWhat would you like? = ").lower()

        if (userChoice == "espresso" or userChoice == "latte" or userChoice == "cappuccino" or userChoice == "report" or userChoice == "off"):
            break
        else:
            print("\nPlease, enter the correct choice.")

    if (userChoice == "off"):
        break
    elif (userChoice == "report"):
        displayReport()
    elif (userChoice == "espresso"):
        available = checkAvailable(userChoice)

        if (available == 1):
            insertCoins(userChoice)
            print("\nHere is your Espresso ☕ Enjoy!!")
            deductResources(userChoice)
    elif (userChoice == "latte"):
        available = checkAvailable(userChoice)

        if (available == 1):
            insertCoins(userChoice)
            print("\nHere is your Latte ☕ Enjoy!!")
            deductResources(userChoice)
    elif (userChoice == "cappuccino"):
        available = checkAvailable(userChoice)

        if (available == 1):
            insertCoins(userChoice)
            print("\nHere is your Cappuccino ☕ Enjoy!!")
            deductResources(userChoice)
    else:
        print("\n~~!There is error in the machine.")
        break     