class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
            raise NotImplementedError
        
    def props_to_html(self):
            if self.props == None:
                  return ""
            tags = []
            for tag, value in self.props.items():
                string = (f' {tag}="{value}"')
                tags.append(string)
            string = ""
            for tag in tags:
                string += tag
            return string

    def __repr__(self):
            return(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")
    
class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props = None):
        super().__init__(tag, value, None, props)

        if value == None:
            raise ValueError("LeafNode must have a value")
        else:
            self.value = value

        self.children = None
        
    def to_html(self):
        if self.value == None:
            raise ValueError("All LeafNodes need a value")
        if self.tag == None:
            return self.value
        else:
            return (f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>")

            # <p>This is a paragraph of text.</p>               
            #<a href="https://www.google.com">Click me!</a>

            # <tag (props)>value</tag>