import json
from pathlib import Path


def load_inventory():
    file_path = Path("inventory.json")

    if file_path.exists():
        print("inventory.json found.")

        with open(file_path, "r") as f:
            inventory = json.load(f)

        print("Inventory loaded successfully.")
        return inventory

    print("inventory.json not found. Starting with an empty inventory.")
    return []


def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

    print("Inventory saved successfully to inventory.json.")


def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip()
    product_name = input("Product Name: ").strip()

    if not product_id or not product_name:
        print("Product ID and name cannot be empty.")
        return

    if any(product["id"] == product_id for product in inventory):
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

    product = {
        "id": product_id,
        "name": product_name,
        "price": product_price,
        "quantity": product_quantity
    }

    inventory.append(product)

    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['quantity']}")

            try:
                new_quantity = int(input("New Stock Quantity: "))
            except ValueError:
                print("Stock quantity must be an integer.")
                return

            if new_quantity < 0:
                print("Stock quantity cannot be negative.")
                return

            product["quantity"] = new_quantity

            print("Stock updated successfully!")
            return

    print("Product not found.")


def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("------------------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['quantity']}")
            print("------------------------------------------------")
            return

    print("Product not found.")


def display_all(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory")
    print("------------------------------------------------")

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['quantity']}"
        )

    print("------------------------------------------------")


def main():
    inventory = load_inventory()

    if not inventory:
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
            display_all(inventory)

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