from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import *

class IndexPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def click_shop_button(self):
        shop_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Shop']"))
        )
        shop_button.click()

    def click_cart_icon(self):
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='headerIcon'][3]"))
        )
        cart_icon.click()

    def close(self):
        self.driver.quit()