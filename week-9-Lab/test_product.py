from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct

guitar = PhysicalProduct("P001", "Guitar", 500, 10, 4.5)
windows = DigitalProduct("D001", "Windows OS", 199, 50, 5000)

print("\nPhysical Product:")
guitar.display_information()

print("\nShipping Cost:")
print(guitar.calculate_shipping_cost())

print("\nShipping Details:")
print(guitar.get_shipping_details())

print("\nDigital Product:")
windows.display_information()