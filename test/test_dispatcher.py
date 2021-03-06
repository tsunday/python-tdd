import unittest

from stock.dispatcher import Dispatcher
from test.test_utils.fake_observer import Observer


class DispatcherTest(unittest.TestCase):
    def setUp(self):
        self.dispatcher = Dispatcher()

    def test_add_observer(self):
        self.dispatcher.add(Observer())
        self.assertEqual(len(self.dispatcher._observers), 1)

    def test_notify_observer(self):
        observer = Observer()
        self.dispatcher.add(observer)
        self.dispatcher.notify()
        self.assertEqual(observer.update_counter, 1)


if __name__ == '__main__':
    unittest.main()
