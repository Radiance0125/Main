import tkinter as tk
import random
import time

record = ""

code = []

tries = 0

def lose(tries):
    global code

    root = tk.Tk()
    root.title("game")
    root.geometry("400x250")
    root.config(background = "firebrick2")

    def retry():
        root.destroy()
        main()
    
    def quit():
        exit()

    x = ""
    for i in code:
        x += i

    tk.Message(root, text = "you lost!", font = ("arial", 20), background = "firebrick2").place(x = 200, y = 75, anchor = tk.CENTER)
    tk.Message(root, text = f"the code was {x}", font = ("arial", 10), background = "firebrick2", width = 200).place(x = 200, y = 115, anchor = tk.CENTER)
    tk.Message(root, text = record, font = ("arial", 10), background = "firebrick2", width = 70).place(x = 37, y = 14, anchor = tk.CENTER)
    tk.Button(root, text = "retry", font = ('arial', 14,), activebackground = "RoyalBlue1", bg = "RoyalBlue1", width = 7, 
              command = retry).place(x = 135, y = 160, anchor = tk.CENTER)
    tk.Button(root, text = "quit", font = ('arial', 14,), activebackground = "orange", bg = "orange", width = 7, 
              command = quit).place(x = 265, y = 160, anchor = tk.CENTER)

    root.mainloop()

def win(tries):
    global code, record

    root = tk.Tk()
    root.title("game")
    root.geometry("400x250")
    root.config(background = "lawn green")

    if record == "" or int(record)>tries:
        record = f"record: {tries} attempts"

    def retry():
        root.destroy()
        main()
    
    def quit():
        exit()

    tk.Message(root, text = "you won!", font = ("arial", 20), background = "lawn green").place(x = 200, y = 100, anchor = tk.CENTER)
    tk.Message(root, text = record, font = ("arial", 10), background = "lawn green", width = 70).place(x = 37, y = 14, anchor = tk.CENTER)
    tk.Button(root, text = "retry", font = ('arial', 14,), activebackground = "RoyalBlue1", bg = "RoyalBlue1", width = 7, 
              command = retry).place(x = 135, y = 160, anchor = tk.CENTER)
    tk.Button(root, text = "quit", font = ('arial', 14,), activebackground = "orange", bg = "orange", width = 7, 
              command = quit).place(x = 265, y = 160, anchor = tk.CENTER)

    root.mainloop()


def main():

    global code, slots, nextslot, occurrences, occurrences_copy, chances, history, feedback, tries

    tries = 0
    
    code = []
    slots = []
    nextslot = 0
    chances = 10
    feedback = {"green": 0, "yellow": 0, "red": 0}
    occurrences = {str(i): 0 for i in range(10)}
    history = {str(i): "" for i in range(1, 11)}
    
    while len(code) != 4:
        x = ""
        while not x.isdigit() or  x in code:
            x = str(random.randint(0,9))
        code.append(x)

    print (code)
    
    for i in code:
        occurrences[i] += 1
    
    occurrences_copy = occurrences.copy()

    root = tk.Tk()
    root.title("game")
    root.geometry("500x210")

    canvas = tk.Canvas(root, width=150, height=210)
    canvas.place(x = 200, y = 0)

    canvas.create_line(3, 1, 3, 209, width = 2)
    canvas.create_line(147, 1, 147, 209, width = 2)

    records = tk.Text(root, font = ("arial", 13), state = "normal")
    records.place(x = 350, y = 7, width = 145, height = 194)

    records.configure(state="normal")
    records.insert(tk.END, "1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n10.")
    records.configure(state="disabled")

    for i in range(1, 11):
        slots.append(canvas.create_oval(25, i*19-3, 35, i*19+7, fill = "white"))
        slots.append(canvas.create_oval(55, i*19-3, 65, i*19+7, fill = "white"))
        slots.append(canvas.create_oval(85, i*19-3, 95, i*19+7, fill = "white"))
        slots.append(canvas.create_oval(115, i*19-3, 125, i*19+7, fill = "white"))


    def add_to_display(value):
        display.configure(state="normal")
        display.insert(tk.END, value)
        display.configure(state="readonly")

    def clear_display():
        display.configure(state="normal")
        display.delete(0, tk.END)
        display.configure(state="readonly")

    def add_to_history():
        records.configure(state="normal")
        records.delete("1.0","end")
        records.insert(tk.END, f"1.{history.get('1')}\n2.{history.get('2')}\n3.{history.get('3')}\n4.{history.get('4')}\n5.{history.get('5')}\n6.{history.get('6')}\n7.{history.get('7')}\n8.{history.get('8')}\n9.{history.get('9')}\n10.{history.get('10')}")
        records.configure(state="disabled")

    def change_color(color):
        global nextslot
        canvas.itemconfig(slots[nextslot], fill=color)
        nextslot += 1

    def submit_code():

        global tries
                
        feedback["green"] = 0
        feedback["yellow"] = 0
        feedback["red"] = 0
    
        global nextslot, chances, history
        attempt_num = display.get()

        if not attempt_num.isdigit() or len(attempt_num) != 4:
            display.configure(state="normal")
            display.delete(0, tk.END)
            display.configure(state="readonly")
            return
        else:
            tries += 1

        attempt_list = [str(i) for i in attempt_num]
        digit_counts = occurrences.copy()
        
        for i in range(4):
            if attempt_list[i] == code[i]:
                feedback["green"] += 1
                digit_counts[attempt_list[i]] -= 1
        
        for i in range(4):
            if attempt_list[i] != code[i] and attempt_list[i] in code:
                if digit_counts[attempt_list[i]] > 0:
                    feedback["yellow"] += 1
                    digit_counts[attempt_list[i]] -= 1
                else:
                    feedback["red"] += 1
            elif attempt_list[i] != code[i]:
                feedback["red"] += 1

        x = 11 - chances
        
        if attempt_list == code:
            #root.destroy()
            win(tries)

        if len(attempt_list) != 4:
            print("response invalid")
        else:
            chances -= 1

            history[f"{x}"] = attempt_num        
            add_to_history()

            for i in ("green", "yellow", "red"):
                for j in range(feedback[i]):
                    change_color(i)

        display.configure(state="normal")
        display.delete(0, tk.END)
        display.configure(state="readonly")

        if chances == 0:
            #root.destroy()
            lose(tries)


    display = tk.Entry(root, font = ("arial", 20), state = "readonly")
    display.place(x = 10, y = 3, width = 182)

    buttonframe = tk.Frame(root, width = 198, height = 168)
    buttonframe.columnconfigure(0, weight = 1)
    buttonframe.columnconfigure(1, weight = 1)
    buttonframe.columnconfigure(2, weight = 1)
    for i in range(4):
        buttonframe.rowconfigure(i, weight = 1)

    btn1 = tk.Button(buttonframe, text = "1", font = ("arial", 16), command = lambda x = "1" : add_to_display(x))
    btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

    btn2 = tk.Button(buttonframe, text = "2", font = ("arial", 16), command = lambda x = "2" : add_to_display(x))
    btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E, ipadx = 18)

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
    clrbtn.grid(row = 3, column = 0, sticky = "snew", ipadx = 2)

    btn0 = tk.Button(buttonframe, text = "0", font = ("arial", 16), command = lambda x = "0" : add_to_display(x))
    btn0.grid(row = 3, column = 1, sticky = tk.W + tk.E)

    entrbtn = tk.Button(buttonframe, text = "enter", font = ("arial", 16), command = lambda : submit_code())
    entrbtn.grid(row = 3, column = 2, sticky = "snew")

    buttonframe.place(x = 0, y = 42)
    
    root.mainloop()


main()