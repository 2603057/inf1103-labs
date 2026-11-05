
from product import Product


class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        for existing_product in self.__products:
            if existing_product.get_product_id() == product.get_product_id():
                print(f"Product ID '{product.get_product_id()}' already exists.")
                return

        self.__products.append(product)
        print("Product added successfully!")

    def search_product(self, product_id):
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

    def get_products(self):
        return self.__products
