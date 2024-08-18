import unittest, textnode, inline_markdown
from inline_markdown import *
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
        new_nodes = split_nodes_delimeter(new_nodes, "*", text_type_italic)
        self.assertEqual(new_nodes, self.test_answers[4])

class Test_Extraction(unittest.TestCase):
    test_answers = [
        [("rick roll", "https://i.imgur.com/aKaOqIh.gif")],
        [("funky monkey", "https://funkymonkey.png"), ("alt text", "https://someimageidk.jpeg")],
        [("link", ("https://website"))]
    ]

    def test_image_extraction(self):
        text = "This has a link ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text), self.test_answers[0])

    def test_multiple_images(self):
        text = "Image: ![funky monkey](https://funkymonkey.png) Image 2: ![alt text](https://someimageidk.jpeg)"
        self.assertEqual(extract_markdown_images(text), self.test_answers[1])

    def test_link_extraction(self):
        text = "Here is a [link](https://website)"
        self.assertEqual(extract_markdown_links(text), self.test_answers[2])