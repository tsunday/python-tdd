from stock.dispatcher import Dispatcher


class FileEventSource(Dispatcher):
    def __init__(self, filepath):
        with open(filepath) as events:
            for event in events:
                self.notify(event)
