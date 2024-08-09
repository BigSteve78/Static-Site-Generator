import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node,node2)

    def test_not_eq2(self):
        node = TextNode("Sample Text Here", "italic", "https.yummers")
        node2 = TextNode("Sample Text Here", "italic", "https.notyummers")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Sample Text", "bold")
        actual_string = ("TextNode(Sample Text, bold, None)")
        self.assertEqual(repr(node), actual_string)
        #(f"TextNode({self.text}, {self.text_type}, {self.url})")

if __name__ == "__main__":
    unittest.main()