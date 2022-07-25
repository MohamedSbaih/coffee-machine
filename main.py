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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    #? Return True when order can be made, False if ingredients are sufficient 
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True

def process_coins():
    #?  Return the total calculated from coins inserted
    print("Please insert the coins.")
    total = int(input("How many quaters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    
    return total

def is_transaction_successful(money_received , drink_cost):
    #? Return True when payment is accepted, or False if money is insufficient
    global profit
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Her is ${change} in change.")
        
        profit += drink_cost
        return True
    else:
        print("Sorry That's not enough money. Money Refunded.")
        return False    

def make_coffee(drink_name, order_ingredients):
    #? Deduct the required ingredients from the resourses. 
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")
        
