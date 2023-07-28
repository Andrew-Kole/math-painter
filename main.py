from canvas import Canvas
from shapes import Square, Rectangle

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
