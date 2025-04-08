from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

while machine_on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            print("Sorry, that drink is not available.")
        else: 
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                coffee_maker.report()
                money_machine.report()