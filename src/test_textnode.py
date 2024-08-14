import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link
)

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
        actual_string = ('TextNode("Sample Text", bold, None)')
        self.assertEqual(repr(node), actual_string)
        #(f"TextNode({self.text}, {self.text_type}, {self.url})")

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode(text="This is some text", text_type="text")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is some text" )

    def test_bold(self):
        node = TextNode(text="This is some bold text", text_type="bold")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is some bold text" )
    
    def test_bold(self):
        node = TextNode(text="This is some italic text", text_type="italic")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is some italic text" )

    def test_code(self):
        node = TextNode(text="This is some code", text_type="code")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is some code" )

    def test_link(self):
        node = TextNode(text="Click Me!!!", text_type="link", url = "https://google.co.uk")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.value, "Click Me!!!")
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href":"https://google.co.uk"})

    def test_image(self):
        node = TextNode(text="Here is an image", text_type="image", url = "https://google.co.uk")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src":"https://google.co.uk", "alt":"Here is an image"})

if __name__ == "__main__":
    unittest.main()