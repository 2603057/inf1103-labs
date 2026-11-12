
from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from supplier import Supplier
from inventory import Inventory
from order import Order


print("=" * 60)
print("TASK 9: TESTING AND REVIEW")
print("=" * 60)


# --------------------------------------------------
# 1. SUPPLIER AND PRODUCT ASSOCIATION
# --------------------------------------------------

print("\nTEST 1: Supplier and Product Association")

supplier = Supplier("S001", "Dell", "dell@email.com")

physical = PhysicalProduct(
    "P001", "Laptop", 1500.0, 10, 2.5, supplier
)

digital = DigitalProduct(
    "P002", "Software", 50.0, 100, 500, supplier
)

print("Product stores correct Supplier:",
      physical.get_supplier() is supplier)

print("Supplier exists independently:")
supplier.display_information()


# --------------------------------------------------
# 2. INVENTORY AGGREGATION
# --------------------------------------------------

print("\nTEST 2: Inventory Aggregation")

inventory1 = Inventory()
inventory2 = Inventory()

inventory1.add_product(physical)

print("Product found in Inventory 1:",
      inventory1.find_product("P001") is physical)

# Remove product from first inventory
inventory1.remove_product("P001")

# Add same product to second inventory
inventory2.add_product(physical)

print("Product found in Inventory 2:",
      inventory2.find_product("P001") is physical)

print("Same Product object preserved:",
      inventory2.find_product("P001") is physical)


# --------------------------------------------------
# 3. ORDER AND ORDERLINE COMPOSITION
# --------------------------------------------------

print("\nTEST 3: Order and OrderLine Composition")

order = Order("O001")

# Order creates its own OrderLine objects
order.add_order_line(physical, 2)
order.add_order_line(digital, 3)

order_lines = order.get_order_lines()

print("Order created OrderLine objects:",
      len(order_lines) == 2)

# OrderLine references the original Product
print("OrderLine references original Product:",
      order_lines[0].product is physical)

# Remove an OrderLine
order.remove_order_line("P001")

print("Product still exists after OrderLine removal:",
      physical.get_name())


# --------------------------------------------------
# 4. ORDER TOTAL CALCULATION
# --------------------------------------------------

print("\nTEST 4: Order Total Calculation")

# Create a new order for total calculation
order2 = Order("O002")

order2.add_order_line(physical, 2)
order2.add_order_line(digital, 3)

expected_total = (1500.0 * 2) + (50.0 * 3)

actual_total = order2.get_total()

print(f"Expected total: ${expected_total:.2f}")
print(f"Actual total:   ${actual_total:.2f}")

print("Order total correct:",
      actual_total == expected_total)

order2.display_order()


# --------------------------------------------------
# 5. POLYMORPHISM THROUGH PRODUCT
# --------------------------------------------------

print("\nTEST 5: Polymorphism")


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


inventory3 = Inventory()

inventory3.add_product(physical)
inventory3.add_product(digital)

print("\nDisplaying products through Product references:")

for item in inventory3.get_products():
    show_product_details(item)
    print("-" * 40)


# --------------------------------------------------
# 6. CHECK SUBCLASS FULFILMENT INFORMATION
# --------------------------------------------------

print("\nTEST 6: Subclass Behaviour")

print("Physical fulfilment:",
      physical.get_fulfilment_info())

print("Digital fulfilment:",
      digital.get_fulfilment_info())

print("Physical shipping cost:",
      physical.calculate_shipping_cost())

print("Physical shipping details:",
      physical.get_shipping_details())


# --------------------------------------------------
# 7. CHECK PRODUCT AND SUPPLIER INDEPENDENCE
# --------------------------------------------------

print("\nTEST 7: Object Independence")

another_supplier = Supplier(
    "S002", "Microsoft", "microsoft@email.com"
)

another_product = DigitalProduct(
    "P003", "Office Software", 80.0, 50, 1000,
    another_supplier
)

print("Original Supplier:",
      physical.get_supplier().name)

print("Another Supplier:",
      another_product.get_supplier().name)

print("Products have different suppliers:",
      physical.get_supplier() is not another_product.get_supplier())


# --------------------------------------------------
# 8. FINAL INVENTORY DISPLAY
# --------------------------------------------------

print("\nTEST 8: Inventory Display")

inventory3.display_all()


# --------------------------------------------------
# END
# --------------------------------------------------

print("\n" + "=" * 60)
print("ALL TASK 9 TESTS COMPLETED")
print("=" * 60)
