import unittest
from stock.dispatcher import Dispatcher
from stock.input import Input


class InputTest(unittest.TestCase):
    def test_requires_event_source(self):
        event_source = Dispatcher()
        input = Input(event_source)
        self.assertEqual(len(event_source._observers), 1)


if __name__ == '__main__':
    unittest.main()
