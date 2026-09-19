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

inventorynumber = 0
failedentries = 0

while True:
    amount = get_valid_input()
    if amount == "quit":
        break
    if amount is None:
        failedentries += 1
        continue
    inventorynumber += amount  
    print("Current inventory number:", inventorynumber) 
