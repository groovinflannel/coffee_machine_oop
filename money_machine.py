class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dims": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints profit"""
        print(f"Money available: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns total calculated from inserted coins"""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Return True when the payment is successful, False if not"""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, not enough money inserted. Issuing refund.")
            self.money_received = 0
            return False