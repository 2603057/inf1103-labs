inventory = []
inventory.clear()
inventorynumber = 0
failedentries = 0

quit = False
while quit == False:
  try:
    amount = int(input("Enter the amount: "))
    if amount <= 0:
          print("Amount must be greater than 0.")
          failedentries += 1
          continue
    itemname = input("Enter the item name: ")
    if not itemname:
          print("Item name cannot be empty.")
          failedentries += 1
          continue
    item = (amount, itemname)
    inventory.append(item)
    inventorynumber += amount
    if inventorynumber > 500:
      print("Inventory limit exceeded. Must be less than 500 items total")
      quit = True
    else:
        print("Current Inventory Number is:", inventorynumber)
        wantquit = input("Do you want to quit? (quit, any key to continue): ").lower()
        if wantquit == "quit":
            quit = True
            print("Inventory List:", inventory)
            print("Total number of items in inventory:", inventorynumber)
            print("Number of failed entries:", failedentries)
        else:
           continue
  except ValueError:
    print("Invalid input. Please enter a valid amount in numbers.")
    failedentries += 1
    continue