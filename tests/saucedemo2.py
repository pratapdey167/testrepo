from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "https://www.saucedemo.com/"
)

# Login

username = driver.find_element(
    By.ID,
    "user-name"
)

password = driver.find_element(
    By.ID,
    "password"
)

username.send_keys(
    "standard_user"
)

password.send_keys(
    "secret_sauce"
)

driver.find_element(
    By.ID,
    "login-button"
).click()

time.sleep(2)

# Verify Inventory Page

assert (
    "inventory"
    in
    driver.current_url.lower()
)

inventory_title = driver.find_element(
    By.CLASS_NAME,
    "title"
)

assert (
    inventory_title.text
    ==
    "Products"
)

# Sort Products

sort_dropdown = driver.find_element(
    By.CLASS_NAME,
    "product_sort_container"
)

sort_dropdown.click()

time.sleep(1)

sort_option = driver.find_element(
    By.XPATH,
    "//option[@value='hilo']"
)

sort_option.click()

time.sleep(2)

# Add Products To Cart

driver.find_element(
    By.ID,
    "add-to-cart-sauce-labs-backpack"
).click()

driver.find_element(
    By.ID,
    "add-to-cart-sauce-labs-bike-light"
).click()

time.sleep(1)

cart_badge = driver.find_element(
    By.CLASS_NAME,
    "shopping_cart_badge"
)

assert cart_badge.text == "2"

# Open Cart

driver.find_element(
    By.CLASS_NAME,
    "shopping_cart_link"
).click()

time.sleep(2)

# Validate Cart

cart_items = driver.find_elements(
    By.CLASS_NAME,
    "inventory_item_name"
)

assert len(cart_items) == 2

# Checkout

driver.find_element(
    By.ID,
    "checkout"
).click()

time.sleep(1)

driver.find_element(
    By.ID,
    "first-name"
).send_keys(
    "Pratap"
)

driver.find_element(
    By.ID,
    "last-name"
).send_keys(
    "Dey"
)

driver.find_element(
    By.ID,
    "postal-code"
).send_keys(
    "700001"
)

driver.find_element(
    By.ID,
    "continue"
).click()

time.sleep(2)

# Verify Checkout Overview

overview_title = driver.find_element(
    By.CLASS_NAME,
    "title"
)

assert (
    overview_title.text
    ==
    "Checkout: Overview"
)

driver.find_element(
    By.ID,
    "finish"
).click()

time.sleep(2)

# Verify Success

success_message = driver.find_element(
    By.CLASS_NAME,
    "complete-header"
)

assert (
    success_message.text
    ==
    "Thank you for your order!"
)

# Logout

driver.find_element(
    By.ID,
    "react-burger-menu-btn"
).click()

time.sleep(1)

WebDriverWait(
    driver,
    10
).until(
    EC.element_to_be_clickable(
        (
            By.ID,
            "logout_sidebar_link"
        )
    )
).click()

time.sleep(2)

driver.quit()
