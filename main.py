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



# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

def ask_user(ask):
    if ask != "off":
        # TODO: Turn off the Coffee Machine by entering “off” to the prompt
        if ask == "espresso":
            resources["water"] - MENU["espresso"] ["water"]
            resources["coffee"] - MENU ["espresso"] ["coffee"]
            return resources
            print(input("inset coins"))
        elif ask == "latte":
            print(input("insert coins"))
        elif ask == "cappuccino":
            print(input("insert coins"))
        elif ask == "report":
            print(resources)
        # TODO: Print report.

        else:
            print("wrong")



prompt = ask_user(input("which one do you want? (espresso/latte/cappuccino").lower())
print(prompt)

















# TODO: Check resources sufficient?
# TODO: Process coins.
# TODO:  Check transaction successful?
# TODO: Make Coffee.
