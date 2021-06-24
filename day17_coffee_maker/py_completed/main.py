from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
myMenu = Menu()

while True:
    drinkChoice = input(f"What would you like? {myMenu.get_items()}: ")
    if drinkChoice == "off":
        print("Goodbye")
        break
    elif drinkChoice == "report":
        coffeeMachine.report()
        moneyMachine.report()
    else:
        item = myMenu.find_drink(drinkChoice)
        if item != None:
            if not coffeeMachine.is_resource_sufficient(item):
                pass
            else:
                if moneyMachine.make_payment(item.cost):
                    coffeeMachine.make_coffee(item)
    print()
            