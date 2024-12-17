from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:

    def __init__(self, driver: WebDriver, navbar=None):
        self.driver = driver

        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.ID, "login_button")
        self.login_message = [By.XPATH, "//*[@id='table-of-contents']/h1/text()"]
        self.error_message = [By.XPATH, "//*[@id='navbar']/div[1]"]

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

