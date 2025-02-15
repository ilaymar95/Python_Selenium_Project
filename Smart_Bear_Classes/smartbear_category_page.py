from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CategoryPage:
    def __init__(self,driver:webdriver.Edge):
        """Initialize the BearStoreSubCategoryPage with a WebDriver instance."""
        self.driver = driver

    def sub_categories(self):
        """Returns a list of the sub categories in the BearStoreProductPage."""
        try:
            # Wait until the element is present
            categories_div = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "artlist-sub-categories.hide-on-active-filter"))
            )
            return categories_div.find_elements(By.CSS_SELECTOR, 'article > div.art-genericname > a')
        except (TimeoutException, NoSuchElementException):
            return None

    def click_category(self,category_name):
        """Returns the chosen sub category of the BearStoreProductPage."""
        categories_list = self.sub_categories()
        for category in categories_list:
            if category_name.lower() == category.text.lower():
                category.click()
                break
    def product(self):
        """Returns a list of the products in the BearStoreProductPage."""
        product_div = self.driver.find_element(By.CSS_SELECTOR,"div.product-list-container > div.artlist.artlist-grid.artlist-4-cols")
        return product_div.find_elements(By.CSS_SELECTOR, "article>h3>a")

    def click_product(self,product_name):
        """Returns the chosen sub category of the BearStoreProductPage."""
        product_list = self.product()
        for product in product_list:
            if product_name.lower() == product.text.lower():
                product.click()
                break

    def get_category_name(self):
        """Returns the name of the chosen category"""
        return self.driver.find_element(By.CSS_SELECTOR,'#content-center > div > div.page-title > h1')