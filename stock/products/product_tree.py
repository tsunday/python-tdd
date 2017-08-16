from stock.products.product import Product
from stock.products.output_event import OutputEvent


class ProductTree:
    def __init__(self, id, stock, notifier):
        self._parent = Product(id, None, stock)
        self._childs = {}
        self.notifier = notifier

    def add_child(self, id, stock):
        self._childs[id] = Product(id, self._parent.id, stock)
        self.synch_stock(id, stock)

    def synch_stock(self, id, new_value):
        self._parent.stock = new_value
        if self._parent.id != id:
            self.notifier.notify(OutputEvent('ProductUpdated', self._parent.id, new_value))
        for child_id in self._childs:
            self._childs[child_id].stock = new_value
            if child_id != id:
                self.notifier.notify(OutputEvent('ProductUpdated', child_id, new_value))

    def update(self, id, stock):
        self.synch_stock(id, stock)
        if (stock == 0):
            self.end_others(id)

    def get(self, id):
        if self._parent.id == id:
            return self._parent
        try:
            return self._childs[id]
        except:
            return None

    def end(self, id):
        if self._parent.id != id:
            self.get(id).end()
        else:
            self._parent.end()
            self.end_others(id)

    def end_others(self, id):
        for child_id in self._childs:
            if id != child_id:
                self._childs[child_id].end()
                self.notifier.notify(OutputEvent('ProductEnded', child_id))
        if id != self._parent.id: self._parent.end()
