import tkinter as tk 

def keypad():
    root = tk.Tk()

    root.geometry("600x600")

    root.title("my first gui")

    label = tk.Label(root, text = "keypad", font = ("arial", 18))
    label.pack(padx = 20, pady = 20)

    textbox = tk.Text(root, height = 3, font = ("arial", 16))
    textbox.pack(padx = 10, pady = 10)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)
    buttonframe.columnconfigure(2, weight = 1)

    btn1 = tk.Button(buttonframe, text = "1", font = ("arial", 18))
    btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

    btn2 = tk.Button(buttonframe, text = "2", font = ("arial", 18))
    btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

    btn3 = tk.Button(buttonframe, text = "3", font = ("arial", 18))
    btn3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

    btn4 = tk.Button(buttonframe, text = "4", font = ("arial", 18))
    btn4.grid(row = 1, column = 0, sticky = tk.W + tk.E)

    btn5 = tk.Button(buttonframe, text = "5", font = ("arial", 18))
    btn5.grid(row = 1, column = 1, sticky = tk.W + tk.E)

    btn6 = tk.Button(buttonframe, text = "6", font = ("arial", 18))
    btn6.grid(row = 1, column = 2, sticky = tk.W + tk.E)

    btn7 = tk.Button(buttonframe, text = "7", font = ("arial", 18))
    btn7.grid(row = 2, column = 0, sticky = tk.W + tk.E)

    btn8 = tk.Button(buttonframe, text = "8", font = ("arial", 18))
    btn8.grid(row = 2, column = 1, sticky = tk.W + tk.E)

    btn9 = tk.Button(buttonframe, text = "9", font = ("arial", 18))
    btn9.grid(row = 2, column = 2, sticky = tk.W + tk.E)

    btn0 = tk.Button(buttonframe, text = "0", font = ("arial", 18))
    btn0.grid(row = 3, column = 1, sticky = tk.W + tk.E)

    buttonframe.pack(fill = "x")

    root.mainloop()

