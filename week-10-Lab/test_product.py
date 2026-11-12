
from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from main import save_inventory, load_inventory
from supplier import Supplier

supplier = Supplier("S001", "Guitar World", "Test@gmail.com")
product1 = PhysicalProduct("P001", "Guitar", 499.99, 10, 2.5, supplier)
product2 = DigitalProduct("P002", "Guitar Lessons", 29.99, 100, "https://example.com/guitar-lessons", supplier)

name = product1.get_supplier()
name2 =product2.get_supplier()

print(name.name)
print(name2.name)
