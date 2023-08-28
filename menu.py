from menuCategory import MenuCategory


class MenuIter:
    def __init__(self, menu):
        self.__menu = menu
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.__menu):
            self.index += 1
            return self.__menu[self.index - 1]
        raise StopIteration


class Menu:
    def __init__(self):
        self.menu = []

    def add_menu(self, menu_category: MenuCategory):
        if not isinstance(menu_category, MenuCategory):
            logger.info(f'Problem - Type error: not MenuCategory')
            raise TypeError('error in MenuCategory datatype')
        self.menu.append(menu_category)

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.menu):
                return self.menu[index]
            raise IndexError("Index out of range")

        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.menu) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step

            tmp = []
            if start < 0 and stop > len(self.menu):
                raise IndexError
            for i in range(start, stop, step):
                tmp.append(self.menu[i])
            return tmp

    def __len__(self):
        return len(self.menu)

    def __iter__(self):
        return MenuIter(self.menu)

    def __str__(self):
        res = ''
        for x in self.menu:
            res += str(x) + '\n'
        return res
