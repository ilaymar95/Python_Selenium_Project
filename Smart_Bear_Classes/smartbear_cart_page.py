from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BearStoreCartPage:
    def __init__(self,driver:webdriver.Edge):
        """Initialize the BearStoreToolBar with a WebDriver instance."""
        self.driver = driver

    def find_shopping_cart(self):
        """Locate the shopping cart element on the page."""
        cart = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#content-center > div.page.shopping-cart-page')))
        return cart

    def empty_cart(self):
        """Remove all items from the shopping cart."""
        while True:
            try:
                # Re-locate the remove buttons inside the loop to avoid stale element exception
                remove_btns = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                         'div.cart-row-actions.btn-group-vertical > a.btn-to-danger.btn-sm.btn-icon.ajax-action-link'))
                )
                # If no remove buttons are found, break the loop
                if not remove_btns:
                    break
                # Click the last remove button
                remove_btns[-1].click()
                # Wait for a short period to ensure the element is removed from the DOM
                WebDriverWait(self.driver, 1).until(EC.staleness_of(remove_btns[-1]))
            except (TimeoutException, StaleElementReferenceException):
                # If a timeout or stale element exception occurs, continue the loop to re-locate the elements
                break

    def find_products_names(self):
        """Locate and return all product names in the shopping cart."""
        prod_names = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'a.cart-item-link')))
        return prod_names

    def cart_page_product_subtotal_price(self):
        """Locate and return all product subtotal prices in the shopping cart."""
        subtotal_prod_prices = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.cart-col-subtotal> span.price')))
        return subtotal_prod_prices

    def cart_page_product_price(self):
        """Locate and return all product prices in the shopping cart."""
        prod_prices = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.cart-col-price[data-caption="Price"] > span.price')))
        return prod_prices

    def find_products_quantities(self):
        """Locate and return all product quantities in the shopping cart."""
        prod_quantities = WebDriverWait(self.driver,5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.input-group.bootstrap-touchspin > input')))
        return prod_quantities

    def change_quantity(self,element,quantity):
        """Change the quantity of a product in the shopping cart."""
        element.clear()
        element.send_keys(quantity)

    def cart_summary_total(self):
        """Locate and return the total price of the shopping cart."""
        sub_total = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'tr.cart-summary-total > td.cart-summary-value > span')))
        return sub_total

    def checkout(self):
        """Click the checkout button to proceed with the purchase."""
        checkout = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.ID,'checkout')))
        self.driver.execute_script("arguments[0].click();", checkout)
