from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BearStoreCheckout:
    def __init__(self,driver:webdriver.Edge):
        """Initialize the BearStoreToolBar with a WebDriver instance."""
        self.driver = driver

    def billing_address(self):
        """Locate and return the billing address button."""
        address = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.address-item > button')))
        return address

    def click_billing_address(self):
        """Click the billing address button."""
        address = self.billing_address()
        self.driver.execute_script('arguments[0].click();', address)

    def shipping_address(self):
        """Locate and return the shipping address button."""
        address = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.address-item > button')))
        return address

    def click_shipping_address(self):
        """Click the shipping address button."""
        address = self.shipping_address()
        self.driver.execute_script('arguments[0].click();', address)

    def confirm_shipping_method(self):
        """Click the button to confirm the selected shipping method."""
        confirm = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.buttons > button.shipping-method-next-step-button')))
        self.driver.execute_script('arguments[0].click();', confirm)

    def confirm_payment_method(self):
        """Click the button to confirm the selected payment method."""
        confirm = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div > button.payment-method-next-step-button')))
        self.driver.execute_script('arguments[0].click();', confirm)

    def agree_to_terms(self):
        """Click the checkbox to agree to the terms and conditions."""
        agree = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input#termsofservice'))
        )
        self.driver.execute_script('arguments[0].click();', agree)

    def confirm_checkout(self):
        """Click the button to confirm the checkout process."""
        confirm = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-buy'))
        )
        self.driver.execute_script('arguments[0].click();', confirm)

    def get_order_number(self):
        """Locate and return the order number after checkout."""
        order_number = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'p > a > strong'))
        )
        return order_number

    def go_to_order_details(self):
        """Click the button to navigate to the order details page."""
        order_details = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.btn-warning'))
        )
        self.driver.execute_script('arguments[0].click();', order_details)

    def get_completed_order_number(self):
        """Locate and return the completed order number."""
        completed_order_number = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.page-title.mb-3.col > h1 > small > small'))
        )
        return completed_order_number.text
