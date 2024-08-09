import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None,None,None, {
        "href": "https://www.google.com", 
         "target": "_blank",
        })
        expected_string = ' href="https://www.google.com" target="_blank"'  
        self.assertEqual(node.props_to_html(), expected_string)

    def test_repr(self):
        node = HTMLNode("<p>", "Sample Text Here", None,)
        expected_string = "HTMLNode(<p>, Sample Text Here, None, None)"
        self.assertEqual(repr(node), expected_string)

if __name__ == "__main__":
    unittest.main()