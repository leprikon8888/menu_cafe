from discount import Discount
from order import Order

class Client:
    def __init__(self, name, discount : Discount):
        if not isinstance(discount, Discount):
            logger.info(f'Problem - Type error: not Discount')
            raise TypeError('Error in Discount datatype')

        self.name = name
        self.discount = discount

    def get_total_price(self, order: Order):
        if not isinstance(order, Order):
            logger.info(f'Problem - Type error: not Order')
            raise TypeError('Error in Order datatype')
        return f'your check including discounts - ({order.total_summ() * self.discount.discount()})'

    def __str__(self):
        return f"Your order: \n"