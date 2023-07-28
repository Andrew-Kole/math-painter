from canvas import Canvas
from shapes import Square, Rectangle

# Canvas settings
canvas_width = int(input("Enter the width of canvas: "))
canvas_height = int(input("Enter the height of canvas: "))
colors = {"black": (0, 0, 0), "white": (255, 255, 255),
          "red": (255, 0, 0), "green": (0, 255, 0),
          "blue": (0, 0, 255)}
canvas_color = input("Enter a color of canvas(black, white, red, green or blue): ")

# Creating canvas for drawing
canvas = Canvas(width=canvas_height, height=canvas_width, color=colors[canvas_color])

while True:
    action = input("What would you like to draw rectangle or square? If you want to finish type quit.")
    if action == "rectangle":
        # Rectangle settings
        x = int(input("Enter x coordinate of upper left corner: "))
        y = int(input("Enter y coordinate of upper left corner: "))
        width = int(input("Enter width of rectangle: "))
        height = int(input("Enter height of rectangle: "))
        color = input("Enter color of rectangle(black, white, red, green or blue): ")
        # Creating rectangle
        rectangle = Rectangle(x=y, y=x, width=width, height=height, color=colors[color])
        # Drawing rectangle on canvas
        rectangle.draw(canvas)
    elif action == "square":
        # Square settings
        x = int(input("Enter x coordinate of upper left corner: "))
        y = int(input("Enter y coordinate of upper left corner: "))
        side = int(input("Enter side length: "))
        color = input("Enter color of rectangle(black, white, red, green or blue): ")
        # Creating square
        square = Square(x=y, y=x, side=side, color=colors[color])
        # Drawing square
        square.draw(canvas)
    elif action == "quit":
        break
    else:
        print("Unknown command.")

# creating a .png file
canvas.make("output/canvas.png")
