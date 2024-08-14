import unittest, textnode, split_nodes
from split_nodes import split_nodes_delimeter
from textnode import(
    TextNode,
    text_type_text,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_bold
)


class TestSplitNodes(unittest.TestCase):

    test_answers = [
        [
            TextNode("This is some ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text.", text_type_text)
        ],
        [
            TextNode("This is some ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text.", text_type_text),
            TextNode("More ", text_type_text),
            TextNode("BOLD", text_type_bold),
            TextNode(" text!!!", text_type_text)
        ],
        [
            TextNode("This is some ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" text.", text_type_text)
        ],
        [
            TextNode("Some ", text_type_text),
            TextNode("double", text_type_bold),
            TextNode(" text ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" please.", text_type_text)
        ],
        [
            TextNode("Bold", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("italic", text_type_italic)
        ]
    ]

    def test_splitting(self):
        node = TextNode("This is some **bold** text.", text_type_text)
        new_nodes = split_nodes_delimeter([node], "**", text_type_bold)
        self.assertEqual(new_nodes, self.test_answers[0])
    
    def test_multiple_nodes(self):
        node = TextNode("This is some **bold** text.", text_type_text)
        node2 = TextNode("More **BOLD** text!!!", text_type_text)
        new_nodes = split_nodes_delimeter([node,node2], "**", text_type_bold)
        self.assertEqual(new_nodes, self.test_answers[1])
    
    def test_italics(self):
        node = TextNode("This is some *italic* text.", text_type_text)
        new_nodes = split_nodes_delimeter([node], "*", text_type_italic)
        self.assertEqual(new_nodes, self.test_answers[2])
        
    def test_double_bold(self):
        node = TextNode("Some **double** text **bolded** please.", text_type_text)
        new_nodes = split_nodes_delimeter([node], "**", text_type_bold)
        self.assertEqual(new_nodes, self.test_answers[3])

    def test_multiple_types(self):
        node = TextNode("**Bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimeter([node], "**",  text_type_bold)
        print(new_nodes)
        new_nodes = split_nodes_delimeter(new_nodes, "*", text_type_italic)
        print(new_nodes)
        self.assertEqual(new_nodes, self.test_answers[4])