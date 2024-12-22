import time

import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.constants import USERNAME, PASSWORD


@pytest.mark.parametrize("username, password, success_message", [
    (USERNAME, PASSWORD, "valid credentials"),
])
def test_login(browser, username, password, success_message):
    login_page = LoginPage(browser)
    login_page.go_to_login_page()
    login_page.click_login_button(username, password)
    time.sleep(1)

    success_message = browser.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/ul/li[1]/a")
    assert "Home" in success_message.text, "Valid credentials"

    print("Valid credentials")

