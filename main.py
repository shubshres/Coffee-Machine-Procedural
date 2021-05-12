# dictionary that contains three entries
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

# resources dictionary 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# function that checks if there are enough resources
def is_resource_sufficient(order_ingredients):
    """Returns true when the order can be made, and false when the order is insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough
        

# function that processes the money
def process_coins():
    """Returns the total calculated form the coins inserted."""
    print("Please insert coins...")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# function that checks if the transaction was successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is sufficient, and false if not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in money")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]  
    print(f"Here is your {drink_name} ☕️")


# money box
profit = 0

# setting the machine boolean status to on – as true
is_on = True

while is_on: 
    # asking user what selection they would like to make 
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    # user turns off machine
    if choice == "off":
        print("Powering off the coffee machine...")
        is_on = False
    elif choice == "report": # user wants to see the status of machine
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    else: # user orders drink
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            # ask user for payment
            payment = process_coins()
            
            # check payment and cost 
            if is_transaction_successful(payment, drink["cost"]):
                # make coffee
                make_coffee(choice, drink["ingredients"])
