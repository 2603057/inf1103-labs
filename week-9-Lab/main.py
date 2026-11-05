
import json
from pathlib import Path

from product import Product
from inventory import Inventory
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct



def load_inventory():
    inventory = Inventory()

    file_path = Path("inventory.json")

    if not file_path.exists() or file_path.stat().st_size == 0:
        return inventory

    with open(file_path, "r") as file:
        products_data = json.load(file)

    for data in products_data:
        product_type = data.get("type", "physical")

        if product_type == "physical":
            product = PhysicalProduct(
                data["product_id"],
                data["name"],
                data["price"],
                data["quantity"],
                data.get("weight", 0)
            )

        elif product_type == "digital":
            product = DigitalProduct(
                data["product_id"],
                data["name"],
                data["price"],
                data["quantity"],
                data.get("download_size", 0)
            )

        else:
            print(f"Unknown product type: {product_type}")
            continue

        inventory.add_product(product)

    return inventory



def save_inventory(inventory):
    products_data = []

    for product in inventory.get_products():

        data = {
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "quantity": product.get_stock()
        }

        if isinstance(product, PhysicalProduct):
            data["type"] = "physical"
            data["weight"] = product.get_weight()

        elif isinstance(product, DigitalProduct):
            data["type"] = "digital"
            data["download_size"] = product.get_download_size()

        products_data.append(data)

    with open("inventory.json", "w") as file:
        json.dump(products_data, file, indent=4)

    print("Inventory saved successfully!")




def add_product(inventory):
    print("\nChoose Product Type")
    print("1. Physical Product")
    print("2. Digital Product")

    choice = input("Enter your choice: ")

    if choice not in ["1", "2"]:
        print("Invalid choice. Please select 1 or 2.")
        return

    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Stock Quantity: "))

    if choice == "1":
        weight = float(input("Enter Product Weight (kg): "))

        product = PhysicalProduct(
            product_id, name, price, quantity, weight
        )

    elif choice == "2":
        download_size = float(input("Enter Download Size (MB): "))

        product = DigitalProduct(
            product_id, name, price, quantity, download_size
        )

    else:
        print("Invalid product type.")
        return

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
