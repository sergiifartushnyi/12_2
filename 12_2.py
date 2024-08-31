class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        items_str = "\n".join ( [f"{item.name}: {count} pcs." for item , count in self.products.items ()] )
        return f"User: {self.user}\nItems:\n{items_str}"

    def get_total(self):
        return sum(item.price * count for item, count in self.products.items())


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)
print(apple)
buyer = User("Ivan", "Ivanov", "0506546789")
print(buyer)
print("*****")
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print("*****")

print(isinstance(cart.user, User))
print(cart.get_total())
print(cart.get_total())
print("*****")

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 10)
print(cart)
print("*****")

print(cart.get_total())
