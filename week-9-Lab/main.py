
import json
from pathlib import Path

from product import Product
from inventory import Inventory


def load_inventory():
    file_path = Path("inventory.json")
    inventory = Inventory()

    if file_path.exists():
        print("inventory.json found.")

        try:
            with open(file_path, "r") as f:
                products = json.load(f)

            for product_data in products:
                product = Product(
                    product_data["id"],
                    product_data["name"],
                    product_data["price"],
                    product_data["quantity"]
                )

                inventory.add_product(product)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Error loading inventory.json.")

    else:
        print("inventory.json not found. Starting with an empty inventory.")

    return inventory


def save_inventory(inventory):
    products = []

    for product in inventory.get_products():
        product_data = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "quantity": product.get_stock()
        }

        products.append(product_data)

    with open("inventory.json", "w") as f:
        json.dump(products, f, indent=4)

    print("Inventory saved successfully to inventory.json.")


def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip()
    product_name = input("Product Name: ").strip()

    if not product_id or not product_name:
        print("Product ID and name cannot be empty.")
        return

    if inventory.search_product(product_id):
        print(f"Product ID '{product_id}' already exists.")
        return

    try:
        product_price = float(input("Price: "))
        product_quantity = int(input("Stock Quantity: "))
    except ValueError:
        print("Price must be a number and stock quantity must be an integer.")
        return

    if product_price < 0 or product_quantity < 0:
        print("Price and quantity must be non-negative.")
        return

    product = Product(
        product_id,
        product_name,
        product_price,
        product_quantity
    )

    inventory.add_product(product)


def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")

    try:
        new_quantity = int(input("New Stock Quantity: "))
    except ValueError:
        print("Stock quantity must be an integer.")
        return

    if new_quantity < 0:
        print("Stock quantity cannot be negative.")
        return

    product.update_stock(new_quantity)


def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")


def main():
    inventory = load_inventory()

    if not inventory.get_products():
        print("Inventory is empty. Please add products to the inventory.")

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)

        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
