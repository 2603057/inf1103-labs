import unittest

from supplier import Supplier
from physicalProduct import PhysicalProduct
from orderline import OrderLine


class TestProductValidation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Dell", "dell@email.com"
        )

    def test_valid_product(self):
        product = PhysicalProduct(
            "P001", "Desk Lamp", 25.00, 10, 1.5, self.supplier
        )
        self.assertEqual(product.get_price(), 25.00)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P002", "Lamp", 0, 10, 1.5, self.supplier
            )

    def test_negative_stock(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P003", "Lamp", 25, -5, 1.5, self.supplier
            )

    def test_invalid_stock_update(self):
        product = PhysicalProduct(
            "P004", "Lamp", 25, 10, 1.5, self.supplier
        )

        with self.assertRaises(ValueError):
            product.update_stock(-10)

    def test_valid_order_quantity(self):
        product = PhysicalProduct(
            "P005", "Lamp", 25, 10, 1.5, self.supplier
        )

        order_line = OrderLine(product, 2)
        self.assertEqual(order_line.quantity, 2)

    def test_zero_order_quantity(self):
        product = PhysicalProduct(
            "P006", "Lamp", 25, 10, 1.5, self.supplier
        )

        with self.assertRaises(ValueError):
            OrderLine(product, 0)

    def test_negative_order_quantity(self):
        product = PhysicalProduct(
            "P007", "Lamp", 25, 10, 1.5, self.supplier
        )

        with self.assertRaises(ValueError):
            OrderLine(product, -3)


if __name__ == "__main__":
    unittest.main()