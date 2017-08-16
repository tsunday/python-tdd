class Product(object):
    def __init__(self, id, parent_id, stock):
        self.id = id
        self.parent_id = parent_id
        self.is_ended = False

    def end(self):
        self.is_ended = True