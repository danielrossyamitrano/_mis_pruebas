from pygame import display


class Renderer:

    @classmethod
    def init(cls, size):
        return display.set_mode(size)
