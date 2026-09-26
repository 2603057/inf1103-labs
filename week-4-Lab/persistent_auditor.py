from pathlib import Path

def load_inventory():
    try:
        file_path = Path(__file__).parent / "inventory.txt"

        with open(file_path, "r") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("Inventory file not found. Starting with 0 inventory.")
        return 0

    except ValueError:
        print("Invalid data in inventory file. Starting with 0 inventory.")
        return 0


inventory = load_inventory()