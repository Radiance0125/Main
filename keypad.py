import tkinter as tk 

def keypad():

    def add_to_display(value):
        display.configure(state="normal")
        display.insert(tk.END, value)
        display.configure(state="readonly")

    def clear_display():
        display.configure(state="normal")
        display.delete(0, tk.END)
        display.configure(state="readonly")
    
    def submit_code():
        code = display.get()
        print(code)



    root = tk.Tk()

    root.geometry("200x210")

    root.title("Keypad")

    display = tk.Entry(root, font = ("arial", 20), state = "readonly")
    display.pack(padx = 10, pady = 3)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)
    buttonframe.columnconfigure(2, weight = 1)
    for i in range(4):
        buttonframe.rowconfigure(i, weight = 1)

    btn1 = tk.Button(buttonframe, text = "1", font = ("arial", 16), command = lambda x = "1" : add_to_display(x))
    btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

    btn2 = tk.Button(buttonframe, text = "2", font = ("arial", 16), command = lambda x = "2" : add_to_display(x))
    btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

    btn3 = tk.Button(buttonframe, text = "3", font = ("arial", 16), command = lambda x = "3" : add_to_display(x))
    btn3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

    btn4 = tk.Button(buttonframe, text = "4", font = ("arial", 16), command = lambda x = "4" : add_to_display(x))
    btn4.grid(row = 1, column = 0, sticky = tk.W + tk.E)

    btn5 = tk.Button(buttonframe, text = "5", font = ("arial", 16), command = lambda x = "5" : add_to_display(x))
    btn5.grid(row = 1, column = 1, sticky = tk.W + tk.E)

    btn6 = tk.Button(buttonframe, text = "6", font = ("arial", 16), command = lambda x = "6" : add_to_display(x))
    btn6.grid(row = 1, column = 2, sticky = tk.W + tk.E)

    btn7 = tk.Button(buttonframe, text = "7", font = ("arial", 16), command = lambda x = "7" : add_to_display(x))
    btn7.grid(row = 2, column = 0, sticky = tk.W + tk.E)

    btn8 = tk.Button(buttonframe, text = "8", font = ("arial", 16), command = lambda x = "8" : add_to_display(x))
    btn8.grid(row = 2, column = 1, sticky = tk.W + tk.E)

    btn9 = tk.Button(buttonframe, text = "9", font = ("arial", 16), command = lambda x = "9" : add_to_display(x))
    btn9.grid(row = 2, column = 2, sticky = tk.W + tk.E)

    clrbtn = tk.Button(buttonframe, text = "clear", font = ("arial", 16), command = clear_display)
    clrbtn.place(x = 0, y = 126, height = 42, width = 66)

    btn0 = tk.Button(buttonframe, text = "0", font = ("arial", 16), command = lambda x = "0" : add_to_display(x))
    btn0.grid(row = 3, column = 1, sticky = tk.W + tk.E)

    entrbtn = tk.Button(buttonframe, text = "enter", font = ("arial", 16), command = lambda : submit_code())
    entrbtn.place(x = 134, y = 126, height = 42, width = 66)

    buttonframe.pack(fill = "x")

    root.mainloop()

keypad()