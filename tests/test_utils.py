
import unittest
from src.utils import add_item, remove_item


class TestListUtilities(unittest.TestCase):
    def test_add_item(self):
        items = []
        self.assertTrue(add_item(items, "Book"))
        self.assertEqual(items, ["Book"])

    def test_add_empty_item(self):
        items = []
        self.assertFalse(add_item(items, " "))
        self.assertEqual(items, [])

    def test_remove_item(self):
        items = ["Book", "Pen"]
        self.assertTrue(remove_item(items, "Book"))
        self.assertEqual(items, ["Pen"])

    def test_remove_missing_item(self):
        items = ["Book"]
        self.assertFalse(remove_item(items, "Pen"))
        self.assertEqual(items, ["Book"])


if __name__ == "__main__":
    unittest.main()
