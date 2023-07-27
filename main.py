
class Canvas:
    """
    Background for figures drawing
    """
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self, imagepath):
        """image creating"""
        pass


class Square:
    """
    Square where x, y are coordinates of left-upper point
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Drawing figure"""
        pass


class Rectangle:
    """
    Rectangle where x, y upper-left point
    """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """drawing figure"""
        pass
