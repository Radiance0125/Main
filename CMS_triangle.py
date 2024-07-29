import tkinter as tk 

known_value1 = ""
known_value2 = ""

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
    buttonframe.rowconfigure(0, weight = 1)
    buttonframe.rowconfigure(1, weight = 1)
    buttonframe.rowconfigure(2, weight = 1)
    buttonframe.rowconfigure(3, weight = 1)

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

def firstknownchange(value, root):
    global known_value1
    known_value1 = value
    root.destroy()

def secondknownchange(value, root):
    global known_value2
    known_value2 = value

def firstchoice():

    global known_value1

    root = tk.Tk()

    root.geometry("500x250")

    root.title("CMS calculator")

    label = tk.Label(root, text = "which of the CMS triangle's values are known?", font = ("arial", 14))
    label.pack(pady = 10)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)
    buttonframe.columnconfigure(2, weight = 1)
    buttonframe.columnconfigure(3, weight = 1)

    btn_C = tk.Button(buttonframe, text = "Cost price", font = ("arial", 14), command = lambda x = "C" : firstknownchange(x, root))
    btn_C.grid(row = 0, column = 0, sticky = tk.W + tk.E, padx = 5)

    btn_M = tk.Button(buttonframe, text = "Marked price", font = ("arial", 14), command = lambda x = "M" : firstknownchange(x, root))
    btn_M.grid(row = 0, column = 1, sticky = tk.W + tk.E, padx = 5)

    btn_S = tk.Button(buttonframe, text = "Selling price", font = ("arial", 14), command = lambda x = "S" : firstknownchange(x, root))
    btn_S.grid(row = 0, column = 2, sticky = tk.W + tk.E, padx = 5)

    btn_none = tk.Button(buttonframe, text = "none are known", font = ("arial", 14), command = lambda x = "none" : firstknownchange(x, root))
    btn_none.grid(row = 0, column = 3, sticky = tk.W + tk.E, padx = 5)

    buttonframe.pack(fill = "x", pady = 30)

    root.mainloop()

firstchoice()