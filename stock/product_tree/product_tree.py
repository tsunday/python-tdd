from stock.product_tree.product import Product


class ProductTree:
    def __init__(self, id, stock):
        self._parent = Product(id, None, stock)
        self._childs = {}

    def add_child(self, id, stock):
        self._childs[id] = Product(id, self._parent.id, stock)
        self.synch_stock(stock)

    def synch_stock(self, new_value):
        self._parent.stock = new_value
        for id in self._childs:
            self._childs[id].stock = new_value

    def update(self, id, stock):
        self.synch_stock(stock)

    def get(self, id):
        if self._parent.id == id:
            return self._parent
        return self._childs[id]