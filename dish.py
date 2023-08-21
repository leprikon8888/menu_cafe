
class Dish:
    def __init__(self, name, description, price):

        if price <= 0:
            logger.info(f'Problem - (price <= 0): {name}; {description}')
            raise ValueError ('не может быть меньше или равно нулю')
        self.name = name
        self.description = description
        self.price = price



    def __str__(self):
        return f'{self.name} : {self.price:.2f}'
