"""
Aim:
- Create a class called Order which stores item & its price.
- Under Dunder Function __gt__() to convey that:
    - order1 > order2 if price of order1 > price of order2
Author: Mehdiali
Date: 04 / June / 2024 - 03:15 PM
"""

import os

class Order:

    def __init__(self, orderName, orderPrice):
        self.orderName = orderName
        self.orderPrice = orderPrice
    
    def __gt__(self, orderObj):
        priceOfOrder1 = self.orderPrice
        priceOfOrder2 = orderObj.orderPrice

        if (priceOfOrder1 > priceOfOrder2):
            return 1
        else:
            return 0
        

order1 = Order("Pizza", 120)
order2 = Order("Burger", 240)


os.system("cls")

print("\n\n")
if (order1 > order2):
    print(order1.orderName, "cost more than", order2.orderName)
else:
    print(order2.orderName, "cost more than", order1.orderName)    

print("\n\n")