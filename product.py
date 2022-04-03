
from unicodedata import category


class Product:
    def __init__(self, product_name, price, category):
        self.name = product_name
        self.price = price
        self.category = category