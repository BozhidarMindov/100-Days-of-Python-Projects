from menu import resources, MENU

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

money = 0
to_continue = True

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def resources_sufficient(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Insert coins. ")
    result = 0
    result += int(input("How many quarters?: ")) * quarter
    result += int(input("How many dimes?: ")) * dime
    result += int(input("How many nickels?: ")) * nickel
    result += int(input("How many pennies?: ")) * penny
    return result


def check_transaction_successful(total, drink_cost):
    if total >= drink_cost:
        change = round(total - drink_cost, 2)
        print(f"Here is your {change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry, there is not enough money. Money refunded")
        return False


def make_coffee(name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {name}. Enjoy!")



while to_continue:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        to_continue = False
    elif order == "report":
        print_report()
    else:
        drink = MENU[order]
        if resources_sufficient(drink["ingredients"]):
            total = process_coins()
            if check_transaction_successful(total, drink["cost"]):
                make_coffee(order, drink["ingredients"])
        