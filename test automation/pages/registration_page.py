from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    def click_create_new_account(self):
        self.driver.find_element(By.XPATH, "//a[text()='Create a new account']").click()

    def create_account(self, new_user, new_password, new_email):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys(new_user)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email address']").send_keys(new_email)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(new_password)
        self.driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
