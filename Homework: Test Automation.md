## **Task 1**
Write a script that does the following:

1. Opens the URL “https://masterschool.com”
2. Wait for 2-3 seconds.
3. Finds the link that has text “Browse Programs” . Hint: Inspect the link to see which appropriate locator can be used.
4. Click on the link.
5. Wait for 2 seconds.
6. Quit.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://masterschool.com")

    time.sleep(3)

    target_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//section[@id='section-cover-1']/div[@class='container']/div[@class='section-cover__inner']/div[@class='section-cover__row'][2]/div[@class='section-cover__col'][2]/div[@class='section-cover__buttons']/div[@class='section-cover__buttons']/a[@class='button-bordered-white-arrow']"))
    )
    target_element.click()

    time.sleep(2)

finally:
    driver.quit()

## **Task 2**
Write a script that automates the Google search:

1. Opens the URL “https://www.google.com”
2. Finds the search bar input element. Use Inspect to see which locator can be used. 
3. It should send the search term “cats”
4. Add a delay of 3 seconds.
5. Print the title of the document (driver).
6. Quit.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    time.sleep(3)

    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//textarea[@id='APjFqb']"))
    )
    search_box.send_keys("cats")

    search_box.submit()

    time.sleep(3)

    print(driver.title)

finally:
    driver.quit()

## **Task 3**
Write a script that automates the login process of any website of your choice. 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email = "wendy*****@gmail.com"
password = "*******"

driver = webdriver.Chrome()

try:
    driver.get("https://www.netflix.com/login")

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_userLoginId"))
    )
    email_input.send_keys(email)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_password"))
    )
    password_input.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-uia='login-submit-button']"))
    )
    login_button.click()

    time.sleep(5)

    print(driver.title)

finally:
    driver.quit()


