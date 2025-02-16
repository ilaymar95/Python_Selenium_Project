from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BearStoreToolBar:
    def __init__(self,driver:webdriver.Edge):
        """Initialize the BearStoreToolBar with a WebDriver instance."""
        self.driver = driver

    def toolbar_logo_click(self):
        """
        Clicks the toolbar logo using JavaScript if a blocking element prevents a normal click.
        """
        logo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "brand")))
        self.driver.execute_script("arguments[0].click();", logo)

    def toolbar_menu(self):
        """Opens menu in smart bear mainpage."""
        return self.driver.find_element(By.ID, "shopbar-menu")

    def toolbar_menu_click(self):
        """Click the menu button in the toolbar."""
        self.toolbar_menu().click()

    def toolbar_login(self):
        """Locate and return the login link in the toolbar."""
        return self.driver.find_element(By.CSS_SELECTOR, "nav#menubar-my-account > div.dropdown > a")

    def toolbar_login_click(self):
        """Click the login link in the toolbar."""
        self.toolbar_login().click()

    def toolbar_compare(self):
        """Locate and return the compare link in the toolbar."""
        return self.driver.find_element(By.CSS_SELECTOR, "#shopbar-compare > a")

    def toolbar_compare_click(self):
        """Click the compare link in the toolbar."""
        self.toolbar_compare().click()

    def toolbar_wishlist(self):
        """Locate and return the wishlist link in the toolbar."""
        return self.driver.find_element(By.ID, "shopbar-wishlist")

    def toolbar_wishlist_click(self):
        """Click the wishlist link in the toolbar."""
        self.toolbar_wishlist().click()

    def toolbar_cart(self):
        """Locate and return the cart link in the toolbar."""
        cart = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#shopbar-cart > a.shopbar-button.navbar-toggler"))
        )
        return cart

    def toolbar_cart_click(self):
        """Click the cart link in the toolbar."""
        cart = self.toolbar_cart()
        self.driver.execute_script("arguments[0].click();", cart)

    def toolbar_search(self):
        """Locate and return the search button in the toolbar."""
        return self.driver.find_element(By.CSS_SELECTOR, "form > button")

    def toolbar_search_click(self):
        """Click the search button in the toolbar."""
        self.toolbar_search().click()

    def toolbar_search_input(self):
        """Locate and return the search input field in the toolbar."""
        return self.driver.find_element(By.CLASS_NAME, "instasearch-term form-control")

    def toolbar_search_input_fill(self, fill):
        """Clear the search input field and enter the search term."""
        self.toolbar_search_input().clear()
        self.toolbar_search_input().send_keys(fill)

    def toolbar_account_click(self):
        """Click the account link in the toolbar."""
        account = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "nav#menubar-my-account > div.dropdown > a")))
        self.driver.execute_script("arguments[0].click();", account)

    def toolbar_account_name(self):
        """Locate and return the account name element in the toolbar."""
        return self.driver.find_element(By.CSS_SELECTOR, "nav#menubar-my-account > div.dropdown > a > span")

    def toolbar_logout(self):
        """Click the logout link in the toolbar."""
        logout_account = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.dropdown-menu.dropdown-menu-right.show > a")))
        self.driver.execute_script("arguments[0].click();", logout_account[-1])
