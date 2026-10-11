import tkinter as tk
from tkinter import messagebox
from decimal import Decimal



AVOGADRO_CONSTANT = Decimal("6.022E+23")


def calculate() -> None:
	try:
		values = [Decimal(entries[name].get()) for name in input_names]
		vb, dc, cn, lp, mbp = values
		result = vb * dc * cn * lp * mbp / Decimal(AVOGADRO_CONSTANT)
		result_label.config(text=f"Result: {result:.10g}")
	except ValueError:
		messagebox.showerror("Invalid input", "Please enter a number in every field.")
	except ZeroDivisionError:
		messagebox.showerror("Invalid input", "NA cannot be zero.")


root = tk.Tk()
root.title("Miniprep max yield calculator")
root.resizable(False, False)

input_names = ["Vb", "Dc", "CN", "Lp", "mbp"]
entries = {}

for row, name in enumerate(input_names):
	tk.Label(root, text=f"{name}:").grid(row=row, column=0, padx=10, pady=5, sticky="e")
	entry = tk.Entry(root, width=20)
	entry.grid(row=row, column=1, padx=10, pady=5)
	entries[name] = entry

tk.Button(root, text="Calculate", command=calculate).grid(
	row=len(input_names), column=0, columnspan=2, pady=10
)
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=len(input_names) + 1, column=0, columnspan=2, pady=(0, 10))

root.mainloop()
