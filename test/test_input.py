import unittest
from stock.dispatcher import Dispatcher
from stock.input.input_handler import InputHandler
from test.fake_observer import Observer

CORRECT_EVENT = '{"type": "ProductCreated", "id": 1, "stock": 10, "timestamp": 123, "parent_id": null}'
WRONG_TYPE_EVENT = '{"type": "ProductCreatedddd", "id": 1, "stock": 10, "timestamp": 123, "parent_id": null}'
INCOMPLETE_EVENT = '{"type": "ProductUpdated", "id": 1, "timestamp": 123}'
WRONG_DATA_EVENT = '{"type": "ProductEnded", "id": 1, "timestamp": "123"}'


class InputTest(unittest.TestCase):
    def setUp(self):
        self.event_source = Dispatcher()
        self.input = InputHandler(self.event_source)

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

    def test_translate_incomplete_event(self):
        self.assertRaises(ValueError, self.input.translate, INCOMPLETE_EVENT)

    def test_translate_wrong_data_event(self):
        self.assertRaises(TypeError, self.input.translate, WRONG_DATA_EVENT)

    def test_dispatch_translated_events(self):
        observer = Observer()
        self.input.add(observer)
        self.event_source.notify(CORRECT_EVENT)
        self.event_source.notify(INCOMPLETE_EVENT)
        self.assertEqual(observer.update_counter, 1)

if __name__ == '__main__':
    unittest.main()
