import tkinter as tk

class KeypadApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Keypad")
        self.display = tk.Entry(self, font=("Arial", 20), state="readonly")
        self.display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create the keypad buttons
        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', 'Clear'
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == '0':
                tk.Button(self, text=button, font=("Arial", 20), width=5, command=lambda x=button: self.add_to_display(x)).grid(row=4, column=1, padx=5, pady=5)
            elif button == 'Clear':
                tk.Button(self, text=button, font=("Arial", 20), width=5, command=self.clear_display).grid(row=4, column=0, padx=5, pady=5)
            else:
                tk.Button(self, text=button, font=("Arial", 20), width=5, command=lambda x=button: self.add_to_display(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

    def add_to_display(self, value):
        self.display.configure(state="normal")
        self.display.insert(tk.END, value)
        self.display.configure(state="readonly")

    def clear_display(self):
        self.display.configure(state="normal")
        self.display.delete(0, tk.END)
        self.display.configure(state="readonly")

if __name__ == '__main__':
    app = KeypadApp()
    app.mainloop()