from menuCategory import MenuCategory


class Menu:
    def __init__(self):
        self.menu = []

    def add_menu(self, menu_category: MenuCategory):
        if not isinstance(menu_category, MenuCategory):
            logger.info(f'Problem - Type error: not MenuCategory')
            raise TypeError('error in MenuCategory datatype')
        self.menu.append(menu_category)

    def __str__(self):
        res = ''
        for x in self.menu:
            res += str(x) + '\n'
        return res
