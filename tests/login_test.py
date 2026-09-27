from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login():

    driver = webdriver.Chrome()

    driver.get(
        "https://portal.company.com"
    )

    driver.implicitly_wait(10)

    driver.find_element(
        By.XPATH,
        "//input[@id='username']"
    ).send_keys(
        "employee.user"
    )

    driver.find_element(
        By.XPATH,
        "//input[@id='password']"
    ).send_keys(
        "Password@123"
    )

    time.sleep(5)

    driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    ).click()

    time.sleep(3)

    dashboard = driver.find_element(
        By.XPATH,
        "//div[contains(text(),'Welcome')]"
    )

    assert dashboard.is_displayed()

    driver.quit()
