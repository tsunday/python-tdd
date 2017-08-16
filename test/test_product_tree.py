import unittest

from stock.product_tree.product import Product


class ProductTreeTest(unittest.TestCase):
    def test_synchronize_stock(self):
        parent = Product(1, None, 10)
        child = Product(2, 1, 9)
        self.assertEqual(parent.stock, 9)


if __name__ == '__main__':
    unittest.main()
