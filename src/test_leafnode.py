import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(tag = "p", value = "Sample Text")
        expected_string = "<p>Sample Text</p>"
        self.assertEqual(node.to_html(), expected_string)

    def test_to_html_no_tag(self):
        node = LeafNode (value = "Sample Text")
        expected_string = "Sample Text"
        self.assertEqual(node.to_html(), expected_string)

    def test_to_html_props(self):
        node = LeafNode(tag = "a", value = "Please Click Me!!!", props = {"href" : "https://www.google.com"})
        expected_string = '<a href="https://www.google.com">Please Click Me!!!</a>'
        self.assertEqual(node.to_html(), expected_string)

    
if __name__ == "__main__":
    unittest.main()