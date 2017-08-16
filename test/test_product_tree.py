import unittest

from stock.product_tree.product_tree import ProductTree


class ProductTreeTest(unittest.TestCase):
    def test_synchronize_stock(self):
        tree = ProductTree(1, 10)
        tree.add_child(2, 9)
        self.assertEqual(tree._parent.stock, 9)

    def test_update_parent(self):
        tree = ProductTree(1, 10)
        tree.add_child(2, 10)
        tree.update(1, 3)
        self.assertEqual(tree.get(2).stock, 3)

if __name__ == '__main__':
    unittest.main()
