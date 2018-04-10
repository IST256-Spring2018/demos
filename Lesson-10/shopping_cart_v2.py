"""
Shopping Cart V2 - With Classes!
"""

class CartItem():
    price = 0
    qty = 0

    def __init__(self, name, price, qty):
        self.name = name
        try:
            self.price = float(price)
        except:
            self.price = 0
        self.qty = int(qty)
        

    def __str__(self):
        return self.name

    def sub_total(self):
        return self.price * self.qty
    

shopping_cart = []

def add_item(person):
    shopping_cart.append(person)

def remove_item(name):
    index = 0
    for item in shopping_cart:
        if item.name == name:
            shopping_cart.pop(index)
        index += 1


def print_cart():
    print("Your Shopping Cart")
    print("-" * 57)
    fmt_str = "{:30} | {} | {} | {}"   
    print(fmt_str.format("Name", "Price", "Qty", "Sub-Total"))
    print("-" * 57)
    total = 0
    for item in shopping_cart:
        print("{:30} | ${:.2f} | {} | ${:.2f}".format(item.name, item.price, item.qty, item.sub_total()))
        total = total + item.sub_total()
    print("-" * 57)
    print("{:>30} | ${:.2f}".format("Sub Total", total))

def print_menu_get_choice():
    print("Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Print Shopping Cart")
    print("4. Quit")
    while True:
        choice = input("Please enter an option: ")
        try:
            if int(choice) in [1, 2, 3, 4]:
                return choice
        except:
            pass
        print("Please enter a valid option.")


item = CartItem("apples", "gjgk", "gjhgk")


# while True:
#     choice = print_menu_get_choice()
#     if choice == 1:
#         try:
#             name = input("Please enter a name ")
#             price = input("Please enter a price ")
#             qty = input("Please enter a qty")
#         except Exception as e:
#             print("invalid values")
#     if choice == 2:
#         in

