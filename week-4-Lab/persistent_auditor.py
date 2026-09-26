def load_inventory():
    try:
       with open("inventory.txt", "r") as file:
        for line in file:
            print(line.strip())
        
    except FileNotFoundError:
            print("Inventory file not found. Starting with 0 inventory.")
            return 0, []
    
    except ValueError:
            print("Invalid data in inventory file. Starting with 0 inventory.")
            return 0, []

load_inventory()
