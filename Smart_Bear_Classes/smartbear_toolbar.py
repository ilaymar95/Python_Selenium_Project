from selenium import webdriver
from selenium.webdriver.common.by import By
class BearStoreToolBar:
    def __init__(self,driver:webdriver.Edge):
        """Initialize the BearStoreToolBar with a WebDriver instance."""
        self.driver = driver

    def toolbar_logo(self):
        """Returns to Smart Bear main page"""
        return self.driver.find_element(By.CSS_SELECTOR,"a>brand")
    def toolbar_menu(self):
        """Opens menu in smart bear mainpage"""
        return self.driver.find_element(By.ID,"shopbar-menu")
    def toolbar_login(self):
        return self.driver.find_element(By.ID,"shopbar-user")
    def toolbar_compare(self):
        return self.driver.find_element(By.ID,"shopbar-user")