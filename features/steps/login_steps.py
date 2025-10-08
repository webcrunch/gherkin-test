from behave import given, when, then
from cart import login


@given('en användare med användarnamn "{user}" och lösenord "{pwd}"')
def step_impl(context, user, pwd):
    context.users = {user: pwd}


@when('jag försöker logga in med användarnamn "{user}" och lösenord "{pwd}"')
def step_impl(context, user, pwd):
    context.login_result = login(context.users, user, pwd)


@then("inloggningen ska vara {resultat}")
def step_impl(context, resultat):
    expected = resultat == "lyckad"
    assert context.login_result == expected
