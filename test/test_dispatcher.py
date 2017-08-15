import unittest
from stock.dispatcher import Dispatcher


class Observer:
    def update(self):
        print('callback called')


class DispatcherTest(unittest.TestCase):
    def test_add_observer(self):
        dispatcher = Dispatcher()
        dispatcher.add(Observer())
        self.assertEqual(len(dispatcher._observers), 1)


if __name__ == '__main__':
    unittest.main()
