class CoffeeMaker:
    """This class models a machine that makes coffee."""

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints the machine's available resources."""
        print(f"Remaining water: {self.resources['water']}ml")
        print(f"Remaining milk: {self.resources['milk']}ml")
        print(f"Remaining coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when a drink can be made, False otherwise"""
        can_make_drink = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, issuficient {item} to make your coffee.")
                can_make_drink = False

        return can_make_drink