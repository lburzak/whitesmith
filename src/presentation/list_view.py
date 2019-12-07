from view import View


class ListView(View):
    items: [str]
    pos: int = 0
    height: int
    first_line_index = 0

    def __init__(self, items: [str], height: int = 10):
        self.items = items
        self.height = height

    def get_last_line_index(self) -> int:
        return self.height + self.first_line_index\
            if len(self.items) > self.height and self.height + self.first_line_index <= len(self.items) - 1\
            else len(self.items) - 1

    def adjust_position(self, last_line_index):
        if self.pos > last_line_index:
            self.pos = last_line_index

    def render(self) -> str:
        last_line_index = self.get_last_line_index()
        self.adjust_position(last_line_index)

        s = ""
        for i in range(self.first_line_index, last_line_index + 1):
            if self.pos == i:
                s += "> "
            else:
                s += "  "
            s += self.items[i] + "\n"

        empty_lines = ""
        if self.height - len(self.items) > 0:
            empty_lines += (self.height - len(self.items)) * "\n"

        return s + empty_lines

    def up(self):
        if self.pos > 0:
            self.pos -= 1
            if self.first_line_index > self.pos:
                self.first_line_index -= 1

    def down(self):
        if self.pos < len(self.items) - 1:
            self.pos += 1
            if self.get_last_line_index() < self.pos:
                self.first_line_index += 1
