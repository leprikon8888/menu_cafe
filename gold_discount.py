from discount import Discount

class GoldDiscount(Discount):
    def __init__(self, value =10):
        super().__init__(value)
    def discount (self):
        return  1 -self.value/100