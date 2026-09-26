def get_valid_input():
    while True:
        user_input = input("Enter the amount (or 'quit' to stop): ")

        if user_input.lower() == 'quit':
            return "quit"

        try:
            amount = int(user_input)

            if amount <= 0:
                print("Amount must be greater than 0.")
                return None

            return amount

        except ValueError:
            print("Invalid input. Please enter a valid amount in numbers.")
            return None


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts, total_tax):
    print("Total Deliveries Processed:", total_units)
    print("Number of failed entries:", failed_attempts)
    print("Total Tax:", total_tax)


def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            total = int(lines[0].split("=")[1].strip())

            history_text = lines[1].split("=")[1].strip()
            history_text = history_text.strip("[]")

            history = []

            if history_text:
                values = history_text.split(",")

                for value in values:
                    history.append(int(value.strip()))

            return total, history

    except FileNotFoundError:
        print("Inventory file not found. Starting with 0 inventory.")
        return 0, []

    except ValueError:
        print("Invalid data in inventory file. Starting with 0 inventory.")
        return 0, []


def save_inventory(total, history):
    with open("inventory.txt", "w") as file:
        file.write("Total = " + str(total) + "\n")
        file.write("History = " + str(history) + "\n")


# Main program

deliveries_processed = 0
failedentries = 0
total_tax = 0

inventorynumber, transaction_history = load_inventory()

print("Loaded inventory:", inventorynumber)
print("Transaction history:", transaction_history)

while True:

    amount = get_valid_input()

    if amount == "quit":
        break

    if amount is None:
        failedentries += 1
        continue

    inventorynumber = process_delivery(inventorynumber, amount)

    transaction_history.append(amount)

    tax = calculate_tax(amount)
    total_tax += tax

    deliveries_processed += 1

    print("Delivery amount:", amount)
    print("Tax for this delivery:", tax)
    print("Total tax so far:", total_tax)
    print("Current total inventory:", inventorynumber)


# Save inventory and transaction history
save_inventory(inventorynumber, transaction_history)

# Final report
generate_report(deliveries_processed, failedentries, total_tax)