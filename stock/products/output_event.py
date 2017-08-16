class OutputEvent:
    def __init__(self, type, id=None, stock=None, stocks=None):
        self.type = type
        if id: self.id = id
        if stock: self.stock = stock
        if stocks: self.stocks = stocks