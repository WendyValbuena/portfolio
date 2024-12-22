import random
import time

import pytest
from pages.checkout_page import CheckoutPage
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.get_product_page import GetProductPage
from pages.product_page import ProductPage


@pytest.mark.parametrize(
    "username, password, age_date, street_address, city, postal_code, card_number, card_name, expiry_date, card_code, star, product_name, comment, new_star, expected_message, expected_outcome",
    [
        ('ramovalbuena@gmail.com', 'ecd912f4bbd84e', '01-12-1990', 'street 9876', 'Hamburg', '27480', '83466434233',
         'Joseph Dong', '01/2026', '407', 5, 'Simply Pepperoni Pizza', 'very good quality and taste', random.randint(1, 4).__str__(), 'Boundary of 5 stars', 'Verify that a user can submit a rating exactly at the boundary of 5 stars.'),
        ('wendyvalbuena@gmail.com', 'ecd912f4bbd84e', '12-11-1980', 'street 12', 'Luneburg', '23436', '65776445321',
         'Kamile Muller', '05/2030', '607', 3, 'Ocean Sea King Prawns', 'Interesting flavors', random.randint(1, 5).__str__(), 'Boundary of 3 stars', 'Submit a rating of 3 stars as a valid mid-point rating.'),
        ('ramovalbuena@gmail.com', 'ecd912f4bbd84e', '14-06-1970', 'street 235', 'Berlin', '65432', '995484763621',
         'France Valbuena', '06/2032', '901', 2, 'Freshona', '',  random.randint(2, 5).__str__(),'Rating is submitted without feedback.', 'Submit rating without comments'),
        ('wendyvalbuena@gmail.com', 'ecd912f4bbd84e', '06-09-2000', 'street 657', 'Hanover', '29834', '84635252632',
         'Jessica Smith', '06/2028', '745', 1, 'Rocket', 'Shit product', random.randint(2, 5).__str__(), 'Inappropriate language detected', 'Submit feedback with offensive terms')

    ]
)
def test_rate_product_new(browser, username, password, age_date, street_address, city, postal_code, card_number,
                          card_name, expiry_date, card_code, star, product_name, comment, new_star, expected_message, expected_outcome):

    index_page = IndexPage(browser)
    index_page.open()
    login_page = LoginPage(browser)
    login_page.go_to_login_page()

    login_page.click_login_button(username, password)
    index_page.click_shop_button()

    get_product_page = GetProductPage(browser)
    time.sleep(5)

    get_product_page.age_verification(age_date)
    time.sleep(3)

    get_product_page.click_on_frozen_menu()

    get_product_page.select_product_name(product_name)
    time.sleep(3)

    index_page.click_cart_icon()

    checkout_page = CheckoutPage(browser)
    checkout_page.select_shipment_address(street_address, city, postal_code)
    checkout_page.select_payment(card_number, card_name, expiry_date, card_code)
    time.sleep(3)
    checkout_page.click_buy_now_button()
    time.sleep(5)
    index_page.click_shop_button()
    time.sleep(5)

    get_product_page.click_on_frozen_menu()
    get_product_page.click_product_frozen(product_name)
    time.sleep(5)
    product_page = ProductPage(browser)
    product_page.select_star(star)
    product_page.add_comment(comment)
    product_page.send_button()
    time.sleep(3)

    concurrent_star = product_page.get_concurrent_value_star()
    star = star.__str__()
    assert "(" + star + ")" in concurrent_star, "The star do not match"

    product_page.refresh_page()
    time.sleep(5)
    expected_message = product_page.get_confirmation_message()
    assert "You have already reviewed this product." in expected_message, "Product no reviewed"
    time.sleep(3)

    product_page.click_options()
    time.sleep(1)
    product_page.click_edit()
    product_page.edit_star(new_star)
    product_page.edit_comment(comment + "_changed")
    time.sleep(5)
    product_page.click_save_changes()

    time.sleep(2)
    concurrent_star = product_page.get_concurrent_value_star()
    new_star = new_star.__str__()
    assert "(" + new_star + ")" in concurrent_star, "The star do not match"

    concurrent_comment = product_page.get_concurrent_comment()
    assert comment + "_changed" in concurrent_comment, "The comment do not match"

    time.sleep(1)
    product_page.click_options()
    product_page.click_delete()
    time.sleep(2)

    login_page.go_to_login_page()
    login_page.click_logout_button()
    time.sleep(3)

    browser.delete_all_cookies()
    browser.execute_script("window.sessionStorage.clear();")
    browser.execute_script("localStorage.clear();")

    time.sleep(3)

    print(expected_outcome)

