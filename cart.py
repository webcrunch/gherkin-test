# class Cart:
#     def __init__(self):
#         self.items = {}

#     def add_book(self, title, price, quantity=1):
#         if title in self.items:
#             self.items[title]["quantity"] += quantity
#         else:
#             self.items[title] = {"price": price, "quantity": quantity}

#     def remove_book(self, title):
#         if title in self.items:
#             del self.items[title]

#     def clear(self):
#         self.items = {}

#     def total_books(self):
#         return sum(item["quantity"] for item in self.items.values())

#     def total_price(self):
#         return sum(item["price"] * item["quantity"] for item in self.items.values())


from typing import Dict, Any

Cart = Dict[str, Dict[str, Any]]


def create_cart() -> Cart:
    return {}


def add_book(cart: Cart, title: str, price: int, quantity: int = 1) -> None:
    if title in cart:
        cart[title]["quantity"] += quantity
    else:
        cart[title] = {"price": price, "quantity": quantity}


def remove_book(cart: Cart, title: str) -> None:
    if title in cart:
        del cart[title]


def total_price_with_discount(cart: Cart) -> int:
    total = total_price(cart)
    if total_books(cart) > 3:
        return int(total * 0.9)  # 10% rabatt
    return total


def login(users: Dict[str, str], username: str, password: str) -> bool:
    return users.get(username) == password


Stock = Dict[str, int]


def add_book_with_stock(
    cart: Cart, stock: Stock, title: str, price: int, quantity: int = 1
) -> None:
    available = stock.get(title, 0)
    to_add = min(quantity, available)
    if to_add == 0:
        return
    stock[title] -= to_add
    add_book(cart, title, price, to_add)


def clear(cart: Cart) -> None:
    cart.clear()


def total_books(cart: Cart) -> int:
    return sum(item["quantity"] for item in cart.values())


def total_price(cart: Cart) -> int:
    return sum(item["price"] * item["quantity"] for item in cart.values())
