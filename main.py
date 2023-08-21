import logging
from dish import Dish
from menuCategory import MenuCategory
from menu import Menu
from order import Order
from discount import Discount
from regular_discount import RegularDiscount
from silver_discount import SilverDiscount
from gold_discount import GoldDiscount
from client import Client

logger = logging.getLogger('order_processing')
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('log_ord.log')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(console_handler)

try:

    a = Dish('kola', 'drink', 10)
    b = Dish('apple', 'frukt', 95)
    c = Dish('soda', 'drink', 30)
    d = Dish('kiwi', 'ice', 40)

    breakfast = MenuCategory()
    breakfast.add_dishes(d)
    breakfast.add_dishes(c)

    lunch = MenuCategory()
    lunch.add_dishes(b)

    dinner = MenuCategory()
    dinner.add_dishes(d)

    menu = Menu()
    menu.add_menu(breakfast)
    menu.add_menu(lunch)
    menu.add_menu(dinner)

    gld = GoldDiscount()


    sasha  = Client('sasha', gld)
    sasha_order = Order()
    sasha_order.add_item(a,3)
    sasha_order.add_item(c,8)
    sasha_order.add_item(d)
    print(sasha.get_total_price(sasha_order))
except MyNewError as error:
        print (error)
except TypeError as error:
        print(error)
except:
        print('Error')

print(sasha, sasha_order, sasha.get_total_price(sasha_order) )