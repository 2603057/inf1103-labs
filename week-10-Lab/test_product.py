
from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from main import save_inventory, load_inventory
from supplier import Supplier

# 1. Create a Product BEFORE creating an Inventory
product1 = PhysicalProduct("P001", "Laptop", 1500 , 10, 2.5, Supplier("S001", "Tech Supplies Inc.", "techsupplies@example.com"))

# 2. Create Inventory A
inventoryA = Inventory()

# 3. Add Product to Inventory A
inventoryA.add_product(product1)

# 4. Remove Product from Inventory A
inventoryA.remove_product("P001")

# 5. Check whether Product still exists
print("\nChecking Product after removal:")
product1.display_information()

# 6. Create Inventory B
inventoryB = Inventory()

# 7. Add the SAME Product object to Inventory B
inventoryB.add_product(product1)

# 8. Display Inventory B
inventoryB.display_all()

# 9. Remove Product from Inventory B
inventoryB.remove_product("P001")

# 10. Check Product still exists
print("\nChecking Product after removal from Inventory B:")
product1.display_information()
