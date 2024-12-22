from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def select_shipment_address(self, street_address, city, postal_code):
        address_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Street Address']"))
        )
        address_input.send_keys(street_address)

        city_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='City']"))
        )
        city_input.send_keys(city)

        postal_code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Postal Code']"))
        )
        postal_code_input.send_keys(postal_code)

    def select_payment(self, card_number, card_name, expiry_date, card_code):
        card_number_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Card number']"))
        )
        card_number_input.send_keys(card_number)

        card_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name on card']"))
        )
        card_name_input.send_keys(card_name)

        expiry_date_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Expiration']"))
        )
        expiry_date_input.send_keys(expiry_date)

        card_code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Cvv']"))
        )
        card_code_input.send_keys(card_code)

    def click_buy_now_button(self):
        buy_now_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Buy now']"))
        )
        buy_now_button.click()

    def click_on_plus(self, plus_number):
        plus_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='plus']"))
        )

        for _ in range(plus_number):
            plus_button.click()

    def click_on_minus(self, minus_number):
        minus_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='minus']"))
        )

        for _ in range(minus_number):
            minus_button.click()

    def get_shipment_value(self):
        value_with_symbol = self.driver.find_element(By.XPATH, "//div[@class='shipment-container']/h5[2]").text
        return value_with_symbol.replace('€', '').strip()

    def click_on_remove_product(self):
        remove_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//a[@class='remove-icon'])"))
        )
        remove_button.click()

    def shipment_value_after_removal(browser):
        checkout_page = CheckoutPage(browser)

        checkout_page.click_on_remove_product()
        shipment_value_after_removal = checkout_page.get_shipment_value()

        return shipment_value_after_removal