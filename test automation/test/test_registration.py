import time

import pytest
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.mark.parametrize(
    "username_new, password_new, email_new, message",
    [
        ('Tester_user_5', '2425226626', 'Testeruser5@gmail.com', 'New user register'),
        ('Tester_user_6', '2425226626', 'Testeruser6@gmail.com', 'New user register'),

    ]
)
def test_registration(browser, username_new, email_new, password_new, message):
    index_page = IndexPage(browser)
    index_page.open()

    login_page = LoginPage(browser)
    login_page.go_to_login_page()

    registration_page = RegistrationPage(browser)
    registration_page.click_create_new_account()
    registration_page.create_account(username_new, password_new, email_new)
    time.sleep(3)

    print("New user register")
