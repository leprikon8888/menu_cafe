from dish import Dish


class Order:
    def __init__(self):
        self.order_dishes = []
        self.quantity = []

    def add_item(self, dish: Dish, quantity =1):
        if not isinstance(dish, Dish):
            logger.info(f'Problem - Type error: not Dish')
            raise TypeError('Error in Dish datatype')
        if not isinstance(quantity, int|float ):
            logger.info(f'Problem - Type error: not int or float')
            raise TypeError('Error in quantity of Dish')
        if quantity<=0:
            logger.info(f'Problem - (quantity <= 0): {dish}; {quantity}')
            raise ValueError('Quantity must be > 0. But less or equal got.')
        self.order_dishes.append(dish)
        self.quantity.append(quantity)

    def total_summ(self):
        result = 0
        for x, y in zip(self.order_dishes, self.quantity):
            result += x.price * y
        return result

    def __str__(self):
        res = ""
        for x, y in zip(self.order_dishes, self.quantity):
            res += f'{x} x {y} = {x.price*y} $\n'
        res += f'Total = {self.total_summ()} $'
        return res