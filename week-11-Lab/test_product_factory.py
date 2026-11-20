import unittest

from product_factory import ProductFactory
from supplier import Supplier
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct


class TestProductFactory(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Dell", "dell@email.com"
        )

    def test_create_physical_product(self):
        product = ProductFactory.create(
            "physical",
            "P001",
            "Desk Lamp",
            25.00,
            10,
            self.supplier,
            weight=1.5
        )

        self.assertIsInstance(product, PhysicalProduct)

    def test_create_digital_product(self):
        product = ProductFactory.create(
            "digital",
            "D001",
            "Photo Editor",
            49.90,
            100,
            self.supplier,
            download_size=500
        )

        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_product_type(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "service",
                "S001",
                "Installation",
                30.00,
                5,
                self.supplier
            )


if __name__ == "__main__":
    unittest.main()