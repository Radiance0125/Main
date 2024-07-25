import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.title("testing")
root.geometry("400x400")


#1st approach
photo = tk.PhotoImage(file = "assets/image.png")

#2nd approach
photo2 = Image.open("assets/image.png")
resized_image = photo2.resize((400, 400), Image.BILINEAR)
converted_image = ImageTk.PhotoImage(resized_image)


label = tk.Label(root, image = converted_image, bg = "white", fg = "black")


label.pack()
root.mainloop()