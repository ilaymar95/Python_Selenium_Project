
# 🧪 BearStore Automation Project – Python + Selenium

This project is a full-featured automation test suite for the BearStore e-commerce demo site. It uses Python and Selenium, follows the Page Object Model (POM) pattern, and includes 9 smart test cases that simulate realistic user behaviors.

---

## 🚀 Project Overview

- Automated UI testing for BearStore's product, cart, login, and checkout flows.
- Randomized product selection for each run to simulate diverse user behavior.
- Full test coverage including price validation, quantity updates, and order confirmation.

---

## 📁 Folder Structure

```
Python_Selenium_Project/
├── Smart_Bear_Classes/     # Page Object Model (POM) classes
│   ├── BearStoreMainPage.py
│   ├── ProductPage.py
│   ├── CartPage.py
│   ├── CartPopUp.py
│   ├── LoginPage.py
│   ├── Checkout.py
│   └── ToolBar.py
├── tests/
│   └── test_smartbear.py   # Main test suite with 9 automated test cases
├── README.md
```

---

## 🧩 Page Object Model Classes

- `BearStoreMainPage.py` – Handles home page and category elements
- `CategoryPage.py` – Product listings per category
- `ProductPage.py` – Product details, quantity changes, and add to cart
- `CartPopUp.py` – Right-side cart popup validation
- `CartPage.py` – Full cart screen: totals, edits, and clearing
- `LoginPage.py` – Login fields and button interaction
- `Checkout.py` – Order flow: billing, shipping, confirmation
- `ToolBar.py` – Top navigation bar: cart icon, login, logo

📁 [View Classes Folder](./Smart_Bear_Classes)

---

## 🧪 Test Scenarios

Located in `test_smartbear.py`, the test suite includes:

1. **Page Transitions** – Navigation between category and product pages
2. **Add to Cart** – Adding products with quantity and validating totals
3. **Cart Details** – Validating prices × quantities = subtotal
4. **Cart + Remove Item** – Ensures accurate removal
5. **Cart Transition Flow** – Popup to full cart page
6. **Three Product Validation** – Full comparison of names, prices, and totals
7. **Update Quantities** – Changing quantities and recalculating totals
8. **Full Checkout** – Logging in and completing an order
9. **Login/Logout** – Full auth flow with state verification

---

## ▶️ Running the Tests

```bash
pip install selenium
python -m unittest tests/test_smartbear.py
```

Edge driver must be installed and accessible from PATH, or you can configure Chrome instead.

---

## 👨‍💻 Author

Ilay Marciano  
📧 ilay.marciano95@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ilay-marciano-421860223)  
💻 [GitHub](https://github.com/ilaymar95)

---

# 🧪 פרויקט אוטומציה BearStore – פייתון וסלניום

זהו פרויקט בדיקות אוטומטיות מלא עבור אתר ההדגמה BearStore.  
הבדיקות כתובות בפייתון ומבוססות על Selenium ומבנה Page Object Model (POM).

---

## 🚀 סקירה כללית

- בדיקות UI מקצה לקצה: קטגוריות, מוצרים, עגלת קניות, התחברות והזמנה.
- בחירת מוצרים אקראית בכל הרצה.
- כיסוי מלא של ולידציית מחירים, כמויות, והזמנה מלאה.

---

## 📁 מבנה תיקיות

```
Python_Selenium_Project/
├── Smart_Bear_Classes/     # מחלקות Page Object
├── tests/
│   └── test_smartbear.py   # קובץ הבדיקות הראשי
├── README.md
```

---

## 🧩 מחלקות (Page Object)

- `BearStoreMainPage.py` – עמוד הבית והקטגוריות
- `CategoryPage.py` – עמוד מוצרים בקטגוריה
- `ProductPage.py` – עמוד מוצר
- `CartPopUp.py` – עגלת הקניות הצפה
- `CartPage.py` – עמוד עגלת קניות מלאה
- `LoginPage.py` – התחברות
- `Checkout.py` – תהליך תשלום והזמנה
- `ToolBar.py` – סרגל ניווט עליון

📁 [לצפייה בתיקיית המחלקות](./Smart_Bear_Classes)

---

## 🧪 תרחישי בדיקה עיקריים

מופיעים בקובץ `test_smartbear.py`:

1. ניווט בין עמודים
2. הוספת מוצרים לעגלה
3. בדיקת סכום ביניים (מחיר × כמות)
4. הסרת פריט מהעגלה
5. ניווט מהפופאפ לעגלה מלאה
6. ולידציית 3 מוצרים (שמות, כמויות, מחירים)
7. שינוי כמויות ועדכון מחירים
8. ביצוע הזמנה מלאה עם התחברות
9. התחברות וניתוק משתמש

---

## ▶️ הרצת הבדיקות

```bash
pip install selenium
python -m unittest tests/test_smartbear.py
```

יש לוודא ש־EdgeDriver מותקן או להחליף ל־ChromeDriver.

---

## 👨‍💻 מחבר הפרויקט

אילאי מרציאנו  
📧 ilay.marciano95@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ilay-marciano-421860223)  
💻 [GitHub](https://github.com/ilaymar95)
