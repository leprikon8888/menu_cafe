from dish import Dish
class MenuCategory:
    def __init__(self):
        self.dishes = []

    def add_dishes(self, dish: Dish):
        if not isinstance(dish, Dish):
            logger.info(f'Problem - Type error: not Dish')
            raise TypeError('error in Dish datatype')
        self.dishes.append(dish)

    def __str__(self):
        res = ''
        for x in self.dishes:
            res += str(x) + '\n'
        return res
