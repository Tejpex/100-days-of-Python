from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine = CoffeeMaker()
coin_machine = MoneyMachine()
our_menu = Menu()

on = True
while on:
    order = input(f"What would you like? ({our_menu.get_items()}): ").lower()
    if order == "off":
        on = False
    elif order == "report":
        coffe_machine.report()
        coin_machine.report()
    elif order == "cost":
        choice = input(f"What are you interested in? ({our_menu.get_items()}): ")
        print(our_menu.find_drink(choice).cost)
    else:
        drink = our_menu.find_drink(order)
        if drink:
            if coffe_machine.is_resource_sufficient(drink):
                if coin_machine.make_payment(drink.cost):
                    coffe_machine.make_coffee(drink)
