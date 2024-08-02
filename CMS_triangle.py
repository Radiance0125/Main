import tkinter as tk 

firstcount = 0

known_values = []
known_percentages = []

knownvalue1 = []
knownvalue2 = []

knownpercentage1 = []
knownpercentage2 = []
knownpercentage3 = []

def fail():
    root  = tk.Tk()

    root.geometry("300x150")

    root.title("CMS calculator")
               
    label = tk.Label(root, text = "sorry, but the information is \n insufficient for this calculation", font = ("arial", 15))
    label.pack(padx = 10, pady = 40)

    root.mainloop()

    exit()

def addknownvalue(value, root):
    global known_values
    known_values.append(value)
    root.destroy()

def firstvaluechoice():

    global known_values

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

    btn_C = tk.Button(buttonframe, text = "Cost price", font = ("arial", 14), command = lambda x = "C" : addknownvalue(x, root))
    btn_C.grid(row = 0, column = 0, sticky = tk.W + tk.E, padx = 5)

    btn_M = tk.Button(buttonframe, text = "Marked price", font = ("arial", 14), command = lambda x = "M" : addknownvalue(x, root))
    btn_M.grid(row = 0, column = 1, sticky = tk.W + tk.E, padx = 5)

    btn_S = tk.Button(buttonframe, text = "Selling price", font = ("arial", 14), command = lambda x = "S" : addknownvalue(x, root))
    btn_S.grid(row = 0, column = 2, sticky = tk.W + tk.E, padx = 5)

    btn_none = tk.Button(buttonframe, text = "none are known", font = ("arial", 14), command = lambda x = "none" : addknownvalue(x, root))
    btn_none.grid(row = 0, column = 3, sticky = tk.W + tk.E, padx = 5)

    buttonframe.pack(fill = "x", pady = 30)

    root.mainloop()

def secondvaluechoice(x):

    global known_values

    root = tk.Tk()

    root.geometry("500x250")

    root.title("CMS calculator")

    label = tk.Label(root, text = "which of the CMS triangle's other values are known?", font = ("arial", 14))
    label.pack(pady = 10)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)
    buttonframe.columnconfigure(2, weight = 1)

    column = 0

    if x != "C":
        btn_C = tk.Button(buttonframe, text = "Cost price", font = ("arial", 14), command = lambda x = "C" : addknownvalue(x, root))
        btn_C.grid(row = 0, column = column, sticky = tk.W + tk.E, padx = 5)
        column += 1

    if x != "M":
        btn_M = tk.Button(buttonframe, text = "Marked price", font = ("arial", 14), command = lambda x = "M" : addknownvalue(x, root))
        btn_M.grid(row = 0, column = column, sticky = tk.W + tk.E, padx = 5)
        column += 1

    if x != "S":
        btn_S = tk.Button(buttonframe, text = "Selling price", font = ("arial", 14), command = lambda x = "S" : addknownvalue(x, root))
        btn_S.grid(row = 0, column = column, sticky = tk.W + tk.E, padx = 5)
        column += 1

    btn_none = tk.Button(buttonframe, text = "no other are known", font = ("arial", 14), command = lambda x = "none" : addknownvalue(x, root))
    btn_none.grid(row = 0, column = column, sticky = tk.W + tk.E, padx = 5)

    buttonframe.pack(fill = "x", pady = 30)

    root.mainloop()

def findvalue (value, info):
    def add_to_display(value):
        display.configure(state="normal")
        display.insert(tk.END, value)
        display.configure(state="readonly")

    def clear_display():
        display.configure(state="normal")
        display.delete(0, tk.END)
        display.configure(state="readonly")
    
    def submit_code():
        if display.get() != "":
            code = display.get()
            info.append(int(code))
            root.destroy()

    root = tk.Tk()

    root.geometry("245x250")

    root.title("CMS calculator")

    if value == "C":
        label = tk.Label(root, text = "what is the cost price?", font = ("arial", 16))
    if value == "M":
        label = tk.Label(root, text = "what is the marked price?", font = ("arial", 16))
    if value == "S":
        label = tk.Label(root, text = "what is the selling price?", font = ("arial", 16))
    label.pack(pady = 10)

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
    clrbtn.place(x = 0, y =119, height = 39, width = 81)

    btn0 = tk.Button(buttonframe, text = "0", font = ("arial", 16), command = lambda x = "0" : add_to_display(x))
    btn0.grid(row = 3, column = 1, sticky = tk.W + tk.E)

    entrbtn = tk.Button(buttonframe, text = "enter", font = ("arial", 16), command = lambda : submit_code())
    entrbtn.place(x = 164, y = 119, height = 39, width = 81)

    buttonframe.pack(fill = "x")

    root.mainloop()

def addknownpercentage(value, root):
    global known_percentages
    known_percentages.append(value)
    root.destroy()

def insertknownpercentage(value, position, root):
    global known_percentages
    known_percentages.insert(position, value)
    root.destroy()

def firstpercentagechoice():

    global known_percentages

    root = tk.Tk()

    root.geometry("500x250")

    root.title("CMS calculator")

    label = tk.Label(root, text = "which of the conversions are known?", font = ("arial", 14))
    label.pack(pady = 10)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)
    buttonframe.columnconfigure(2, weight = 1)
    buttonframe.columnconfigure(3, weight = 1)
    buttonframe.columnconfigure(4, weight = 1)

    btn_discount = tk.Button(buttonframe, text = "Discount", font = ("arial", 14), command = lambda x = "discount" : addknownpercentage(x, root))
    btn_discount.grid(row = 0, column = 0, sticky = tk.W + tk.E, padx = 5)

    btn_markup = tk.Button(buttonframe, text = "Markup", font = ("arial", 14), command = lambda x = "markup" : addknownpercentage(x, root))
    btn_markup.grid(row = 0, column = 1, sticky = tk.W + tk.E, padx = 5)

    btn_profitloss = tk.Button(buttonframe, text = "Profit/loss", font = ("arial", 14), command = lambda x = "profit/loss" : addknownpercentage(x, root))
    btn_profitloss.grid(row = 0, column = 2, sticky = tk.W + tk.E, padx = 5)

    btn_none = tk.Button(buttonframe, text = "none are known", font = ("arial", 14), command = lambda x = "none" : addknownpercentage(x, root))
    btn_none.grid(row = 0, column = 3, sticky = tk.W + tk.E, padx = 5)

    btn_all = tk.Button(buttonframe, text = "all", font = ("arial", 14), command = lambda x = "all" : addknownpercentage(x, root))
    btn_all.grid(row = 0, column = 4, sticky = tk.W + tk.E, padx = 5)

    buttonframe.pack(fill = "x", pady = 30)

    root.mainloop()

def secondpercentagechoice(x):

    global known_percentages

    root = tk.Tk()

    root.geometry("500x250")

    root.title("CMS calculator")

    label = tk.Label(root, text = "which of the other conversions are known?", font = ("arial", 14))
    label.pack(pady = 10)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)
    buttonframe.columnconfigure(2, weight = 1)

    column = 0

    if x != "discount":
        btn_discount = tk.Button(buttonframe, text = "Discount", font = ("arial", 14), command = lambda x = "discount" : addknownpercentage(x, root))
        btn_discount.grid(row = 0, column = column, sticky = tk.W + tk.E, padx = 5)
        column += 1

    if x != "markup":
        btn_markup = tk.Button(buttonframe, text = "Markup", font = ("arial", 14), command = lambda x = "markup" : addknownpercentage(x, root))
        btn_markup.grid(row = 0, column = column, sticky = tk.W + tk.E, padx = 5)
        column += 1

    if x != "profit/loss":
        btn_profitloss = tk.Button(buttonframe, text = "Profit/loss", font = ("arial", 14), command = lambda x = "profit/loss" : addknownpercentage(x, root))
        btn_profitloss.grid(row = 0, column = column, sticky = tk.W + tk.E, padx = 5)
        column += 1

    btn_none = tk.Button(buttonframe, text = "none are known", font = ("arial", 14), command = lambda x = "none" : addknownpercentage(x, root))
    btn_none.grid(row = 0, column = column, sticky = tk.W + tk.E, padx = 5)

    buttonframe.pack(fill = "x", pady = 30)

    root.mainloop()

def profitlossoption():

    position = known_percentages.index("profit/loss")

    known_percentages.remove("profit/loss")

    root = tk.Tk()

    root.geometry("300x100")

    root.title("CMS calculator")

    label = tk.Label(root, font = ("arial", 15), text = "is there a profit or a loss?")
    label.pack(pady = 10)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)

    btn_profit = tk.Button(buttonframe, text = "profit", font = ("arial", 15), command = lambda x = "profit": insertknownpercentage(x, position, root))
    btn_profit.grid(row = 0, column = 0, sticky = tk.W + tk.E, padx = 3)

    btn_profit = tk.Button(buttonframe, text = "loss", font = ("arial", 15), command = lambda x = "loss": insertknownpercentage(x, position, root))
    btn_profit.grid(row = 0, column = 1, sticky = tk.W + tk.E, padx = 3)
    
    buttonframe.pack(fill = "x")

    root.mainloop()

def findvalue (value, info):
    def add_to_display(value):
        display.configure(state="normal")
        display.insert(tk.END, value)
        display.configure(state="readonly")

    def clear_display():
        display.configure(state="normal")
        display.delete(0, tk.END)
        display.configure(state="readonly")
    
    def submit_code():
        if display.get() != "":
            code = display.get()
            info.append(int(code))
            root.destroy()

    root = tk.Tk()

    root.geometry("245x250")

    root.title("CMS calculator")

    if value == "C":
        label = tk.Label(root, text = "what is the cost price?", font = ("arial", 16))
    if value == "M":
        label = tk.Label(root, text = "what is the marked price?", font = ("arial", 16))
    if value == "S":
        label = tk.Label(root, text = "what is the selling price?", font = ("arial", 16))
    label.pack(pady = 10)

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
    clrbtn.place(x = 0, y =119, height = 39, width = 81)

    btn0 = tk.Button(buttonframe, text = "0", font = ("arial", 16), command = lambda x = "0" : add_to_display(x))
    btn0.grid(row = 3, column = 1, sticky = tk.W + tk.E)

    entrbtn = tk.Button(buttonframe, text = "enter", font = ("arial", 16), command = lambda : submit_code())
    entrbtn.place(x = 164, y = 119, height = 39, width = 81)

    buttonframe.pack(fill = "x")

    root.mainloop()

def findnumber(value, info, prevpage):

    prevpage.destroy()
    
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
        info.append(int(code))
        info.append("number")
        root.destroy()

    root = tk.Tk()

    root.geometry("200x260")

    root.title("CMS calculator")

    label = tk.Label(root, text = "what is the " + value + "?", font = ("arial", 14))
    label.pack()

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

def findpercentage(value, info, prevpage):

    prevpage.destroy()

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
        info.append(int(code))
        info.append("percentage")
        root.destroy()

    root = tk.Tk()

    root.geometry("200x260")

    root.title("CMS calculator")

    label = tk.Label(root, text = "what is the " + value + "%?", font = ("arial", 14))
    label.pack()

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

def numberorpercentage(value, info):

    root = tk.Tk()

    root.geometry("400x200")

    root.title("CMS calculator")

    label = tk.Label(root, text = "is the known " + value + "\nin the form of a percentage or a number?", font = ("arial", 14))
    label.pack()

    buttonframe = tk.Frame(root)

    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)

    btn_num = tk.Button(buttonframe, text = "number", font = ("arial", 15), command = lambda x = value : findnumber(x, info, root))
    btn_num.grid(row = 0, column  = 0, sticky = tk.W + tk.E, pady = 3)

    btn_perc = tk.Button(buttonframe, text = "percentage", font = ("arial", 15), command = lambda x = value : findpercentage(x, info, root))
    btn_perc.grid(row = 0, column  = 1, sticky = tk.W + tk.E, pady = 3)

    buttonframe.pack(fill = "x")

    root.mainloop()



#see if any of the values are known
firstvaluechoice()

if known_values [0] == "none":
    fail()

knownvalue1 = [known_values[0]]

#see if there is a second known value, if there is a first one
if known_values[0] != "none":
    if known_values[0] == "C":
        secondvaluechoice("C")
    if known_values[0] == "M":
        secondvaluechoice("M")
    if known_values[0] == "S":
        secondvaluechoice("S")
    knownvalue2 = [known_values[1]]

#find the values of the 1-2 variables that we know of
if known_values[0] != "none":
    findvalue(knownvalue1[0], knownvalue1)
    if known_values[1] != "none":
        findvalue(knownvalue2[0], knownvalue2)

#see how many percentages are known
firstpercentagechoice()

if known_percentages[0] == "none":
    fail()

#see if any other ones are known
if known_percentages[0] == "all":
    known_percentages.pop()
    known_percentages.append("discount")
    known_percentages.append("markup")
    known_percentages.append("profit/loss")
elif known_percentages[0] != "none":
    secondpercentagechoice(known_percentages[0])
    known_percentages.append("none")

#clarify if it's profit or loss if its known
if "profit/loss" in known_percentages:
    profitlossoption()

print(known_percentages)

#seperating the percentages into their individual lists for later use
knownpercentage1.append(known_percentages[0])
numberorpercentage(knownpercentage1[0], knownpercentage1)
if known_percentages[1] != "none":
    knownpercentage2.append(known_percentages[1])
    numberorpercentage(knownpercentage2[0], knownpercentage2)
    if known_percentages[2] != "none":
        knownpercentage3.append(known_percentages[2])
        numberorpercentage(knownpercentage3[0], knownpercentage3)

if knownvalue2 == "none" and knownpercentage2 == "none":
    fail()

#the input part has ended

dictofcomponents = {
    "S" : "none", 
    "M" : "none", 
    "C" : "none", 
    "markup" : "none", 
    "discount" : "none", 
    "profit" : "none", 
    "loss" : "none", 
    "markup%" : "none", 
    "discount%" : "none", 
    "profit%" : "none", 
    "loss%" : "none"
}

def changedict(object, value):
    dictofcomponents.update({object : value})

changedict(knownvalue1[0], knownvalue1[1])
if knownvalue2[0] == "none":
    pass
else:
    changedict(knownvalue2[0], knownvalue2[1])

for i in (knownpercentage1, knownpercentage2, knownpercentage3):

    if i == "none":
        pass
    else:
        if i[0] == "profit":
            dictofcomponents.pop("loss")
            dictofcomponents.pop("loss%")
        if i[0] == "loss":
            dictofcomponents.pop("profit")
            dictofcomponents.pop("profit%")

        x = ""

        if i[2] == "percentage":
            x = "%"
        
    changedict(i[0] + x, i[1])

