from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()

isOn = True


options = menu.get_items()


while isOn:
    userChoice = input(f"What would you like? ({options}): ").lower()

    if (userChoice == "off"):
        isOn = False
    elif (userChoice == "report"):
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(userChoice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
