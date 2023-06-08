class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.list = []

    def add(self, item: Item):  # adds in the max 10 items to the cart
        if len(self.list) >= 10:
            print("Shopping Cart full")
        else:
            self.list.append(item)

    def items_names(self) -> []:  # returns the items names
        return [item.name for item in self.list]

    def total(self) -> int:  # returns the items prices
        return sum(item.price for item in self.list)


car = Item("car", 25000)
cell = Item("cell", 1200)
bed = Item("bed", 2000)

cart = ShoppingCart()
cart.add(car)
cart.add(cell)
cart.add(bed)

print(f"total price of the items: {cart.total()}")
print(f"items names: {cart.items_names()}")
