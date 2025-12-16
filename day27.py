MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

class CoffeeMachine:
    INITIAL_RESOURCES = {
    "water": 1000,  # ml
    "milk": 500,   # ml
    "coffee": 150, # g
}
    def __init__(self, drink_name, money):
        self.drink_name = drink_name
        self.money = money

    def check_resources(self):
        for ingredient in MENU[self.drink_name]["ingredients"]:
            required = MENU[self.drink_name]["ingredients"][ingredient]
            available = CoffeeMachine.INITIAL_RESOURCES[ingredient]
            if required <= available:
                pass
                
            else:
                print("insufficient resources. add stock")

    def handle_payment(self):
            cost = MENU[self.drink_name]["cost"]
            change = round((self.money - cost), 2)   
            if change >= 0:    
                print(f"here is your change = {change}")
            else:
                print("Insufficient money. the coffee costs more than you paid") 
                
            



    def make_coffee(self):
        for ingredient in MENU[self.drink_name]["ingredients"]:
            required = MENU[self.drink_name]["ingredients"][ingredient]
            available = CoffeeMachine.INITIAL_RESOURCES[ingredient]
            new_quantity = available - required
            if new_quantity >= 0:
                CoffeeMachine.INITIAL_RESOURCES[ingredient] = new_quantity
                
                
            else:
                print("not enough resources. requirement exceeds resources")
                break

    def process(self):
        print("Hi. How may I help you!")
        self.check_resources()
        self.handle_payment()
        self.make_coffee()
        print("making your coffee with love")
        print(f"here's your {self.drink_name}")
        print("Have a good day, Thank you and visit again")



order1 = CoffeeMachine("cappuccino", 2.57)
order1.process()          



