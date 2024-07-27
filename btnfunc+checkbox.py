import tkinter as tk 
from tkinter import messagebox

class mygui:

    def __init__(self):
        
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu (self.menubar, tearoff = 0)
        self.filemenu.add_command(label = "close", command = self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "close without asking", command = exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff = 0)
        self.actionmenu.add_command(label = "show message", command = self.show_message)

        self.menubar.add_cascade(menu = self.filemenu, label = "file")
        self.menubar.add_cascade(menu = self.actionmenu, label = "action")

        self.root.config(menu = self.menubar)

        self.label = tk.Label (self.root, text = "your message", font = ("arial", 18))
        self.label.pack (padx = 10, pady = 10)

        self.textbox = tk.Text (self.root, height = 5, font = ("arial", 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack (padx = 10, pady = 10)

        self.check_state = tk.IntVar ()

        self.check = tk.Checkbutton (self.root, text = "show message box", font = ("arial", 16), variable = self.check_state)
        self.check.pack (padx = 10, pady = 10)
        
        self.button = tk.Button (self.root, text = "show message", font = ("arial", 18), command = self.show_message)
        self.button.pack (padx = 10, pady = 10)

        self.clearbtn = tk.Button (self.root, text = "clear", font = ("arial", 18), command = self.clear)
        self.clearbtn.pack(padx = 10, pady = 10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo (title = "message", message = self.textbox.get("1.0", tk.END))

    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
    
    def on_closing(self):
        if messagebox.askyesno (title = "quit?", message = "do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete("1.0", tk.END)

mygui()