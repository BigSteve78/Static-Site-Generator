import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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


    def test_to_html_display(self):
        LeafNode1 = LeafNode(value = "This is some sample text ")
        LeafNode2 = LeafNode(value = "Bold Text ", tag = "b")
        LeafNode3 = LeafNode(value = "Click Me!!! ", tag = "a", props = {"href" : "https://www.google.co.uk"})
        ParentNode1 = ParentNode(tag = "p", children=[LeafNode1, LeafNode2, LeafNode3]) 
        self.assertEqual(ParentNode1.to_html(), '<p>This is some sample text <b>Bold Text </b><a href="https://www.google.co.uk">Click Me!!! </a></p>')

    def test_headings(self):
        node = ParentNode(
            tag = "h1",
            children = 
            [
                LeafNode(tag = "b", value = "Here is some bold text good sir."),
                LeafNode(value = "Here is some plain text, mr tester")
            ]
        )
        expected_string = "<h1><b>Here is some bold text good sir.</b>Here is some plain text, mr tester</h1>"
        self.assertEqual(node.to_html(), expected_string)
        
    def test_parent_as_child(self):
        node_child = ParentNode(
            tag = "h1",
            children = 
            [
                LeafNode(tag = "b", value = "Bold Text"),
                LeafNode(value = "Plain Text")
            ]
        )
        node = ParentNode(tag = "div", children = [node_child])
        expected_string = "<div><h1><b>Bold Text</b>Plain Text</h1></div>"
        self.assertEqual(node.to_html(), expected_string)


            
if __name__ == "__main__":
    unittest.main()