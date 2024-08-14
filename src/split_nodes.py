import textnode
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_italic
)


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        str = node.text
        #split_nodes = []
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
    
            

node = TextNode("This is some **bold** text.", text_type_text)
node2 = TextNode("More **BOLD** text!!!", text_type_text)

new_nodes = split_nodes_delimeter([node, node2], "**", text_type_bold)

#print(new_nodes)