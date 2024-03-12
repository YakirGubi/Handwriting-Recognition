import tkinter as tk
from functools import reduce
from tkinter import Canvas, PhotoImage
from PIL import Image, ImageDraw

imageSize = 28
imagePerCanvasSize = 10
canvasSize = imageSize * imagePerCanvasSize

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        # Set the initial size of the canvas
        self.canvas_width = canvasSize
        self.canvas_height = canvasSize

        # Create a canvas for drawing
        self.canvas = Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()

        # Create a PIL Image and ImageDraw object for drawing
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "black")
        self.draw = ImageDraw.Draw(self.image)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def paint(self, event):
        # Draw on the canvas and the PIL Image
        size = 12
        x1, y1 = (event.x - size), (event.y - size)
        x2, y2 = (event.x + size), (event.y + size)
        self.canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")
        self.draw.line([x1, y1, x2, y2], fill="white", width=size)

    def reset(self, event):
        # Save the drawn image
        self.image.save("drawn_frame.png")

    def comprecate(self, pixels):
        for i in range(len(pixels)):
            pixels[i] = reduce(lambda x, y: x + y, pixels[i])/3
        return pixels





def returnImage():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

    pixels = app.comprecate(list(app.image.getdata()))
    list2D = []
    temp_list = []

    for i, data in enumerate(pixels):
        temp_list.append(data)
        if (i+1) % 280 == 0:
            list2D.append(temp_list)
            temp_list = []


    new_shape = (28, 28)

    # Calculate the block size
    block_size = 10


    # Function to calculate the average of a block
    def average_block(block):
        total = sum(sum(block, []))
        return total / (block_size * block_size)


    # Initialize the new array
    averaged_array = [[0.0] * new_shape[1] for _ in range(new_shape[0])]

    # Iterate through the blocks and calculate the average
    for i in range(0, new_shape[0] * block_size, block_size):
        for j in range(0, new_shape[1] * block_size, block_size):
            block = [row[j:j + block_size] for row in list2D[i:i + block_size]]
            averaged_array[i // block_size][j // block_size] = average_block(block)

    return averaged_array