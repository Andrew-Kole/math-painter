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
