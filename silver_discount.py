from discount import Discount

class SilverDiscount(Discount):
    def __init__(self, value =7):
        super().__init__(value)
    def discount(self):
        return  1 -self.value/100