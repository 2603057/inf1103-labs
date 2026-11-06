
from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from main import save_inventory, load_inventory


print("========== STEP 7: TESTING ==========")


# 1. Test PhysicalProduct
print("\n1. Testing PhysicalProduct")

guitar = PhysicalProduct("P001", "Guitar", 500, 10, 4.5)

guitar.display_information()
print("Weight:", guitar.get_weight(), "kg")


# 2. Test DigitalProduct
print("\n2. Testing DigitalProduct")

windows = DigitalProduct("D001", "Windows OS", 199, 50, 5000)

windows.display_information()
print("Download Size:", windows.get_download_size(), "MB")


# 3. Test get_fulfilment_info()
print("\n3. Testing Fulfilment Information")

print(guitar.get_fulfilment_info())
print(windows.get_fulfilment_info())


# 4. Test Abstract Product
print("\n4. Testing Abstract Product")

try:
    product = Product("T001", "Test Product", 100, 10)
except TypeError:
    print("PASS: Product cannot be instantiated directly.")


# 5. Test Shipping Functionality
print("\n5. Testing Shipping")

print("Can guitar be shipped?", isinstance(guitar, CanBeShipped))
print("Shipping Cost:", guitar.calculate_shipping_cost())
print("Shipping Details:", guitar.get_shipping_details())

print("Can Windows OS be shipped?",
      hasattr(windows, "calculate_shipping_cost"))


# 6. Test Inventory Operations
print("\n6. Testing Inventory")

inventory = Inventory()

inventory.add_product(guitar)
inventory.add_product(windows)

print("\nDisplaying All Products:")
inventory.display_all()

print("\nSearching for Guitar:")
result = inventory.search_product("P001")

if result:
    result.display_information()
else:
    print("Product not found.")

print("\nUpdating Guitar Stock:")
guitar.update_stock(20)
print("Updated Stock:", guitar.get_stock())


# 7. Test JSON Saving
print("\n7. Testing JSON Saving")

save_inventory(inventory)


# 8. Test JSON Loading
print("\n8. Testing JSON Loading")

loaded_inventory = load_inventory()

loaded_inventory.display_all()


# 9. Verify Correct Product Types
print("\n9. Verifying Product Types")

for product in loaded_inventory.get_products():
    print(type(product).__name__)

print("\n========== TESTING COMPLETED ==========")
