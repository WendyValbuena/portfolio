import time

import pytest
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.get_product_page import GetProductPage


@pytest.mark.parametrize(
    "username, password, age_date, expected_message, expected_outcome",
    [
        ('ramovalbuena@gmail.com', 'ecd912f4bbd84e', '12-04-2006', 'Corona Extra',
         'Access to alcoholic products is granted.'),
        ('wendyvalbuena@gmail.com', 'ecd912f4bbd84e', '05-08-2007', 'You are underage and cannot view alcohol products.',
         'Error message: "Access denied. You must be at least 18 years old.'),
        ('ramovalbuena@gmail.com', 'ecd912f4bbd84e', '03-12-2005', 'Corona Extra',
         'Access granted to alcoholic products.'),
        ('wendyvalbuena@gmail.com', 'ecd912f4bbd84e', '', 'You are underage and cannot view alcohol products.',
         'Error message: "Age is required.'),
        ('ramovalbuena@gmail.com', 'ecd912f4bbd84e', 'abc', 'You are underage and cannot view alcohol products.',
         'Error message: "Invalid age format.'),

    ]
)
def test_alcoholic(browser, username, password, age_date, expected_message, expected_outcome):
    browser.delete_all_cookies()
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

    get_product_page.click_on_alcoholic_menu()
    time.sleep(5)

    response_alcohol = get_product_page.response_alcohol()
    assert response_alcohol in expected_message, "Access to alcohol"

    login_page.go_to_login_page()
    time.sleep(3)
    login_page.click_logout_button()
    browser.delete_all_cookies()
    browser.execute_script("window.sessionStorage.clear();")

    print(expected_outcome)
