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
    inventory = [
        {
            "id": "P001",
            "name": "Laptop",
            "price": 1200.00,
            "quantity": 15
        },
        {
            "id": "P002",
            "name": "Mouse",
            "price": 25.50,
            "quantity": 40
        },
        {
            "id": "P003",
            "name": "Keyboard",
            "price": 45.00,
            "quantity": 25
        }
    ]

    display_all(inventory)


if __name__ == "__main__":
    main()