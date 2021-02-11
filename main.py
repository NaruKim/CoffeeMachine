MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}

def reporting():
    print(f"water: {resources['water']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${resources['money']}")
    print(f"milk: {resources['milk']}ml")

def coin():
    penny=float(input("How many pennies do you insert?: "))
    nickel=float(input("How many nickels do you insert?: "))
    dime=float(input("How many dimes do you insert?: "))
    quarter=float(input("How mayn quarters do you insert?: "))
    return 0.01*penny+0.05+nickel+0.1*dime+0.25*quarter

def coffeemachine():
    while True:
        want=input("What would you like? (Espresso/ Latte/ Cappuccino): ").lower()

        if want=='off':
            print("Machine is off")
            return
        elif want=='report':
            reporting()
        else:
            order = MENU[want]
            print(f"Your order: {want}")

            if resources['water']<order['ingredients']['water']:
                print("Sorry there is not enough water")
            elif resources['milk']<order['ingredients']['milk']:
                print("Sorry there is not enough milk")
            elif resources['coffee']<order['ingredients']['coffee']:
                print("Sorry there is not enough coffee")
            else:
                payment=coin()
                if payment >= order['cost']:

                    resources['water']-order['ingredients']['water']
                    resources['milk']-order['ingredients']['milk']
                    resources['coffee']-order['ingredients']['coffee']
                    resources['money']+=order['cost']
                    print(f"Your {want} is here")

                    overcharge=payment-order['cost']
                    print(f"${overcharge} returned")

                else:
                    print("Sorry the amount of inserted coins is not enough for the order.")

coffeemachine()