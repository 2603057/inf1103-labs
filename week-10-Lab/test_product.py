
from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from main import save_inventory, load_inventory
from supplier import Supplier

supplier = Supplier("S001", "Guitar World", "Test@gmail.com")

supplier.display_information()


