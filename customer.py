from shopping_cart import Shopping_cart
from product import Product
class Customer:
    def __init__(self, name):
        self.cart = []
        self.cart_price = []
        self.customer_name = name
        self.customers_cart = Shopping_cart(name) 
      

    def add_new_product(self, product, product_price):
        Shopping_cart.add_product_to_cart(self, product, product_price)

    def add_up_cart(self):
        
        price = Shopping_cart.add_up_price(self)
        print(f"The total of {self.customer_name}'s cart is currently ${price}") 

    def view_products(self):
            print(f"{self.customer_name}'s cart current contains {self.cart}")
   
    def empty_cart(self):
        Shopping_cart.empty_cart(self)