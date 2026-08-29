import tkinter as tk


class TinyScreen(tk.Tk):
    def __init__(self, width=200, height=200, block_size=6):
        super().__init__()
        self.title("20x20 Screen")
        self.resizable(False, False)
        self.width = width
        self.height = height
        self.block_size = block_size

        # Canvas exactly width x height pixels
        self.canvas = tk.Canvas(self, width=width, height=height, highlightthickness=0)
        self.canvas.pack()

        # Start block in center
        start_x = (width - block_size) // 2
        start_y = (height - block_size) // 2
        self.block = self.canvas.create_rectangle(start_x, start_y,
                                                  start_x + block_size, start_y + block_size,
                                                  fill="black")

        # Bind arrow keys
        self.bind_all("<Up>", lambda e: self.move(0, -1))
        self.bind_all("<Down>", lambda e: self.move(0, 1))
        self.bind_all("<Left>", lambda e: self.move(-1, 0))
        self.bind_all("<Right>", lambda e: self.move(1, 0))

    def move(self, dx, dy):
        x1, y1, x2, y2 = self.canvas.coords(self.block)
        # Compute new coords clamped to canvas
        new_x1 = max(0, min(self.width - self.block_size, int(x1 + dx)))
        new_y1 = max(0, min(self.height - self.block_size, int(y1 + dy)))
        self.canvas.coords(self.block, new_x1, new_y1, new_x1 + self.block_size, new_y1 + self.block_size)


if __name__ == "__main__":
    app = TinyScreen()
    app.mainloop()
