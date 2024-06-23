"""
Aim: Myown Pizza Ordering System.

Small Pizza: 15
Medium Pizza: 20
Large Pizza: 25

Pepperoni for Small Pizza: 2
Pepperoni for Medium or Large Pizza: 3

Extra Cheese for any size pizza: 1

Author: Mehdiali
Date: 08 / June / 2024 - 12:28 PM
"""

print("\nWelcome to the Myown Pizza app.")
print("*******************************")
print("             Menu              ")
print("*******************************")
print("Small Pizza (S): 150\nMedium Pizza (M): 200\nLarge Pizza (L): 250\n\nPepperoni for Small Pizza: 20\nPepperoni for Medium or Large Pizza: 30\n\nExtra Cheese for any size pizza: 10")
print("*******************************\n")

smallSizePizza = 150
mediumSizePizza = 200
largeSizePizza = 250

pepperoniForS = 20
pepperoniForMorL = 30

extraCheese = 10


while True:
    sizeOfPizza = input("Enter the size of Pizza as (S/M/L) = ")

    if (sizeOfPizza == "s" or sizeOfPizza == "S" or sizeOfPizza == "m" or sizeOfPizza == "M" or sizeOfPizza == "l" or sizeOfPizza == "L"):
        break
    else:
        print("\nPlease enter the correct choice as (S / M / L).")

while True:
    isPepperoni = input("Do you want to add Pepperoni? (Y/N) = ")

    if (isPepperoni == "y" or isPepperoni == "Y" or isPepperoni == "n" or isPepperoni == "N"):
        break
    else:
        print("\nPlease enter the correct choice as (Y / N).")

while True:
    isExtraCheese = input("Do you want to add Extra Cheese? (Y/N) = ")

    if (isExtraCheese == "y" or isExtraCheese == "Y" or isExtraCheese == "n" or isExtraCheese == "N"):
        break
    else:
        print("\nPlease enter the correct choice as (Y / N).")
     

yourOrder = []

if (sizeOfPizza == "s" or sizeOfPizza == "S"):
    totalBill = smallSizePizza
    yourOrder.append("Small Pizza")
    if (isPepperoni == "y" or isPepperoni == "Y"):
        totalBill += pepperoniForS
        yourOrder.append("with Pepperoni")
    else:
        yourOrder.append("without Pepperoni")

else:
    if (sizeOfPizza == "m" or sizeOfPizza == "M"):
        totalBill = mediumSizePizza
        yourOrder.append("Medium Pizza")
    else:
        totalBill = largeSizePizza
        yourOrder.append("Large Pizza")
    
    if (isPepperoni == "y" or isPepperoni == "Y"):
        totalBill += pepperoniForMorL
        yourOrder.append("with Pepperoni")
    else:
        yourOrder.append("without Pepperoni")


if (isExtraCheese == "y" or isExtraCheese == "Y"):
    totalBill += extraCheese
    yourOrder.append("with Extra Cheese")
else:
    yourOrder.append("without Extra Cheese")

print(f"\nYour final order is:\n{yourOrder[0]} {yourOrder[1]} {yourOrder[2]}.")
print(f"\nYour Total bill = {totalBill}\n")
