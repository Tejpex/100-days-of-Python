MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def give_report():
    print(f'''
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${money}
    ''')


def check_resources(choice):
    needs = MENU[choice]["ingredients"]
    for ingredient in needs:
        if needs[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    else:
        return True


def make_coffee(choice):
    needs = MENU[choice]["ingredients"]
    for ingredient in needs:
        resources[ingredient] -= needs[ingredient]
    print(f"Here is your {choice}☕. Enjoy!”.")


def refill(choice):
    if choice == "water":
        resources["water"] = 800
    elif choice == "milk":
        resources["milk"] = 500
    elif choice == "coffee":
        resources["coffee"] = 100
    else:
        print("Sorry, not a valid command.")


def receive_payment(choice):
    price = MENU[choice]["cost"]
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    received = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    if received < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global money
        money += price
        money_back = round(received - price, 2)
        if money_back > 0:
            print(f"Here is ${money_back} in change.")
        return True


def handle_order(command):
    if command == "report":
        give_report()
    elif command == "espresso" or command == "latte" or command == "cappuccino":
        if check_resources(command):
            if receive_payment(command):
                make_coffee(command)
    elif command == "fill":
        ingredient = input("What would you like to refill? ")
        refill(ingredient)
    elif command == "off":
        print("Turning off...")
        global on
        on = False
    else:
        print("Not a valid command. Try again.")


on = True
while on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    handle_order(order)


