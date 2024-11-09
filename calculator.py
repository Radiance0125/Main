import tkinter as tk 

result = None

formula = "didn't change"

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
        global formula
        formula = display.get()
        root.destroy()

    root = tk.Tk()

    root.geometry("600x394")

    root.title("calculator")

    display = tk.Entry(root, font = ("arial", 20), state = "readonly", width = 39)
    display.pack(padx = 3, pady = 3)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)
    buttonframe.columnconfigure(2, weight = 1)
    buttonframe.columnconfigure(3, weight = 1)
    buttonframe.rowconfigure(0, weight = 1)
    buttonframe.rowconfigure(1, weight = 1)
    buttonframe.rowconfigure(2, weight = 1)
    buttonframe.rowconfigure(3, weight = 1)

    btn1 = tk.Button(buttonframe, height = 2, text = "  1  ", font = ("arial", 20), command = lambda x = "1" : add_to_display(x))
    btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E + tk.N + tk.S)

    btn2 = tk.Button(buttonframe, height = 2, text = "  2  ", font = ("arial", 20), command = lambda x = "2" : add_to_display(x))
    btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E + tk.N + tk.S)

    btn3 = tk.Button(buttonframe, height = 2, text = "  3  ", font = ("arial", 20), command = lambda x = "3" : add_to_display(x))
    btn3.grid(row = 0, column = 2, sticky = tk.W + tk.E + tk.N + tk.S)

    btn4 = tk.Button(buttonframe, height = 2, text = "  4  ", font = ("arial", 20), command = lambda x = "4" : add_to_display(x))
    btn4.grid(row = 1, column = 0, sticky = tk.W + tk.E + tk.N + tk.S)

    btn5 = tk.Button(buttonframe, height = 2, text = "  5  ", font = ("arial", 20), command = lambda x = "5" : add_to_display(x))
    btn5.grid(row = 1, column = 1, sticky = tk.W + tk.E + tk.N + tk.S)

    btn6 = tk.Button(buttonframe, height = 2, text = "  6  ", font = ("arial", 20), command = lambda x = "6" : add_to_display(x))
    btn6.grid(row = 1, column = 2, sticky = tk.W + tk.E + tk.N + tk.S)

    btn7 = tk.Button(buttonframe, height = 2, text = "  7  ", font = ("arial", 20), command = lambda x = "7" : add_to_display(x))
    btn7.grid(row = 2, column = 0, sticky = tk.W + tk.E + tk.N + tk.S)

    btn8 = tk.Button(buttonframe, height = 2, text = "  8  ", font = ("arial", 20), command = lambda x = "8" : add_to_display(x))
    btn8.grid(row = 2, column = 1, sticky = tk.W + tk.E + tk.N + tk.S)

    btn9 = tk.Button(buttonframe, height = 2, text = "  9  ", font = ("arial", 20), command = lambda x = "9" : add_to_display(x))
    btn9.grid(row = 2, column = 2, sticky = tk.W + tk.E + tk.N + tk.S)

    clrbtn = tk.Button(buttonframe, height = 2, text = "clear", font = ("arial", 20), command = clear_display)
    clrbtn.grid(row = 3, column = 0, sticky = tk.W + tk.E + tk.N + tk.S)

    btn0 = tk.Button(buttonframe, height = 2, text = "  0  ", font = ("arial", 20), command = lambda x = "0" : add_to_display(x))
    btn0.grid(row = 3, column = 1, sticky = tk.W + tk.E + tk.N + tk.S)

    entrbtn = tk.Button(buttonframe, height = 2, text = "enter", font = ("arial", 20), command = lambda : submit_code())
    entrbtn.grid(row = 3, column = 2, sticky = tk.W + tk.E + tk.N + tk.S)

    #functions
    addbtn = tk.Button(buttonframe, height = 2, text = "  +  ", font = ("arial", 20), command = lambda x = "+" : add_to_display(x))
    addbtn.grid(row = 0, column = 3, sticky = tk.W + tk.E + tk.N + tk.S)

    subtractbtn = tk.Button(buttonframe, height = 2, text = "  -  ", font = ("arial", 20), command = lambda x = "-" : add_to_display(x))
    subtractbtn.grid(row = 1, column = 3, sticky = tk.W + tk.E + tk.N + tk.S)

    multiplybtn = tk.Button(buttonframe, height = 2, text = "  x  ", font = ("arial", 20), command = lambda x = "x" : add_to_display(x))
    multiplybtn.grid(row = 2, column = 3, sticky = tk.W + tk.E + tk.N + tk.S)

    dividebtn = tk.Button(buttonframe, height = 2, text = "  ÷  ", font = ("arial", 20), command = lambda x = "÷" : add_to_display(x))
    dividebtn.grid(row = 3, column = 3, sticky = tk.W + tk.E + tk.N + tk.S)

    buttonframe.pack(fill = "both")

    root.mainloop()

def calculate():
    x = ""
    for i in calculation:
        if i == "x":
            x += "*"
        elif i == "÷":
            x += "/"
        else:
            x += i
        
    print(eval(x))

def check():

    if calculation[0] == "+" or calculation[0] == "-" or calculation[0] == "÷" or calculation[0] == "x":
        print("input error")
        exit()

    for i in range(len(calculation)):
        if calculation[i] == "+" or calculation[i] == "-" or calculation[i] == "÷" or calculation[i] == "x":
            try:
                int(float(calculation[i-1]))
            except:
                print("input error")
                exit()

            try:
                int(float(calculation[i+1]))
            except:
                print("input error")
                exit()


keypad()
calculation = [i for i in formula]
check()

print(formula)
calculate()