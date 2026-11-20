import unittest

from order import Order
from supplier import Supplier
from physicalProduct import PhysicalProduct

from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount


class TestDiscountStrategy(unittest.TestCase):

    def setUp(self):
        supplier = Supplier("S001", "Dell", "dell@email.com")

        product = PhysicalProduct(
            "P001", "Desk Lamp", 25.00, 10, 1.5, supplier
        )

        self.order = Order("O001")
        self.order.add_order_line(product, 10)

    def test_no_discount(self):
        self.order.set_discount(NoDiscount())
        self.assertEqual(self.order.get_total(), 250.0)

    def test_bulk_discount(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.get_total(), 230.0)

    def test_percentage_discount(self):
        self.order.set_discount(PercentageDiscount(10))
        self.assertEqual(self.order.get_total(), 225.0)

    def test_student_discount(self):
        self.order.set_discount(StudentDiscount())
        self.assertEqual(self.order.get_total(), 237.5)


if __name__ == "__main__":
    unittest.main()