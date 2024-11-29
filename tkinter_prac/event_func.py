import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry("600x500")
window.title("event binding")

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = "a button")
btn.pack()


#run
window.mainloop()