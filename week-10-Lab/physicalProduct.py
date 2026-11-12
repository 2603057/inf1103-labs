from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight, supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return f"Physical product weighing {self.__weight} kg"

    def calculate_shipping_cost(self):
        base_cost = 5.0  
        cost_per_kg = 2.0
        return base_cost + (cost_per_kg * self.__weight)

    def get_shipping_details(self):
        return f"Physical product with weight {self.__weight} kg"

    def get_weight(self):
        return self.__weight