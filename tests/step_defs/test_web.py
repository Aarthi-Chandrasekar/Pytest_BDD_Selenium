from assertpy import assertpy
from pytest_bdd import scenarios,given, when, then, parsers
from pages.HomePage import HomePage
from config.environment import Environment

scenarios('../features/web.feature')


@when(parsers.parse('I enter "{username}" in user field "{password}" in password field and click login'))
def login_with_credential(browser, login_page, username, password):
    login_page.do_login(username, password)

@when(parsers.parse("User adds an item to the cart"))
def add_item_to_cart(browser):
    home_page = HomePage(browser)
    home_page.click_invetory();


@then(parsers.parse('The item is added to the cart successfully'))
def verify_login(browser):
    home_page = HomePage(browser)



