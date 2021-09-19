class Text_Box:
    def __init__(self, x, y, width, height, text, word_length):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.word_length = word_length


class Page_Template:
    def __init__(self, text_boxes, text):
        self.text_boxes = text_boxes
        self.text = text

    def split_texts(self):
        pass

    def render_page(self):
        pass