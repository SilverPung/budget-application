import tkinter as tk
import subprocess
class Commands:
    def add_income(self):
        entry = tk.Entry(window)
        entry.pack()

        get_button = tk.Button(window, text="Get Text", command=get_text)
        get_button.pack()
    def add_expense(self):
        pass
    def delete(self):
        pass
    def list_items(self):
        pass
    def stats(self):
        pass
def get_text():
    command = entry.get()
    result_label.config(text=f"You entered: {command}")
    apc=Commands()
    match(command):
        case 'delete':
            apc.delete()
        case 'add_expense':
            apc.add_expense()
        case 'add_income':
            apc.add_income()
        case 'list':
            apc.list()
        case 'stats':
            apc.stats()
if __name__=='__main__':
    window = tk.Tk()
    window.title("Get Information Example")

    entry = tk.Entry(window)
    entry.pack()

    get_button = tk.Button(window, text="Get Text", command=get_text)
    get_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()