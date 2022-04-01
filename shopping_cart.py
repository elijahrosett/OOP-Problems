class Shopping_cart:
    def __init__(self, customers_name):
        self.customers_cart = customers_name
        self.product_list = []
        self.product_list_price = []
    
    def add_up_price(self, list):
        current_total = sum(list)
        return current_total

    def add_product_to_cart(self, new_product):
        self.product_list.append(new_product)
        print(f"Your {new_product} has been added to your shopping cart")

    def empty_cart(self):
        self.product_list.clear
        self.product_list_price.clear
        print("Your shopping cart has been emptied")   