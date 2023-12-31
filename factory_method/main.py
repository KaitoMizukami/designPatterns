from framework.id_card_factory import IDCardFactory


def main(factoryObject):
    card1 = factoryObject.create("Hiroshi Yuki")
    card2 = factoryObject.create("Tomura")
    card3 = factoryObject.create("Hanako Sato")
    card1.use()
    card2.use()
    card3.use()

if __name__ == "__main__":
    main(IDCardFactory())