class Dispatcher:
    def __init__(self):
        self._observers = []

    def add(self, observer):
        self._observers.append(observer)

    def notify(self, body):
        for observer in self._observers:
            observer.update(body)
