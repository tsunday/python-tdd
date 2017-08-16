from stock.product_tree.product_tree import ProductTree


class ProductController:
    def __init__(self, event_source, notifier):
        self.trees = {}
        self.notifier = notifier
        event_source.add(self)

    def update(self, body):
        type = body['type']
        if type == 'ProductCreated':
            self.create_product(body)
        if type == 'ProductUpdated':
            self.update_product(body)
        if type == 'ProductEnded':
            self.end_product(body)

    def create_product(self, body):
        self.trees[body['id']] = ProductTree(body['id'], body['stock'], self.notifier)

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
