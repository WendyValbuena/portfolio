from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import *


class GetProductPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def age_verification(self, age_date):
        age_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='DD-MM-YYYY']"))
        )
        age_input.send_keys(age_date)

        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='DD-MM-YYYY']/following-sibling::button[text()='Confirm']"))
        )
        confirm_button.click()

    def select_product(self, productCode):
        first_add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(), 'Add to Cart')])[" + productCode + "]"))
        )
        first_add_to_cart_button.click()

    def click_on_alcoholic_menu(self):
        alcoholic_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Alocohol')]"))
        )
        alcoholic_menu.click()

    def click_on_price_category(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='widget widget-menu']//a[text()='5€ - 10€']"))
        ).click()

    def response_alcohol(self):
        try:
            text_alcohol = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[6]/div/div[1]/p"))
            ).text
            return text_alcohol

        except Exception as e:
            message_alcohol = "You are underage and cannot view alcohol products."
            return message_alcohol

    def select_product_name(self, product_name):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f"//p[@class='lead' and contains(text(), '{product_name}')]/ancestor::div["
                 f"@class='product-card']//button[contains(@class, 'btn-cart')]"))
        )
        add_to_cart_button.click()

    def click_on_frozen_menu(self):
        frozen_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='root']/div/div[3]/div[1]/div/div[1]/ul/li[9]/a"))
        )
        frozen_menu.click()

    def click_product_frozen(self, product_name):
        add_to_cart_button_frozen = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f"//p[@class='lead' and contains(text(), '{product_name}')]"))
        )
        add_to_cart_button_frozen.click()


