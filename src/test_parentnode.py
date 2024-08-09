import parentnode, unittest, leafnode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
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


            
        