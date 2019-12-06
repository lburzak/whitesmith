from readchar import key


class View:
    def render(self) -> str:
        pass


class KeyListener:
    def on_key(self, k: key):
        pass
