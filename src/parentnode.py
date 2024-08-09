import htmlnode, leafnode

from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):         
    # The parent acts as the container for the leaf nodes.
    def __init__(self, children, tag, props = None):
        super().__init__(tag=tag, children=children, props=props, value = None)

        if children == None:
            raise ValueError("children is a required argument")
        else:
            self.children = children

        self.value = None

    def to_html(self):
        if self.tag == None:
            raise ValueError("A tag is required")

        if self.children == None:
            raise ValueError("Children are required")
        
        child_text = ""

        for child in self.children:
            child_text += child.to_html()

        return f"<{self.tag}{super().props_to_html()}>{child_text}</{self.tag}>"
        # (f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>")
