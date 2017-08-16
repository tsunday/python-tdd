class Product(object):
    products = []

    def __init__(self, id, parent_id, stock):
        self.id = id
        self.parent_id = parent_id
        self.stock = stock
        self.products.append(self)
        if parent_id is not None:
            self.update_products()

    def update_products(self):
        for product in self.products:
            if product.id == self.parent_id or product.parent_id == self.parent_id:
                product.stock = self.stock

