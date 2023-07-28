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
        canvas.data[self.x : self.x + self.side, self.y : self.y + self.side] = self.color


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
        canvas.data[self.x : self.x + self.height, self.y : self.y + self.width] = self.color
