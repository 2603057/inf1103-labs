
import json
from pathlib import Path

import inventory
from product_factory import ProductFactory
from product import Product
from inventory import Inventory
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from supplier import Supplier


# ---------------- SUPPLIER FUNCTIONS ----------------

def load_suppliers():
    file_path = Path("suppliers.json")

    if not file_path.exists() or file_path.stat().st_size == 0:
        return []

    with open(file_path, "r") as file:
        suppliers_data = json.load(file)

    suppliers = []

    for data in suppliers_data:
        supplier = Supplier(
            data["supplier_id"],
            data["name"],
            data["contact_email"]
        )

        suppliers.append(supplier)

    return suppliers


def save_suppliers(suppliers):
    suppliers_data = []

    for supplier in suppliers:
        data = {
            "supplier_id": supplier.supplier_id,
            "name": supplier.name,
            "contact_email": supplier.contact_email
        }

        suppliers_data.append(data)

    with open("suppliers.json", "w") as file:
        json.dump(suppliers_data, file, indent=4)

    print("Suppliers saved successfully!")


def create_supplier():
    print("\nEnter Supplier Details")

    supplier_id = input("Enter Supplier ID: ").strip()
    supplier_name = input("Enter Supplier Name: ").strip()
    contact_email = input("Enter Supplier Email: ").strip()

    return Supplier(supplier_id, supplier_name, contact_email)


def select_supplier(suppliers):
    print("\nChoose Supplier")

    for index, supplier in enumerate(suppliers, start=1):
        print(f"{index}. {supplier.name}")

    print(f"{len(suppliers) + 1}. Add New Supplier")

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Invalid supplier choice.")
        return None

    choice = int(choice)

    if 1 <= choice <= len(suppliers):
        return suppliers[choice - 1]

    elif choice == len(suppliers) + 1:
        supplier = create_supplier()

        for existing in suppliers:
            if existing.supplier_id == supplier.supplier_id:
                print("Supplier ID already exists.")
                return None

        suppliers.append(supplier)
        save_suppliers(suppliers)

        return supplier

    print("Invalid supplier choice.")
    return None


# ---------------- INVENTORY FUNCTIONS ----------------

def load_inventory(suppliers):
    inventory = Inventory()

    file_path = Path("inventory.json")

    if not file_path.exists() or file_path.stat().st_size == 0:
        return inventory

    with open(file_path, "r") as file:
        products_data = json.load(file)

    suppliers_changed = False

    for data in products_data:
        product_type = data.get("type", "physical")
        supplier_data = data.get("supplier")

        supplier = None
        supplier_id = None

        # Get supplier ID from inventory.json
        if isinstance(supplier_data, dict):
            supplier_id = supplier_data.get("supplier_id")

        elif isinstance(supplier_data, str):
            supplier_id = supplier_data

        # Find existing supplier
        if supplier_id is not None:
            for existing_supplier in suppliers:
                if existing_supplier.supplier_id == supplier_id:
                    supplier = existing_supplier
                    break

        # Create supplier if it does not exist
        if supplier is None:
            if isinstance(supplier_data, dict) and "name" in supplier_data:
                supplier = Supplier(
                    supplier_id,
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )
            else:
                supplier = Supplier(
                    "UNKNOWN",
                    "Unknown",
                    "Unknown"
                )

            suppliers.append(supplier)
            suppliers_changed = True

        try:
            product = ProductFactory.create(
                product_type,
                data["product_id"],
                data["name"],
                data["price"],
                data["quantity"],
                supplier,
                weight=data.get("weight", 0),
                download_size=data.get("download_size", 0)
            )

            inventory.add_product(product)
        except ValueError as error:
            print(f"Error loading product {data.get('product_id')}: {error}")

    if suppliers_changed:
        save_suppliers(suppliers)

    return inventory


def save_inventory(inventory):
    products_data = []

    for product in inventory.get_products():

        supplier = product.get_supplier()

        data = {
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "quantity": product.get_stock(),

            # Store supplier ID while keeping supplier details separate
            "supplier": {
                "supplier_id": supplier.supplier_id
            }
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


# ---------------- PRODUCT FUNCTIONS ----------------

def add_product(inventory, suppliers):
    print("\nChoose Product Type")
    print("1. Physical Product")
    print("2. Digital Product")

    choice = input("Enter your choice: ")

    if choice not in ["1", "2"]:
        print("Invalid choice. Please select 1 or 2.")
        return

    product_id = input("Enter Product ID: ").strip()
    name = input("Enter Product Name: ").strip()

    try:
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock quantity.")
        return

    supplier = select_supplier(suppliers)

    if supplier is None:
        return

    if choice == "1":
        try:
            weight = float(input("Enter Product Weight (kg): "))
        except ValueError:
            print("Invalid weight.")
            return

        product = ProductFactory.create(
            "physical",
            product_id,
            name,
            price,
            quantity,
            supplier,
            weight=weight
        )
    else:
        try:
            download_size = float(input("Enter Download Size (MB): "))
        except ValueError:
            print("Invalid download size.")
            return

        product = ProductFactory.create(
            "digital",
            product_id,
            name,
            price,
            quantity,
            supplier,
            download_size=download_size
        )
    inventory.add_product(product)


def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(product_id)

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

    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")


# ---------------- MAIN PROGRAM ----------------

def main():
    # Load suppliers first
    suppliers = load_suppliers()

    # Load inventory using existing supplier objects
    inventory = load_inventory(suppliers)

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
            add_product(inventory, suppliers)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            print("Saving data...")
            save_inventory(inventory)
            save_suppliers(suppliers)

        elif choice == "6":
            print("\nSaving data before exit...")

            save_inventory(inventory)
            save_suppliers(suppliers)

            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
