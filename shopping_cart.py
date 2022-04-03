from product import Product
class Shopping_cart:
    def __init__(self, customers_name):
        self.customers_cart = customers_name
        self.cart = []
        self.cart_price = []
    
    def add_up_price(self,):
        current_total = sum(self.cart_price)
        return current_total

    def add_product_to_cart(self, product, product_price):
        self.cart.append(product)
        self.cart_price.append(product_price)
        print(f"Your {product} has been added to your shopping cart")

    def empty_cart(self):
        self.cart.clear()
        self.cart_price.clear()
        print("Your shopping cart has been emptied")   