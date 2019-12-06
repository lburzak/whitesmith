from view import View


class ListView(View):
    items: [str]
    pos: int = 0

    def __init__(self, items: [str]):
        self.items = items

    def render(self) -> str:
        s = ""

        for i in range(0, len(self.items)):
            if self.pos == i:
                s += "> "
            else:
                s += "  "
            s += self.items[i] + "\n"

        return s

    def up(self):
        if self.pos > 0:
            self.pos -= 1

    def down(self):
        if self.pos < len(self.items) - 1:
            self.pos += 1
