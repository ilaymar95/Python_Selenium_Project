from selenium import webdriver
from selenium.webdriver.common.by import By
from random import choice
"""The class for the product page"""
class ProductPage:
    def __init__(self,driver:webdriver.Edge):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.page-title > h1')

    def get_product_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.pd-price > span')

    def add_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, 'btn-add-to-cart').click()

    def get_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input.form-control.form-control-lg')

    def change_quantity(self, quantity):
        self.get_quantity().clear()
        self.get_quantity().send_keys(quantity)

    def choose_color(self):
        """Choose a color for the product - Not all products have colors"""
        choice(self.driver.find_elements(By.CSS_SELECTOR, '#choice-boxes-13 > ul')).click()


