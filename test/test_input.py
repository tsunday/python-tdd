import unittest
from stock.dispatcher import Dispatcher
from stock.input import Input

CORRECT_EVENT = '{"type": "ProductCreated", "id": 1, "stock": 10, "timestamp": 123, "parent_id": null}'
WRONG_TYPE_EVENT = '{"type": "ProductCreatedddd", "id": 1, "stock": 10, "timestamp": 123, "parent_id": null}'


class InputTest(unittest.TestCase):
    def setUp(self):
        self.event_source = Dispatcher()
        self.input = Input(self.event_source)

    def test_require_event_source(self):
        self.assertEqual(len(self.event_source._observers), 1)

    def test_translate_correct_events(self):
        translated_event = self.input.translate(CORRECT_EVENT)
        expected_event = {
            'type': 'ProductCreated',
            'id': 1,
            'stock': 10,
            'timestamp': 123,
            'parent_id': None
        }
        self.assertDictEqual(translated_event, expected_event)

    def test_translate_wrong_type_event(self):
        self.assertRaises(ValueError, self.input.translate, WRONG_TYPE_EVENT)


if __name__ == '__main__':
    unittest.main()
