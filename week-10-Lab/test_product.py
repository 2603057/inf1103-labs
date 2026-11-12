
from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from main import save_inventory, load_inventory
from supplier import Supplier
from order import Order
from orderline import OrderLine

# Create one Product
product1 = PhysicalProduct("P001", "Laptop", 1500, 10, 2.5, "Dell")

# Create two Orders
order1 = Order("O001")
order2 = Order("O002")

# Add the SAME Product to both Orders
order1.add_order_line(product1, 2)
order2.add_order_line(product1, 3)

# Display both Orders
print("ORDER 1:")
order1.display_order()

print("\nORDER 2:")
order2.display_order()

# Compare object identities
order1_line = order1.get_order_lines()[0]
order2_line = order2.get_order_lines()[0]

print("\nOBJECT IDENTITY TEST")

print("Same OrderLine object:",
      order1_line is order2_line)

print("Same Product object:",
      order1_line.product is order2_line.product)

# Remove OrderLine from Order 1
print("\nREMOVING ORDER LINE FROM ORDER 1")
order1.remove_order_line("P001")

# Check Order 2 is unaffected
print("\nORDER 2 AFTER REMOVAL:")
order2.display_order()

# Check Product still exists
print("\nPRODUCT STILL EXISTS:")
product1.display_information()
