from dish import Dish


class MenuCategoryIter:
    def __init__(self, dishes):
        self.__dishes = dishes
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.__dishes):
            self.index += 1
            return self.__dishes[self.index - 1]
        raise StopIteration


class MenuCategory:
    def __init__(self):
        self.dishes = []

    def add_dishes(self, dish: Dish):
        if not isinstance(dish, Dish):
            logger.info(f'Problem - Type error: not Dish')
            raise TypeError('error in Dish datatype')
        self.dishes.append(dish)

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.dishes):
                return self.dishes[index]
            raise IndexError("Index out of range")

        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.dishes) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step

            tmp = []
            if start < 0 and stop > len(self.dishes):
                raise IndexError
            for i in range (start, stop, step):
                tmp.append(self.dishes[i])
            return tmp

    def __len__(self):
        return len(self.dishes)

    def __iter__(self):
        return MenuCategoryIter(self.dishes)

    def __str__(self):
        res = ''
        for x in self.dishes:
            res += str(x) + '\n'
        return res


