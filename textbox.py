import tkinter as tk
root = tk.Tk()
root.title("testing")
root.geometry("400x200")

label = tk.Label(root, text = "Testing", bg = "white", fg = "black")

label.pack()
root.mainloop()