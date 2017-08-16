from stock.products.product_tree import ProductTree
from stock.products.output_event import OutputEvent

class ProductController:
    def __init__(self, event_source, notifier):
        self.trees = {}
        self.notifier = notifier
        self.timestamp = 0
        event_source.add(self)

    def update(self, body):
        if body['timestamp'] < self.timestamp:
            return
        self.timestamp = body['timestamp']
        body_type = body['type']
        if body_type == 'ProductCreated':
            self.create_product(body)
        if body_type == 'ProductUpdated':
            self.update_product(body)
        if body_type == 'ProductEnded':
            self.end_product(body)

    def create_product(self, body):
        if body['parent_id'] == None:
            self.trees[body['id']] = ProductTree(body['id'], body['stock'], self.notifier)
        else:
            self.trees[body['parent_id']].add_child(body['id'], body['stock'])

    def update_product(self, body):
        tree = self.find_tree(body['id'])
        if tree:
            tree.update(body['id'], body['stock'])

    def end_product(self, body):
        tree = self.find_tree(body['id'])
        if tree:
            tree.end(body['id'])

    def find_tree(self, id):
        if id in self.trees.keys():
            return self.trees[id]
        for tree in self.trees.values():
            product = tree.get(id)
            if product != None: return tree
        return None

    def stocks(self):
        stocks = {}
        for tree in self.trees.values():
            stocks = {**stocks, **tree.stock_summary()}
        return stocks

    def send_summary(self):
        self.notifier.notify(OutputEvent(type='StockSummary', stocks=self.stocks()))

