
from order import Order
from supplier import Supplier
from physicalProduct import PhysicalProduct
from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount
)

# Create supplier and product
supplier = Supplier("S001", "Dell", "dell@email.com")

product = PhysicalProduct(
    "P001",
    "Desk Lamp",
    25.00,
    10,
    1.5,
    supplier
)

# Create order with 10 lamps ($250)
order = Order("O001")
order.add_order_line(product, 10)

# TEST 1: No discount
print("TEST 1: No Discount")
print("Expected: 250.0")
print("Actual:", order.get_total())

assert order.get_total() == 250.0

# TEST 2: Bulk discount
print("\nTEST 2: Bulk Discount")

order.set_discount(BulkDiscount(200, 20))

print("Expected: 230.0")
print("Actual:", order.get_total())

assert order.get_total() == 230.0

# TEST 3: Change to percentage discount
print("\nTEST 3: Percentage Discount")

order.set_discount(PercentageDiscount(10))

print("Expected: 225.0")
print("Actual:", order.get_total())

assert order.get_total() == 225.0

print("\nALL TESTS PASSED!")
