
from product_factory import ProductFactory
from supplier import Supplier
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct


supplier = Supplier(
    "S001",
    "Dell",
    "dell@email.com"
)

# TEST 1: Create Physical Product
physical = ProductFactory.create(
    "physical",
    "P001",
    "Desk Lamp",
    25.00,
    10,
    supplier,
    weight=1.5
)

assert isinstance(physical, PhysicalProduct)
print("Physical product creation: PASSED")


# TEST 2: Create Digital Product
digital = ProductFactory.create(
    "digital",
    "D001",
    "Photo Editor",
    49.90,
    100,
    supplier,
    download_size=500
)

assert isinstance(digital, DigitalProduct)
print("Digital product creation: PASSED")


# TEST 3: Unknown Product Type
try:
    ProductFactory.create(
        "service",
        "S001",
        "Installation",
        30.00,
        5,
        supplier
    )

except ValueError as error:
    print("Unknown product type: PASSED")
    print(error)


print("\nALL FACTORY TESTS PASSED!")
