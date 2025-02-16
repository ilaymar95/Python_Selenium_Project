from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CartPopUp:
    def __init__(self,driver:webdriver.Edge):
        """Initialize the BearStoreToolBar with a WebDriver instance."""
        self.driver = driver

    def cart_total_items_amount(self):
        """Return the total number of items in the cart."""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '#cart-tab > span.badge.badge-pill.label-cart-amount.badge-warning'))
            )
            # Additional wait for text content to be updated
            WebDriverWait(self.driver, 2).until(lambda driver: element.text != '')
            return element.text
        except TimeoutException:
            return '0'  # Returning '0' to indicate the cart is empty

    def cart_product_name(self):
        """Locate and return all product names in the cart popup."""
        return self.driver.find_elements(By.CSS_SELECTOR, "div.col.col-data > a")

    def cart_product_price(self):
        """Locate and return all product prices in the cart popup."""
        return self.driver.find_elements(By.CLASS_NAME, "price.unit-price")

    def cart_product_quantity(self):
        """Locate and return all product quantities in the cart popup."""
        elements = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.ID, "item_EnteredQuantity")))
        return elements

    def find_subtotal(self):
        """Locate and return the subtotal element in the cart popup."""
        subtotal_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sub-total.price"))  # Ensure selector is correct
        )
        return subtotal_element

    def go_to_cart(self):
        """Click the cart button to navigate to the shopping cart page."""
        cart = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.btn-success'))
        )
        self.driver.execute_script("arguments[0].click();", cart)

    def go_to_checkout(self):
        """Click the checkout button to proceed with the purchase."""
        checkout = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.btn-clear.btn-block.btn-action > span')))
        self.driver.execute_script("arguments[0].click();", checkout)
