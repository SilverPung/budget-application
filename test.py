import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Combobox Example")

selected_value = tk.StringVar()

combobox = ttk.Combobox(window, textvariable=selected_value)
combobox['values'] = ("add expense", "add income", "delete", "list", "stats")
combobox.pack()

selection_label = tk.Label(window, textvariable=selected_value)
selection_label.pack()

def on_select(event):
    selected_item = selected_value.get()
    selection_label.config(text=f"Selected: {selected_item}")

combobox.bind("<<ComboboxSelected>>", on_select)

window.mainloop()
