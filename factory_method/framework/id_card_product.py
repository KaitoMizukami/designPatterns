from framework.factory import Factory
from framework.product import Product


class IDCardProduct(Product):
    def __init__(self, owner):
        self.owner = owner 
        print(f'I will create {self.owner} card')
    
    def use(self):
        print(f'I will use {self.owner} card')