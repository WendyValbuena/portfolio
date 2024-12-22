from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def select_star(self, star_number):
        stars = self.driver.find_elements(By.CSS_SELECTOR, ".interactive-rating .star")

        star_to_click = stars[star_number - 1]
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(star_to_click))
        star_to_click.click()

    def add_comment(self, comment):
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='What is your view?']").send_keys(comment)

    def send_button(self):
        self.driver.find_element(By.XPATH, "//button[text()='Send ']").click()

    def get_confirmation_message(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='reviewRestriction']/p[text()='You have already reviewed this "
                                        "product.']").text

    def refresh_page(self):
        self.driver.refresh()

    def get_concurrent_value_star(self):
        return self.driver.find_element(By.XPATH, "//div[@class='comment-actions']//span[@class='small']").text

    def click_options(self):
        self.driver.find_element(By.XPATH, "//div[@class='menu-icon']").click()

    def click_edit(self):
        self.driver.find_element(By.XPATH, "//div[@class='dropdown-menu']/button[text()='Edit']").click()

    def click_delete(self):
        self.driver.find_element(By.XPATH, "//div[@class='dropdown-menu']/button[text()='Delete']").click()
        confirm = self.driver.switch_to.alert
        confirm.accept()

    def edit_star(self, star_number):
        control_start = self.driver.find_element(By.XPATH, "//input[@type='number']")
        control_start.clear()
        control_start.send_keys(star_number)

    def edit_comment(self, new_comment):
        control_comment = self.driver.find_element(By.XPATH, "//textarea")
        control_comment.clear()
        control_comment.send_keys(new_comment)

    def click_save_changes(self):
        self.driver.find_element(By.XPATH, "//button[text()='Save Changes']").click()

    def get_concurrent_comment(self):
        return self.driver.find_element(By.XPATH, "//div[@class='comment-body']/p[1]").text
