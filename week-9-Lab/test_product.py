
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct


# Create a physical product
guitar = PhysicalProduct("P001", "Guitar", 500, 10, 4.5)

# Create a digital product
windows = DigitalProduct("D001", "Windows OS", 199, 50, 5000)


# Display physical product
print("\nPhysical Product")
guitar.display_information()

# Display digital product
print("\nDigital Product")
windows.display_information()
