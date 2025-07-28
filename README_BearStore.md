
# 🧪 BearStore Automation Testing Suite

This project is a comprehensive **QA Automation** test suite for the [BearStore test site](https://bearstore-testsite.smartbear.com), built using **Python** and **Selenium**. It simulates real-world user interactions such as browsing, adding products to the cart, validating prices, completing orders, and more — with a strong focus on **randomization** and **realistic edge cases**.

---

## 🔧 Technologies Used

- **Language**: Python 3
- **Framework**: `unittest`
- **Browser Driver**: Microsoft Edge (can be configured for others)
- **Automation Tools**: Selenium WebDriver
- **Design Patterns**: Page Object Model (POM)
- **Logging**: Python built-in `logging` module
- **Assertions**: Built-in `unittest.TestCase`

---

## ✅ Test Coverage

| Test Name                      | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `test_page_transitions`       | Navigates between homepage, category, and product pages, and verifies titles. |
| `test_add_to_cart`            | Adds random products to cart and checks total quantity.                     |
| `test_add_to_cart_3`          | Adds 3 unique products and verifies names, prices, and quantities.          |
| `test_add_to_cart_and_remove` | Adds 2 products, removes one, and checks the remaining item is accurate.    |
| `test_cart_transitions`       | Verifies cart behavior and transitions from popup to cart page.             |
| `test_3_products_details`     | Validates price × quantity = subtotal, across cart popup and full cart.     |
| `test_changes_in_2_products`  | Updates product quantities in cart and confirms subtotal and total price.   |
| `test_complete_order`         | Full order cycle: add to cart → login → checkout → verify order.            |
| `test_login_logout`           | Verifies login and logout flow for a test user.                             |

---

## 🧠 Key Features

- 🔁 **Randomized test data** – Categories, products, and quantities selected randomly to simulate user variability.
- 🧩 **No duplicate products** – Tests ensure that the same product isn't added more than once in multi-product flows.
- 🧮 **Full price calculation validation** – Verifies subtotal/total prices, unit price × quantity consistency.
- 🔐 **Login/Logout handling** – Includes test user authentication before checkout.
- 🛒 **Complete checkout flow** – From cart to order confirmation with validation of order number and cart reset.
- 🔧 **Helper utilities** – Dynamic DOM interaction (JS execution), overlays removal, and data extraction.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Edge WebDriver (or modify for Chrome/Firefox)
- Install dependencies:
```bash
pip install selenium
```

### Running the Tests

```bash
python -m unittest test_smartbear.py
```

---

## 📁 Project Structure

```
pythonProject/
├── Smart_Bear_Classes/        # Page Object Model classes
│   ├── smartbear_main_page.py
│   ├── smartbear_product_page.py
│   ├── smartbear_cart_page.py
│   └── ...etc
├── test_smartbear.py          # Main test suite
└── README.md                  # This file
```

---

## 👤 Test User Credentials

```
Username: IlayMarcianoTest
Password: IlayTest95
```

---

## 📸 Screenshots & Reports

To enable screenshots or HTML reports, consider integrating tools like:
- `HTMLTestRunner`
- `pytest + allure` (for future upgrades)

---

## 📌 Notes

- This project is ideal for demonstrating **real-world automation capabilities** in e-commerce flows.
- Designed with **extensibility** and **maintainability** in mind using POM.

---

## 🤝 Author

**Ilay Marciano**  
📧 ilay.marciano95@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ilay-marciano-421860223)  
💻 [GitHub](https://github.com/ilaymar95)

---
