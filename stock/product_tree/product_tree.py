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

    def end(self, id):
        if self._parent.id != id:
            self.get(id).end()
        else:
            self._parent.end()
            self.end_others(id)

    def end_others(self, id):
        for child_id in self._childs:
            if id != child_id: self._childs[child_id].end()
        if id != self._parent.id: self._parent.end()


