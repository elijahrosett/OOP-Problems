from shopping_cart import Shopping_cart
from product import Product
class Customer:
    def __init__(self, name):
        self.product_list = []
        self.customer_name = name
        self.customers_cart = Shopping_cart(name) 
      

    def add_new_product(self, product):
        Shopping_cart.add_product_to_cart(self, product)

    def view_products(self, list):
        for items in list:
            print(items)
