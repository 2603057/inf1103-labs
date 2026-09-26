from pathlib import Path

def load_inventory():
    inventory = []

    try:
        file_path = Path(__file__).parent / "inventory.txt"

        with open(file_path, "r") as file:
            for line in file:
                inventory.append(line.strip())

        return inventory

    except FileNotFoundError:
        print("Inventory file not found. Starting with 0 inventory.")
        return 0

    except ValueError:
        print("Invalid data in inventory file. Starting with 0 inventory.")
        return 0

def get_order_input():
    while True:
        product_name = input("Enter product name: ").strip()

        if product_name == "":
            print("Product bane cannot be empty. Please try again.")
        else:
            break 

    while True:
        quantity_input =input("Enter quantity: ").strip()
        try:
            quantity = int(quantity_input)

            if quantity <= 0:
                print("Quality must be greater thern 0. Please try again.")
            else:
                break 

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")

    return product_name, quantity

inventory = load_inventory()

for item in inventory:
    print(item)
product_name = input("Enter product name:")
quantity = input("Enter quantity: ")

product_name, quantity = get_order_input()

if inventory:
    last_item = inventory[-1]
    last_id = int(last_item.split(",")[0])
    new_id = last_id + 1
else:
    new_id = 1001



new_order = f"{new_id}, {product_name}, {quantity}"
inventory.append(new_order)

print("New order added!")
print(new_order)