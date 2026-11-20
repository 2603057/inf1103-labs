from supplier import Supplier
from physicalProduct import PhysicalProduct

supplier = Supplier("S001", "Dell", "dell@email.com")

# Valid product
product = PhysicalProduct(
    "P001", "Desk Lamp", 25.00, 10, 1.5, supplier
)
print("Valid product: PASSED")

# Invalid price
try:
    PhysicalProduct("P002", "Lamp", 0, 10, 1.5, supplier)
except ValueError:
    print("Invalid price: PASSED")

# Invalid stock
try:
    PhysicalProduct("P003", "Lamp", 25, -5, 1.5, supplier)
except ValueError:
    print("Invalid stock: PASSED")

# Invalid stock update
try:
    product.update_stock(-10)
except ValueError:
    print("Invalid stock update: PASSED")