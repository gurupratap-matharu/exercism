class MyParser:
    def __init__(self, text_1, text_2):
        self.text_1 = text_1
        self.text_2 = text_2

    def parse_text(self, text):
        stack = []
        for char in text:
            if char != '#':
                stack.append(char)
            else:
                if len(stack) > 0:
                    stack.pop()
        return ''.join(stack)

    def check_if_equal(self):
        return self.parse_text(self.text_1) == self.parse_text(self.text_2)
