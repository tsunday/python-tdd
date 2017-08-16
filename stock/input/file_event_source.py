from stock.dispatcher import Dispatcher


class FileEventSource(Dispatcher):
    def __init__(self, filepath):
        Dispatcher.__init__(self)
        self.filepath = filepath

    def consume(self):
        with open(self.filepath) as events:
            for event in events:
                self.notify(event)
