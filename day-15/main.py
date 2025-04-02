import data

user_input = ""
PENNIES = 0.01
NICKLES = 0.05
DIMES = 0.10
QUARTERS = 0.25
machine_on = True

def report(data_source):
    """Prints a report of current coffee machine resources"""
    print(f"Water: {data_source['water']}ml")
    print(f"Milk: {data_source['milk']}ml")
    print(f"Coffee: {data_source['coffee']}g")

def machine_input(u_input):
    """Passes in user input and calls the relevant function based on input, also used to break the while loop for the coffee machine
    :param u_input:> passes in user_input variable to determine action
    :return :> calls appropriate function based on input or exits the while loop
    """
    global machine_on
    if u_input == "report":
        return report(data.resources)
    elif u_input == "latte":
        return check_resources(data.MENU["latte"]["ingredients"], data.resources)
    elif u_input == "cappuccino":
        return check_resources(data.MENU["cappuccino"]["ingredients"], data.resources)
    elif u_input == "espresso":
        return check_resources(data.MENU["espresso"]["ingredients"], data.resources)
    elif u_input == "off":
        machine_on = False
        return machine_on
    else:
        print("Invalid input")
        return False

def check_resources(choice, resources):
    """Checks if there are enough resources to make the selected choice
    :param choice:> passes in dictionary of users choice so that it can be checked against resources 
    :param resources:> 
    """
    for ingredient in choice:
        if choice[ingredient] > resources[ingredient]:
            print(f"not enough {ingredient}")
            return False
    return True

def process_coins(choice):
    """ function that prompts the user to input currency, this is totalled and checked against the price of the beverage
    :param choice:> passes in dictionary of users choice so that cost can be pulled
    :return :> returns True if sufficient funds or false if insufficient 
    """
    total = 0
    print(f"The cost of your beverage is: {choice['cost']}")
    pennies_input = int(input("How many pennies?: "))
    nickles_input = int(input("How many nickles?: "))
    dimes_input = int(input("How many dimes?: "))
    quarters_input = int(input("How many quarters?: "))
    total += pennies_input * PENNIES
    total += nickles_input * NICKLES
    total += dimes_input * DIMES
    total += quarters_input * QUARTERS
    if total >= choice['cost']:
        change = total - choice['cost']
        print(f"Your change is: ${round(change, 2)}")
        return True
    else:
        print("Insufficient funds")
        return False

def deduct_resources(funds, choice, resources, drink_name):
    """function to deduct beverage choice from machine resources
    :param funds:> passes in the funds_sufficient which calls the process coins function
    :param choice:> passes in dictionary to access ingredients key
    :param resources:> passing in resources dictionary to access resources
    :param drink_name:> passes in the name of the beverage so it can be returned in a thank you message
    """

    if funds:
        for ingredient in choice["ingredients"]:
            resources[ingredient] -= choice["ingredients"][ingredient]
        print("Resources have been deducted")
        report(data.resources)
        print(f"Here is your {drink_name}. Enjoy!")
    else:
        print("No resources deducted due to insufficient funds.")



while machine_on:
    user_input = input("what would they like to drink? (espresso/latte/cappuccino): ").lower()

    if machine_input(user_input):
        if user_input == "latte":
            funds_sufficient = process_coins(data.MENU["latte"])
            deduct_resources(funds_sufficient, data.MENU["latte"], data.resources, "latte")
        elif user_input == "cappuccino":
            funds_sufficient = process_coins(data.MENU["cappuccino"])
            deduct_resources(funds_sufficient, data.MENU["cappuccino"], data.resources, "cappuccino")
        elif user_input == "espresso":
            funds_sufficient = process_coins(data.MENU["espresso"])
            deduct_resources(funds_sufficient, data.MENU["espresso"], data.resources, "espresso")

