# main.py
from styles_data import styles

def show_all_styles():
    print("\nAvailable Styles:")
    for idx, style in enumerate(styles.keys(), start=1):
        print(f"{idx}. {style}")

def search_by_price(max_price):
    print(f"\nItems cheaper than ${max_price}:")
    found = False
    for style_name, categories in styles.items():
        for category, items in categories.items():
            if isinstance(items, list):
                for item in items:
                    price_val = float(item["price"].replace("$", ""))
                    if price_val <= max_price:
                        print(f"{style_name} - {category}: {item}")
                        found = True
            else:
                price_val = float(items["price"].replace("$", ""))
                if price_val <= max_price:
                    print(f"{style_name} - {category}: {items}")
                    found = True
    if not found:
        print("No items found in this price range.")

def select_style():
    show_all_styles()
    choice = input("\nSelect a style number: ")
    try:
        choice = int(choice)
        style_name = list(styles.keys())[choice - 1]
        return style_name
    except (ValueError, IndexError):
        print("Invalid selection.")
        return None

def select_category(style_name):
    print(f"\nCategories in {style_name}:")
    categories = styles[style_name]
    for idx, cat in enumerate(categories.keys(), start=1):
        print(f"{idx}. {cat}")
    choice = input("\nSelect a category number: ")
    try:
        choice = int(choice)
        category_name = list(categories.keys())[choice - 1]
        return category_name
    except (ValueError, IndexError):
        print("Invalid selection.")
        return None

def show_items(style_name, category_name):
    category_items = styles[style_name][category_name]
    print(f"\nItems in {style_name} - {category_name}:")
    if isinstance(category_items, list):
        for item in category_items:
            print(item)
    else:
        print(category_items)

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Search by price")
        print("2. Buy by style")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                max_price = float(input("Enter maximum price in $: "))
                search_by_price(max_price)
            except ValueError:
                print("Invalid price.")
        elif choice == "2":
            style_name = select_style()
            if style_name:
                category_name = select_category(style_name)
                if category_name:
                    show_items(style_name, category_name)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
