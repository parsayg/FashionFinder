# 🛍 Fashion Styles & Shopping Menu

## 📌 Overview
This is a small Python project that simulates a **fashion store**.  
It contains:
- A complete dictionary of **styles** (Casual, Formal, Sport, Streetwear, Old Money, Classic, Bohemian, Minimalist, Vintage, Techwear).
- Each style includes **clothing items** like pants, shirts, shoes, jackets, and hats with different qualities, prices, and brands.
- A shopping menu where the user can:
  1. **Search items** by price (e.g., "less than $50").
  2. **Choose a style**.
  3. **Select the type of item** (pants, shirt, shoes, etc.) and view details.

---

## 📂 Project Structure
```
project/
│
├── styles_data.py   # Dictionary containing all styles and items
├── shop.py          # Main program with menu & search functionality
└── README.md        # This file
```

---

## ⚙ How It Works
1. **Load Data**  
   The `styles_data.py` file stores all style and item data in a Python dictionary.
   
2. **Main Menu**  
   The `shop.py` script displays:
   - **Search by price**  
   - **Choose style**  
   - **Select item type**  

3. **Search Function**  
   The user can search for all items **below a certain price** in USD.

4. **Selection Flow**  
   ```
   Main Menu → Choose Style → Choose Item Type → Show Items
   ```

---

## ▶ How to Run
1. **Download the project files**.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python shop.py
   ```
4. Follow the instructions in the terminal.

---

## 💡 Example Usage
```
=== Welcome to the Fashion Store ===
1. Search items by price
2. Choose style
Enter your choice: 1
Enter maximum price in USD: 50
Found items:
- Casual - Shirt - $24 - Zara
- Sport - Shoes - $30 - Nike
- Bohemian - Pants - $38 - Anthropologie
...
```

---

## 🚀 Features
✅ Multiple fashion styles with detailed info  
✅ Search items by price  
✅ Style-based item selection  
✅ Structured and reusable dictionary data  

