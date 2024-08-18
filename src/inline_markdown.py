import textnode, re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_image,
    text_type_link
)


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        str = node.text
        sections = str.split(sep=delimeter, maxsplit = -1)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Syntax, formatted section was not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text = sections[i], text_type=text_type_text))
            else:
                new_nodes.append(TextNode(text = sections[i], text_type=text_type))
    return new_nodes    

def extract_markdown_images(text):
    list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return list

def extract_markdown_links(text):
    list = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return list

def split_nodes_image(old_nodes):
    pass