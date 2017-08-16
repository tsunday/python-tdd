import unittest

from stock.product_tree.product_tree import ProductTree


class ProductTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = ProductTree(1, 10)
        self.tree.add_child(2, 9)

    def test_synchronize_stock(self):
        self.assertEqual(self.tree._parent.stock, 9)

    def test_update_parent(self):
        self.tree.update(1, 3)
        self.assertEqual(self.tree.get(2).stock, 3)

    def test_end_parent(self):
        self.tree.end(1)
        self.assertTrue(self.tree.get(1).is_ended)
        self.assertTrue(self.tree.get(2).is_ended)


if __name__ == '__main__':
    unittest.main()
