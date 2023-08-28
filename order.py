from dish import Dish

class OrderIter:
    def __init__(self, order_dishes, quantities):
        self.__order_dishes = order_dishes
        self.__quantities = quantities
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.__order_dishes):
            self.index += 1
            return self.__order_dishes[self.index - 1], self.__quantities[self.index - 1]
        raise StopIteration

class Order:
    def __init__(self):
        self.order_dishes = []
        self.quantity = []

    def add_item(self, dish: Dish, quantity=1):
        if not isinstance(dish, Dish):
            logger.info(f'Problem - Type error: not Dish')
            raise TypeError('Error in Dish datatype')
        if not isinstance(quantity, int | float):
            logger.info(f'Problem - Type error: not int or float')
            raise TypeError('Error in quantity of Dish')
        if quantity <= 0:
            logger.info(f'Problem - (quantity <= 0): {dish}; {quantity}')
            raise ValueError('Quantity must be > 0. But less or equal got.')
        self.order_dishes.append(dish)
        self.quantity.append(quantity)

    def total_summ(self):
        result = 0
        for x, y in zip(self.order_dishes, self.quantity):
            result += x.price * y
        return result

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.order_dishes):
                return self.order_dishes[index]
            raise IndexError("Index out of range")

        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.order_dishes) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            tmp = []
            if start < 0 and stop > len(self.order_dishes):
                raise IndexError
            for i in range(start, stop, step):
                tmp.append(self.order_dishes[i])
            return tmp

    def __len__(self):
        return len(self.order_dishes)

    def __iter__(self):
        return OrderIter(self.order_dishes, self.quantity)

    def __str__(self):
        res = ""
        for x, y in zip(self.order_dishes, self.quantity):
            res += f'{x} x {y} = {x.price * y} $\n'
        res += f'Total = {self.total_summ()} $'
        return res
