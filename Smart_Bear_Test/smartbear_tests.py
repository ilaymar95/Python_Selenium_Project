from unittest import TestCase
from selenium import webdriver
from random import choice, randint
from time import sleep
import logging
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pythonProject.Smart_Bear_Classes.smartbear_product_page import ProductPage
from pythonProject.Smart_Bear_Classes.smartbear_cart_popup import CartPopUp
from pythonProject.Smart_Bear_Classes.smartbear_category_page import CategoryPage
from pythonProject.Smart_Bear_Classes.smartbear_main_page import BearStoreMainPage
from pythonProject.Smart_Bear_Classes.smartbear_toolbar import BearStoreToolBar
from pythonProject.Smart_Bear_Classes.smartbear_cart_page import BearStoreCartPage
from pythonProject.Smart_Bear_Classes.smartbear_login import BearStoreLoginPage
from pythonProject.Smart_Bear_Classes.smartbear_checkout import BearStoreCheckout
import re


# Logging configuring
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


def extract_price(element: WebElement):
    """
    Extracts the numeric price from a given text.
    Supports large prices (e.g., 9999.9999).
    """
    if element is None:
        return None

    text = element.text.replace(',', '')
    text = text.strip()
    match = re.search(r"\d+\.\d+", text)  # Looks for a floating-point number
    return match.group() if match else None  # Return the matched number as a string

class SmartBearTest(TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.driver = webdriver.Edge()
        self.driver.get("https://bearstore-testsite.smartbear.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.main_page = BearStoreMainPage(self.driver)
        self.toolbar = BearStoreToolBar(self.driver)
        self.category_page = CategoryPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_popup = CartPopUp(self.driver)
        self.cart_page = BearStoreCartPage(self.driver)
        self.checkout = BearStoreCheckout(self.driver)
        self.login_page = BearStoreLoginPage(self.driver)
        self.toolbar.toolbar_cart_click()
        self.clean_cart()
        self.remove_cart_blocker()

    def test_page_transitions(self):
        """Test transition between pages and check that the titles are correct"""
        category_name = choice(self.main_page.categories()).text
        self.main_page.click_category(category_name)
        self.assertEqual(category_name, self.category_page.get_category_name().text)
        # Scroll down slightly on the category page
        self.driver.execute_script("window.scrollBy(0, 350)")       #
        product = choice(self.category_page.product()).text
        self.category_page.click_product(product)
        self.assertEqual(self.product_page.get_product_name().text, product)
        self.driver.back()
        self.assertEqual(category_name, self.category_page.get_category_name().text)
        self.assertEqual(category_name, self.category_page.get_category_name().text)
        self.toolbar.toolbar_logo_click()
        logging.info("Test test_page_transitions completed successfully.")

    def test_add_to_cart(self):
        """
        Adds multiple products to the shopping cart and verifies quantities.
        """
        selected_products = set()  # Track selected products to avoid duplicates
        sum_quantity = 0
        # Add first product
        quantity = randint(2, 5)
        sum_quantity += quantity
        self.add_random_product_to_cart(quantity,True,selected_products)
        self.toolbar.toolbar_logo_click()
        # Add second product with a new random quantity
        quantity = randint(2, 5)
        sum_quantity += quantity
        self.add_random_product_to_cart(quantity, False, selected_products)
        WebDriverWait(self.driver, 5).until( # Ensure UI has updated before checking cart quantity
            lambda driver: self.cart_popup.cart_total_items_amount() == str(sum_quantity)
        )
        self.assertEqual(self.cart_popup.cart_total_items_amount(), str(sum_quantity))
        self.clean_cart()
        logging.info("Test test_add_to_cart completed successfully.")

    def test_add_to_cart_3(self):
        """
        Adds multiple products to the shopping cart and verifies quantities, names, and prices.
        Ensures no duplicate products are selected.
        """
        expected_quantities = []
        expected_product_names = []
        expected_prices = []
        selected_products = set()  # Track selected products to avoid duplicates
        # Add two unique products to the cart
        for _ in range(2):
            quantity = randint(2, 10)
            expected_quantities.append(quantity)
            self.add_random_product_to_cart(quantity, True, selected_products)
            self.remove_cart_blocker()
            expected_product_names.append(self.product_page.get_product_name().text)
            expected_prices.append(self.product_page.get_product_price().text)
            self.toolbar.toolbar_logo_click()

        # Add a third unique product to the cart
        quantity = randint(2, 5)
        expected_quantities.append(quantity)
        self.add_random_product_to_cart(quantity, False, selected_products)
        expected_product_names.append(self.product_page.get_product_name().text)
        expected_prices.append(self.product_page.get_product_price().text)
        actual_names = self.cart_popup.cart_product_name()
        actual_prices = self.cart_popup.cart_product_price()
        actual_quantities = self.cart_popup.cart_product_quantity()
        # the cart gives the list as a stack, therefore running backwards
        for i in range(len(actual_names)):
            self.assertEqual(expected_product_names[i], actual_names[3 - i - 1].text)
            self.assertEqual(expected_prices[i], actual_prices[3 - i - 1].text)
            self.assertEqual(str(expected_quantities[i]), actual_quantities[3 - i - 1].get_attribute('value'))
        self.clean_cart()
        logging.info("Test test_add_to_cart_3 completed successfully.")

    def test_add_to_cart_and_remove(self):
        """
        Adds multiple products to the shopping cart, removes the first item added, and verifies that only the second item remains.
        """
        selected_products = set()
        expected_quantities = []
        for i in range(2):
            # Add the first product
            quantity = randint(2, 10)
            expected_quantities.append(quantity)
            self.add_random_product_to_cart(quantity, True,selected_products)
            self.toolbar.toolbar_logo_click()
        self.toolbar.toolbar_cart_click()
        # Remove the first item added (which is last in the cart list)
        remaining_quantity = str(expected_quantities[-1])
        self.remove_first_cart_item()
        # Wait until UI updates
        WebDriverWait(self.driver, 5).until(
            lambda driver: self.cart_popup.cart_total_items_amount() == remaining_quantity)
        self.assertEqual(self.cart_popup.cart_total_items_amount(), remaining_quantity)
        remaining_quantities = [q.get_attribute('value') for q in self.cart_popup.cart_product_quantity()]
        self.assertEqual(remaining_quantities[0], str(expected_quantities[1]),
                         "Wrong quantity for the remaining product")
        self.clean_cart()
        logging.info("Test test_add_to_cart_and_remove completed successfully.")

    def test_cart_transitions(self):
        selected_products=set()
        self.add_random_product_to_cart(2,False,selected_products)
        self.assertNotEqual(self.cart_popup.cart_total_items_amount(), '0',
                            "Cart total items amount should not be empty after adding a product.")
        self.remove_cart_blocker()
        self.toolbar.toolbar_cart_click()
        self.assertNotEqual(self.cart_popup.cart_total_items_amount(), '0',
                            "Cart total items amount should not be empty after clicking the cart button.")
        self.cart_popup.go_to_cart()
        self.assertIsNotNone(self.cart_page.find_shopping_cart(),
                             "Shopping cart page should be displayed after clicking 'Go to cart'.")
        self.cart_page.empty_cart()
        logging.info("Test test_cart_transitions completed successfully.")

    def test_3_products_details(self):
        """
        Adds three different products to the shopping cart with different quantities.
        Verifies that the total order amount in both the cart popup and the full cart page
        matches the expected total based on product prices and quantities.
        Prints the name, quantity, and price of each product in the cart.
        Ensures no duplicate products are selected.
        """
        selected_products = set()  # Track selected products to avoid duplicates
        for _ in range(2):
            quantity = randint(2, 10)
            self.add_random_product_to_cart(quantity, True, selected_products)
            self.toolbar.toolbar_logo_click()
        # Add a third unique product to the cart
        quantity = randint(2, 5)
        self.add_random_product_to_cart(quantity, False, selected_products)
        # GET Name, Price, Quantity from Popup Cart
        actual_names_popup = [name.text.strip() for name in self.cart_popup.cart_product_name()]
        actual_unit_prices_popup = [extract_price(price) for price in self.cart_popup.cart_product_price()]
        actual_quantities_popup = [qty.get_attribute('value') for qty in self.cart_popup.cart_product_quantity()]
        cart_subtotal = float(extract_price(self.cart_popup.find_subtotal()))
        self.cart_popup.go_to_cart()
        # GET Name, Price, Quantity from Cart Page
        actual_names_cart_page = [name.text.strip() for name in self.cart_page.find_products_names()]
        actual_unit_prices_cart_page = [extract_price(price) for price in
                                        self.cart_page.cart_page_product_price()]  # FIXED: Now correctly gets only unit prices
        actual_subtotal_prices_cart_page = [extract_price(price) for price in
                                            self.cart_page.cart_page_product_subtotal_price()]
        actual_quantities_cart_page = [qty.get_attribute('value') for qty in
                                       self.cart_page.find_products_quantities()]
        total_price = sum(float(price) for price in actual_subtotal_prices_cart_page)
        adjusted_popup_prices = [float(actual_unit_prices_popup[i]) * int(actual_quantities_popup[i])
                                 for i in range(len(actual_unit_prices_popup))]
        adjusted_popup_prices = [round(float(price), 2) for price in adjusted_popup_prices]
        actual_subtotal_prices_cart_page = [round(float(price), 2) for price in actual_subtotal_prices_cart_page]
        logging.info("\n=== Popup Cart Details ===")
        for i in range(len(actual_names_popup)):
            logging.info(
                f"Product: {actual_names_popup[i]}, Unit Price: {actual_unit_prices_popup[i]}, Quantity: {actual_quantities_popup[i]}")
        logging.info("\n=== Cart Page Details ===")
        for i in range(len(actual_names_cart_page)):
            logging.info(f"Product: {actual_names_cart_page[i]}, Unit Price: {actual_unit_prices_cart_page[i]}, "
                         f"Subtotal Price: {actual_subtotal_prices_cart_page[i]}, Quantity: {actual_quantities_cart_page[i]}")
        logging.info(f"\nSubtotal from Cart Popup: {cart_subtotal}")
        logging.info(f"Total Price from Cart Page: {total_price}")
        self.assertEqual(actual_names_popup, actual_names_cart_page,
                         "Mismatch in product names between popup and cart page.")
        self.assertEqual(len(actual_unit_prices_popup), len(actual_unit_prices_cart_page),
                         "Mismatch in the number of unit prices extracted.")
        self.assertEqual(actual_unit_prices_popup, actual_unit_prices_cart_page,
                         "Mismatch in unit prices between popup and cart page.")
        # Assert that the adjusted popup prices and the subtotal prices in the cart page are almost equal within 2 decimal places
        for price_popup, price_cart in zip(adjusted_popup_prices, actual_subtotal_prices_cart_page):
            self.assertAlmostEqual(price_popup, price_cart, 2,"Mismatch in total product prices between popup and cart page.")
        self.assertEqual(actual_quantities_popup, actual_quantities_cart_page,"Mismatch in product quantities between popup and cart page.")
        self.assertEqual(total_price, cart_subtotal,"Mismatch in total price between cart popup and cart page.")
        self.cart_page.empty_cart()
        logging.info("Test test_3_products_details completed successfully.")

    def test_changes_in_2_products(self):
        """
        Adds two products to the shopping cart, navigates to the cart page, and updates the quantities of both products.
        Verifies that the total price for each product is updated correctly based on the new quantity.
        Ensures the overall total price in the cart is updated accordingly.
        Checks that the updated total price is reflected correctly in the cart popup.
        """
        selected_products = set()
        # Add two unique products to the cart
        for _ in range(2):
            quantity = randint(2, 10)
            self.add_random_product_to_cart(quantity, True, selected_products)  # Ensure unique selection
            self.toolbar.toolbar_logo_click()
        self.toolbar.toolbar_cart_click()
        self.cart_popup.go_to_cart()
        prod_quantities = self.cart_page.find_products_quantities()
        for i in range(len(prod_quantities)):
            self.cart_page.change_quantity(i, randint(2, 10))
        updated_quantities = self.cart_page.find_products_quantities()
        cart_prod_sub_total = self.cart_page.cart_page_product_subtotal_price()
        for i in range(len(updated_quantities)):
            product_price = float(extract_price(self.cart_page.cart_page_product_price()[i]))
            updated_quantity = updated_quantities[i].text.strip()
            # Check if updated_quantity is not empty before converting to float
            if updated_quantity:
                updated_quantity = float(updated_quantity)
                expected_sub_total = product_price * updated_quantity
                actual_sub_total = float(extract_price(cart_prod_sub_total[i]))
                self.assertEqual(expected_sub_total, actual_sub_total,
                                 f"Expected subtotal: {expected_sub_total}, but got: {actual_sub_total}")
        total_cost_element = self.cart_page.cart_summary_total()
        total_cost = float(extract_price(total_cost_element))
        sum_cart_total = sum(float(extract_price(sub_total)) for sub_total in cart_prod_sub_total)
        self.assertAlmostEqual(total_cost, sum_cart_total,2,
                         f"Expected total cost: {total_cost}, but got: {sum_cart_total}")
        self.cart_page.empty_cart()
        logging.info("Test test_changes_in_2_products completed successfully.")

    def test_complete_order(self):
        """The test makes a full order cycle:
        Choosing products, Going to checkout, Logging in and completing the order
        The test will verify the order number given matches the order number on order details and that the cart empties
        after a successful order"""
        username = "IlayMarcianoTest"
        password = "IlayTest95"
        selected_products = set()
        for i in range(2):
            self.add_random_product_to_cart(randint(2,10),True,selected_products)
            self.toolbar.toolbar_logo_click()
        self.toolbar.toolbar_cart_click()
        self.cart_popup.go_to_checkout()
        self.login_page.login_input_sendkeys(username)
        self.login_page.password_input_sendkeys(password)
        self.login_page.log_in_button()
        self.cart_page.checkout()
        self.checkout.click_billing_address()
        self.checkout.click_shipping_address()
        self.checkout.confirm_shipping_method()
        self.checkout.confirm_payment_method()
        self.checkout.agree_to_terms()
        self.checkout.confirm_checkout()
        order_number = self.checkout.get_order_number().text
        self.checkout.go_to_order_details()
        self.assertEqual(order_number,self.checkout.get_completed_order_number())
        self.toolbar.toolbar_cart_click()
        self.assertEqual(self.cart_popup.cart_total_items_amount(),'0')
        logging.info("Test test_complete_order completed successfully.")

    def test_login_logout(self):
        """
        Logs into the website and verifies that the login was successful.
        Logs out of the website and confirms that the logout was completed correctly.
        """
        # Define login credentials
        username = "IlayMarcianoTest"
        password = "IlayTest95"
        self.toolbar.toolbar_login_click()
        self.login_page.login_input_sendkeys(username)
        self.login_page.password_input_sendkeys(password)
        self.login_page.log_in_button()
        self.assertEqual(self.toolbar.toolbar_account_name().text.lower(), username.lower())
        self.toolbar.toolbar_account_click()
        self.toolbar.toolbar_logout()
        self.assertEqual(self.toolbar.toolbar_account_name().text.lower(), "Log in".lower())
        logging.info("Test test_login_logout completed successfully.")

    # Helper functions
    def add_random_product_to_cart(self, quantity, mouse_click=False, selected_products=None):
        """
        Adds a random product from a random category to the shopping cart
        with a random quantity, ensuring no duplicate selections.
        """

        if selected_products is None:
            selected_products = set()  # Initialize set if not provided
        while True:
            # Choose a random category and click it
            category_name = choice(self.main_page.categories()).text
            # The gift cards products cannot be added without extra information given
            while "Gift" in category_name:
                category_name = choice(self.main_page.categories()).text
            self.main_page.click_category(category_name)
            # Scroll down slightly on the category page
            self.driver.execute_script("window.scrollBy(0, 350);")
            # Get available products and remove already selected ones
            products = [p.text for p in self.category_page.product()]
            available_products = list(set(products) - selected_products)
            if not available_products:
                self.toolbar.toolbar_logo_click()
                continue
            product = choice(available_products)  # Pick a unique product
            selected_products.add(product)  # Track selected product
            self.category_page.click_product(product)
            self.driver.execute_script("window.scrollBy(0, 200);")
            # The converse all star shoes product cannot be added without choosing a color
            if 'Converse' in product:
                self.product_page.choose_color()
            self.product_page.change_quantity(quantity)
            # Simulate clicking outside the input area to update the price - Product name
            self.product_page.get_product_name().click()
            self.product_page.add_to_cart()
            if mouse_click:
                self.remove_cart_blocker()
            break

    def remove_cart_blocker(self):
        """
        Removes the cart blocker overlay using JavaScript.
        """
        self.driver.execute_script("""
            var blocker = document.querySelector('.canvas-blocker.canvas-slidable');
            if (blocker) blocker.remove();
        """)

    def clean_cart(self):
        """Cleans the cart from the cart popup on the right side of the screen"""
        while True:
            try:
                cart_items = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "btn-to-danger"))
                )
                if not cart_items:
                    break
                cart_items[0].click()
                WebDriverWait(self.driver, 1).until(
                    EC.staleness_of(cart_items[0])
                )
            except:
                break

    def remove_first_cart_item(self):
        """
        Removes the first item added to the cart, which appears last in the cart list.
        """
        try:
            # Wait for the cart items to load
            cart_items = WebDriverWait(self.driver, 2).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "offcanvas-cart-item"))
            )

            if cart_items:
                # Select the last item in the cart, since the first added product is last in the list
                last_item = cart_items[-1]
                remove_button = last_item.find_element(By.CLASS_NAME, "btn-to-danger")
                remove_button.click()
                # Wait until the last item is removed from the cart
                WebDriverWait(self.driver, 2).until(EC.staleness_of(last_item))
        except Exception as e:
            print(f"Error removing the first added cart item: {e}")

    def tearDown(self):
        """Clean up after the test."""
        # Wait for 2 seconds before closing the browser
        sleep(1)
        self.driver.quit()
