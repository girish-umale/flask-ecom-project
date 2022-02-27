class Product:
    """This structure is defined to describe what product means"""

    def __init__(self, pid=0, pnm="", pqty=0, pven="", ppric=0.0):
        self.productId = int(pid)
        self.productName = pnm
        self.productQuantity = int(pqty)
        self.productVendor = pven
        self.productPrice = float(ppric)

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)


# a = Product(10, "aaa", 12, "Flipkart", 313148)

print(Product.__doc__)
