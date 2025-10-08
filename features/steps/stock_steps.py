from behave import given, when, then
from cart import create_cart, add_book_with_stock


@given('en bok "{title}" med pris {price:d} och lagersaldo {saldo:d}')
def step_impl(context, title, price, saldo):
    context.cart = create_cart()
    context.stock = {title: saldo}
    context.title = title
    context.price = price


@when('jag försöker köpa {antal:d} exemplar av "{title}"')
def step_impl(context, antal, title):
    add_book_with_stock(context.cart, context.stock, title, context.price, antal)


@then('varukorgen ska innehålla {antal:d} exemplar av "{title}"')
def step_impl(context, antal, title):
    assert context.cart[title]["quantity"] == antal
