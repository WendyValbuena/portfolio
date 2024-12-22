from selenium.webdriver.common.by import By
from utils.constants import *


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.get(LOGIN_URL)

    def expected_message(self):
        return self.driver.find_element(self.expected_message).text

    def click_login_button(self, username, password):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email address']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, "//button[text()='Logout']").click()