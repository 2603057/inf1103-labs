
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from inventory import Inventory
from product import Product


# Function that accepts any Product
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


# Create both product types
physical = PhysicalProduct("P001", "Laptop", 1500, 10, 2.5, "Dell") 
digital = DigitalProduct("D001", "E-book", 15, 100, 60, "Author")



# Add both to the SAME Inventory
inventory = Inventory()

inventory.add_product(physical)
inventory.add_product(digital)


# Display both products using ONE loop
for product in inventory.get_products():
    show_product_details(product)
    print("-------------------------")
