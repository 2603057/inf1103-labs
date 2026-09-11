inventory = []
inventory.clear()
inventorynumber = 0

quit = False
while quit == False:
  try:
    amount = int(input("Enter the amount: "))
    itemname = input("Enter the item name: ")
    item = (amount, itemname)
    inventory.append(item)
    inventorynumber += amount
    if inventorynumber > 500:
      print("Inventory limit exceeded.")
      quit = True
    else:
        wantquit = input("Do you want to quit? (y/n): ").lower()
        if wantquit == "y":
            quit = True
            print("Inventory List:", inventory)
        else:
           continue
  except ValueError:
    print("Invalid input. Please enter a valid amount in numbers.")
    continue