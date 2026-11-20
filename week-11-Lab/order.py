
from orderline import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount


class Order:

    def __init__(
        self,
        order_id: str,
        discount: DiscountStrategy = None
    ):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        for order_line in self.order_lines:
            if order_line.product.get_product_id() == product_id:
                self.order_lines.remove(order_line)
                print("Order line removed successfully!")
                return

        print(f"Product ID '{product_id}' not found in order.")

    def get_order_lines(self) -> list[OrderLine]:
        return self.order_lines.copy()

    def display_order(self) -> None:
        if not self.order_lines:
            print("Order is empty.")
            return

        print(f"\nOrder ID: {self.order_id}")
        print("----------------------------------------")

        for order_line in self.order_lines:
            order_line.product.display_information()
            print(f"Quantity: {order_line.quantity}")
            print(f"Subtotal: ${order_line.get_subtotal():.2f}")
            print("----------------------------------------")

        print(f"Order Total: ${self.get_total():.2f}")

    def get_total(self) -> float:
        total = 0.0

        for order_line in self.order_lines:
            total += order_line.get_subtotal()

        return self.discount.apply(total)
