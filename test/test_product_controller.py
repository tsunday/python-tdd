import unittest

from stock.dispatcher import Dispatcher
from stock.products.product_controller import ProductController
from test.test_utils.fake_notifier import Notifier


class ProductControllerTest(unittest.TestCase):
    def setUp(self):
        self.event_source = Dispatcher()
        self.product_controller = ProductController(self.event_source, Notifier())

    def test_handle_parent_product_creation(self):
        self.event_source.notify({'type': 'ProductCreated', 'id': 1, 'stock': 10, 'timestamp': 123, 'parent_id': None})
        self.assertEqual(len(self.product_controller.trees), 1)


if __name__ == '__main__':
    unittest.main()
