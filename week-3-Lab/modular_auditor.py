def get_valid_input():
    while True:
        user_input = input("Enter the amount ( or 'quit' to stop): ")

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

def process_delvery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

deliveries_processed = 0
inventorynumber = 0
failedentries = 0

while True:
    amount = get_valid_input()
    if amount == "quit":
        break
    if amount is None:
        failedentries += 1
        continue
    inventorynumber = process_delvery(inventorynumber, amount)

    tax = calculate_tax(amount)
    deliveries_processed += 1

    print("Delivery amount:", amount) 
    print("Tax for this delivery:", tax)
    print("Current total inventory:", inventorynumber)
    print("Total deliveries processed:", deliveries_processed)