from framework.factory import Factory
from framework.id_card_product import IDCardProduct


class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []
    
    def createProduct(self, owner):
        return IDCardProduct(owner)

    def registerProduct(self, product):
        self.owners.append(product.owner)