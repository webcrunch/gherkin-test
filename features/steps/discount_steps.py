from behave import when, then
from cart import add_book, total_price_with_discount


@when("jag lägger till {antal:d} böcker med pris {pris:d}")
def step_add_multiple_books(context, antal, pris):
    for i in range(antal):
        add_book(context.cart, f"Bok{i}", pris)


@then("den rabatterade summan ska vara {förväntat:d}")
def step_check_discounted_total(context, förväntat):
    assert total_price_with_discount(context.cart) == förväntat
