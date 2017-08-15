class Dispatcher:
    _observers = []

    def add(self, observer):
        self._observers.append(observer)
