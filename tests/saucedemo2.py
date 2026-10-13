import re
from playwright.sync_api import Page, expect

def test_saucedemo_checkout_flow_playwright(page: Page) -> None:
    # Setup and navigate
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://www.saucedemo.com/")

    # Login
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Verify Inventory Page
    expect(page).to_have_url(re.compile("inventory", re.IGNORECASE))
    expect(page.locator(".title")).to_have_text("Products")

    # Sort Products
    sort_dropdown = page.get_by_role("combobox")
    sort_dropdown.click()
    sort_dropdown.select_option("hilo")

    # Add Products To Cart
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-bike-light").click()

    # Verify Cart Badge Count
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("2")

    # Open Cart
    page.locator(".shopping_cart_link").click()

    # Validate Cart
    cart_items = page.locator(".inventory_item_name")
    expect(cart_items).to_have_count(2)

    # Checkout
    page.locator("#checkout").click()
    page.get_by_placeholder("First Name").fill("Pratap")
    page.get_by_placeholder("Last Name").fill("Dey")
    page.get_by_placeholder("Zip/Postal Code").fill("700001")
    page.locator("#continue").click()

    # Verify Checkout Overview
    expect(page.locator(".title")).to_have_text("Checkout: Overview")
    page.locator("#finish").click()

    # Verify Success
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

    # Logout
    page.locator("#react-burger-menu-btn").click()
    logout_link = page.locator("#logout_sidebar_link")
    expect(logout_link).to_be_visible()
    logout_link.click()