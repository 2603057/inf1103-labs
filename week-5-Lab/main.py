import json
from pathlib import Path


def load_inventory():
    file_path = Path("inventory.json")

    if file_path.exists():
        with open(file_path, "r") as f:
            inventory = json.load(f)

        print("Inventory loaded successfully.")
        return inventory

    print("inventory.json not found. Starting with an empty inventory.")
    return []


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
        print("Inventory is empty.")

    display_all(inventory)


if __name__ == "__main__":
    main()