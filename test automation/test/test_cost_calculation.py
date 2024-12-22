import time

import pytest

from pages.checkout_page import CheckoutPage
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.get_product_page import GetProductPage


@pytest.mark.parametrize(
    "username, password, age_date, product_name, plus_number, minus_number, expected_value, expected_outcome",
    [
        ('ramovalbuena@gmail.com', 'ecd912f4bbd84e', '12-12-2000', 'Gala', 9, 0, 0,
         'Expected Outcome: Free shipping applied 0€'),
        ('wendyvalbuena@gmail.com', 'ecd912f4bbd84e', '03-10-1998', 'Asparagus', 10, 0, 5,
         'Expected Outcome: Shipping fee added'),
        ('ramovalbuena@gmail.com', 'ecd912f4bbd84e', '06-08-1978', 'Cauliflower', 9, 0, 5,
         'Expected Outcome: Order total = 15€'),
        ('wendyvalbuena@gmail.com', 'ecd912f4bbd84e', '23-06-1987', 'Pink Lady', 19, 0, 0,
         'You qualify for free shipping!'),
        ('ramovalbuena@gmail.com', 'ecd912f4bbd84e', '06-08-2000', 'Tenderstem', 66, 0, 0,
         'Message: "You qualify for free shipping!"'),
        ('wendyvalbuena@gmail.com', 'ecd912f4bbd84e', '23-06-1987', 'Kale', 20, 5, 0,
         'Expected Outcome: Shipping fee no re-applied.')

    ]
)
def test_cost_calculation(browser, username, password, age_date, product_name, plus_number, minus_number,
                          expected_value, expected_outcome):
    index_page = IndexPage(browser)
    index_page.open()
    login_page = LoginPage(browser)

    login_page.go_to_login_page()
    login_page.click_login_button(username, password)
    index_page.click_shop_button()

    get_product_page = GetProductPage(browser)
    time.sleep(5)
    get_product_page.age_verification(age_date)
    time.sleep(5)

    get_product_page.select_product_name(product_name)

    time.sleep(3)
    index_page.click_cart_icon()

    checkout_page = CheckoutPage(browser)
    time.sleep(1)
    checkout_page.click_on_plus(plus_number)

    time.sleep(1)
    checkout_page.get_shipment_value()

    checkout_page.click_on_minus(minus_number)
    time.sleep(1)

    shipment_value = checkout_page.get_shipment_value()

    assert expected_value.__str__() in shipment_value, "Shipment cost do not match. It's not 0 the cost."

    time.sleep(1)
    checkout_page.click_on_remove_product()

    time.sleep(1)
    login_page.go_to_login_page()
    time.sleep(3)
    login_page.click_logout_button()

    browser.delete_all_cookies()
    browser.execute_script("window.sessionStorage.clear();")
    browser.execute_script("localStorage.clear();")

    time.sleep(3)

    print(expected_outcome)
