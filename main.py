from alarm_clock import Alarm 
from customer import Customer
from product import Product

# my_clock = Alarm()
# print(my_clock.current_time)
# my_clock.change_current_time(1600)
# my_clock.change_on_or_off(True)

customer = Customer("tommy")
print(customer.customer_name) 
customer.add_new_product("milk")
customer.add_new_product("Flour")
customer.add_new_product("Sugar")


