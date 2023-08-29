import coffee_maker
import money_machine
import menu

our_coffee_maker = coffee_maker.CoffeeMaker()
our_money_machine = money_machine.MoneyMachine()
our_menu = menu.Menu()

print("Welcome to the OOP Coffee Machine.")
order = input("What would you like? Type espresso, latte, or cappuccino and press Enter. Type report to get report on "
              "machine resources or quit to end the program. ")

our_coffee_maker.report()
menu_item = our_menu.find_drink(order)
our_coffee_maker.make_coffee(menu_item)
