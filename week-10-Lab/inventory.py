
from product import Product


class Inventory:

    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product):
        for existing_product in self.__products:
            if existing_product.get_product_id() == product.get_product_id():
                print(f"Product ID '{product.get_product_id()}' already exists.")
                return

        self.__products.append(product)
        print("Product added successfully!")

    def remove_product(self, product_id: str):
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                print("Product removed successfully!")
                return

        print(f"Product ID '{product_id}' not found.")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory")
        print("------------------------------------------------")

        for product in self.__products:
            product.display_information()

        print("------------------------------------------------")

    def get_products(self) -> list[Product]:
        return self.__products
