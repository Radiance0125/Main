import tkinter as tk 

root = tk.Tk()

root.geometry("500x500")

root.title("my first gui")

label = tk.Label(root, text = "hello world", font = ("arial", 18))
label.pack(padx = 20, pady = 20)

textbox = tk.Text(root, height = 3, font = ("arial", 16))
textbox.pack(padx = 10, pady = 10)

button = tk.Button(root, text = "click me!", font = ("arial", 18))
button.pack(padx = 10, pady = 10)

anotherbtn = tk.Button(root, text = "test")
anotherbtn.place (x = 200, y = 300, height = 100, width = 100)


root.mainloop()