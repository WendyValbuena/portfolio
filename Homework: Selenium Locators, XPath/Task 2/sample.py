from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    page_sample = ("file:///Users/ramonavalbuena/Documents/Pycharm/Selenium Locators, XPath/sample.html")
    driver.get(page_sample)

    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text' i]"))
    )
    print("ok")

    input_field.send_keys("Hello world")

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit' i]"))
    )

    submit_button.click()
    time.sleep(3)

finally:

    driver.quit()
