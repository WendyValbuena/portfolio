import time

import pytest
from login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestLoginPage:


    BASE_URL = "https://academy.masterschool.com"

    def test_successful_login(self, browser):

        browser.get(self.BASE_URL)

        login_page = LoginPage(browser)

        login_page.login("ramovalbuena@gmail.com", "ecd912f4bbd84e")

        time.sleep(2)

        success_message = browser.find_element("xpath", "//*[@id='table-of-contents']/h1").text
        assert "Successfully logged in!" in success_message, "Login message did not appear"

    def test_invalid_login(self, browser):

        browser.get(self.BASE_URL)

        login_page = LoginPage(browser)

        login_page.login("ramovalbuena@gmail.com", "122344435")

        time.sleep(2)

        error_text = login_page.get_error_message()
        assert "Invalid login" in error_text, "Invalid credentials"
