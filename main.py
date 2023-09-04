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
    "money": 0,  # Initialize money to 0
}


# Function to calculate total coins inserted and return it
def coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    quarters_value = quarters * 0.25
    dimes_value = dimes * 0.1
    nickels_value = nickels * 0.05
    pennies_value = pennies * 0.01
    total = quarters_value + dimes_value + nickels_value + pennies_value
    return total


# Function to check if there are enough resources to make a coffee
def check_resources(coffee_choice):
    ingredients_needed = MENU[coffee_choice]["ingredients"]
    for ingredient, quantity in ingredients_needed.items():
        if resources[ingredient] < quantity:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True


# Function to serve coffee
def serve_coffee(coffee_choice):
    cost = MENU[coffee_choice]["cost"]
    total_inserted = coins()

    if total_inserted < cost:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        resources["money"] += cost  # Add the cost to the machine's money
        change = total_inserted - cost
        print(f"Here is ${change:.2f} in change.")
        # Deduct the used resources
        for ingredient, quantity in MENU[coffee_choice]["ingredients"].items():
            resources[ingredient] -= quantity
        print(f"Here is your {coffee_choice} ☕. Enjoy!")


# Main function
def user_choice():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']:.2f}")
        elif choice == "off":
            return
        elif choice in MENU:
            if check_resources(choice):
                serve_coffee(choice)
        else:
            print("Invalid choice. Please select from the menu.")


user_choice()
