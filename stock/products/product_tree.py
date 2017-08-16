from stock.products.product import Product
from stock.products.output_event import OutputEvent


class ProductTree:
    def __init__(self, id, stock, notifier):
        self._parent = Product(id, None, stock)
        self._children = {}
        self.notifier = notifier

    def add_child(self, id, stock):
        self._children[id] = Product(id, self._parent.id, stock)
        self.synch_stock(id, stock, True)

    def synch_stock(self, id, new_value, silent=False):
        self._parent.stock = new_value
        if self._parent.id != id and not silent:
            self.notifier.notify(OutputEvent('UpdateProduct', self._parent.id, new_value))
        for child_id in self._children:
            self._children[child_id].stock = new_value
            if child_id != id and not silent:
                self.notifier.notify(OutputEvent('UpdateProduct', child_id, new_value))

    def update(self, id, stock):
        self.synch_stock(id, stock)
        if (stock == 0):
            self.end_others(id)

    def get(self, id):
        if self._parent.id == id:
            return self._parent
        try:
            return self._children[id]
        except:
            return None

    def end(self, id):
        if self._parent.id != id:
            self.get(id).end()
        else:
            self._parent.end()
            self.end_others(id)

    def end_others(self, id):
        for child_id in self._children:
            if id != child_id:
                self._children[child_id].end()
                self.notifier.notify(OutputEvent('EndProduct', child_id))
        if id != self._parent.id: self._parent.end()

    def stock_summary(self):
        stock = {}
        stock[self._parent.id] = self._parent.stock
        for child in self._children:
            stock[self._children[child].id] = self._children[child].stock
        return stock
