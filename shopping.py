class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, quantity):
        item = (item_name, quantity)
        self.items.append(item)

    def remove_item(self, item_name, quantity):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)  # Use () not []
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

cart = ShoppingCart()

# Add items to the cart
cart.add_item(item_name="kiwi", quantity=20)
cart.add_item(item_name="eggs", quantity=12)
cart.add_item(item_name="apple", quantity=40)

print("Current items in our cart:")

# Loop through the list directly (it's a list, not a function)
for item in cart.items:
    print(item[0], "-", item[1])


total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)

