from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_employee_portal_login():

    driver = webdriver.Chrome()

    try:
        # Open Employee Portal
        driver.get(
            "https://employee-portal.company.com"
        )

        # Framework-level wait
        driver.implicitly_wait(10)

        # Username
        driver.find_element(
            By.XPATH,
            "//input[@id='username']"
        ).send_keys(
            "john.smith"
        )

        # Password
        driver.find_element(
            By.XPATH,
            "//input[@id='password']"
        ).send_keys(
            "Password@123"
        )

        # Hard wait before login
        time.sleep(5)

        driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

        # Hard wait before dashboard verification
        time.sleep(3)

        dashboard = driver.find_element(
            By.XPATH,
            "//div[contains(text(),'Welcome')]"
        )

        assert dashboard.is_displayed()

        # Open profile section
        driver.find_element(
       
