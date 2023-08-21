from discount import Discount
class RegularDiscount(Discount):
    def __init__(self, value =3):
        super().__init__(value)
    def discount(self):
        return  1 -self.value/100