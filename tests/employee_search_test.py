from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_employee_search():

    driver = webdriver.Chrome()

    driver.get(
        "https://portal.company.com/employees"
    )

    driver.implicitly_wait(10)

    search_box = driver.find_element(
        By.XPATH,
        "//input[@placeholder='Search Employee']"
    )

    search_box.send_keys(
        "John Smith"
    )

    time.sleep(3)

    driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Search')]"
    ).click()

    employee = driver.find_element(
        By.XPATH,
        "//td[contains(text(),'John Smith')]"
    )

    assert employee.is_displayed()

    driver.quit()
