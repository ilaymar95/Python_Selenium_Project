
## 🧩 Project Structure & Page Object Model

This project uses the **Page Object Model (POM)** design pattern for better maintainability and reusability.

### 📁 Smart_Bear_Classes

- `BearStoreMainPage.py` – Interactions with the home page and categories
- `CategoryPage.py` – Product listing, filters, and selections by category
- `ProductPage.py` – Product detail, quantity selection, and add to cart
- `CartPopUp.py` – Cart popup actions and validations
- `CartPage.py` – Full cart view, subtotal calculations, and updates
- `Checkout.py` – Complete checkout flow, billing/shipping steps
- `LoginPage.py` – User login fields and flow
- `ToolBar.py` – Navigation bar (cart icon, login/logout, site logo, etc.)

These classes are reused across the 9 automated test scenarios to keep the code clean and modular.

📁 [View Source Folder](./Smart_Bear_Classes)
