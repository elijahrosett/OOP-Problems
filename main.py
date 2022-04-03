from alarm_clock import Alarm 
from customer import Customer
from product import Product
from shopping_cart import Shopping_cart

# my_clock = Alarm()
# print(my_clock.current_time)
# my_clock.change_current_time(1600)
# my_clock.change_on_or_off(True)
milk = Product("Milk", 3, "dairy")
flour = Product("Flour", 2, "baking")
sugar = Product("Sugar", 4, "baking")
customer_tommy = Customer("Tommy")

print(customer_tommy.customer_name) 
customer_tommy.add_new_product(milk.name, milk.price)
customer_tommy.add_new_product(flour.name, flour.price)
customer_tommy.add_new_product(sugar.name, sugar.price)
customer_tommy.view_products()
customer_tommy.add_up_cart()
customer_tommy.empty_cart()
print(customer_tommy.cart)

tim = Customer("tim")
tim.add_new_product(milk.name, milk.price)
tim.view_products()
