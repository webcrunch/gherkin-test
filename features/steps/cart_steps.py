from behave import given, when, then
from cart import (
    create_cart,
    add_book,
    remove_book,
    clear,
    total_books,
    total_price,
)


@given("en tom varukorg")
def step_impl(context):
    context.cart = create_cart()


@given('en varukorg med boken "{title}" (pris {price:d})')
def step_impl(context, title, price):
    context.cart = create_cart()
    add_book(context.cart, title, price)


# För att kunna skriva "And boken X (pris Y)" i feature-filen
@given('boken "{title}" (pris {price:d})')
def step_impl(context, title, price):
    add_book(context.cart, title, price)


@when('jag lägger till boken "{title}" med pris {price:d}')
def step_impl(context, title, price):
    add_book(context.cart, title, price)


@when('jag tar bort boken "{title}"')
def step_impl(context, title):
    remove_book(context.cart, title)


@when("jag tömmer varukorgen")
def step_impl(context):
    clear(context.cart)


@then("ska varukorgen vara tom")
def step_impl(context):
    assert total_books(context.cart) == 0


@then("ska varukorgen innehålla {count:d} bok")
@then('ska varukorgen innehålla {count:d} exemplar av "{title}"')
def step_impl(context, count, title=None):
    if title:
        assert context.cart[title]["quantity"] == count
    else:
        assert total_books(context.cart) == count


@then("den totala summan ska vara {total:d}")
def step_impl(context, total):
    assert total_price(context.cart) == total
