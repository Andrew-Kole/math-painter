import numpy as np
from PIL import Image


class Canvas:
    """
    Background for figures drawing
    """
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Creating a numpy array of zeros
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        # Painting canvas in given color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converting a numpy array in image and saving it."""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
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


# Calling methods
# Creating canvas for drawing
canvas = Canvas(width=400, height=500, color=(255, 0, 0))
# Creating rectangle
rectangle = Rectangle(x=10, y=10, width=200, height=80, color=(0, 255, 0))
# Drawing rectangle on canvas
rectangle.draw(canvas)
# Creating square
square = Square(x=90, y=10, side=40, color=(0, 0, 255))
# Drawing square
square.draw(canvas)
# creating a .png file
canvas.make("output/canvas.png")
