import tkinter as tk
import subprocess
from tkinter import ttk

class Commands:
    def add(self,expense):
        global window
        window.destroy()

        window = tk.Tk()
        window.title("Get Information Example")
        text=tk.Label(window,text='Podaj nazwę')
        text.pack()
        name = tk.Entry(window)
        name.pack()
        text=tk.Label(window,text='Podaj categorie')
        text.pack()
        category = tk.Entry(window)
        category.pack()
        text=tk.Label(window,text='Podaj date')
        text.pack()
        date = tk.Entry(window)
        date.pack()
        text=tk.Label(window,text='Podaj wartość')
        text.pack()
        value = tk.Entry(window)
        value.pack()
        if expense==True:
            get_button = tk.Button(window, text="Get Text", command=lambda:self.add_expense(name.get(),category.get(),date.get(),value.get()))
            get_button.pack()
        else:
            get_button = tk.Button(window, text="Get Text", command=lambda:self.add_income(name.get(),category.get(),date.get(),value.get()))
            get_button.pack()
        result_label = tk.Label(window, text="")
        result_label.pack()

        window.mainloop()
    def delete(self):
        global window
        window.destroy()

        window = tk.Tk()
        window.title("Get Information Example")
        text=tk.Label(window,text='Podaj id')
        text.pack()
        id = tk.Entry(window)
        id.pack()
        get_button = tk.Button(window, text="Get Text", command=lambda:self.delete_it(id.get()))
        get_button.pack()
    def list_items(self):
        command='python main.py --list'
        from_sys(command)
    def stats(self):
        command='python main.py --stats'
        from_sys(command)
    def add_expense(self,name,cat,date,value):
        command=f'python main.py --add-expense --name {name} --category {cat} --date {date} --value {value}'
        to_sys(command)
    def add_income(self,name,cat,date,value):
        command=f'python main.py --add-income --name {name} --category {cat} --date {date} --value {value}'
        to_sys(command)
    def delete_it(self,id):
        command=f'python main.py --delete --id {id}'
        to_sys(command)
def from_sys(command):
    result = subprocess.check_output(command, text=True)

    output(result)
def to_sys(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            pass
        else:
            print("Command failed with an error code:", result.returncode)
            print("Error Output:")
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", str(e))
def output(result):
    global window
    window.destroy()
    window = tk.Tk()
    window.title("Get Information Example")
    text=tk.Label(window,text=result)
    text.pack()
    window.mainloop()
if __name__=='__main__':
    window = tk.Tk()
    window.title("Combobox Example")

    selected_value = tk.StringVar()

    combobox = ttk.Combobox(window, textvariable=selected_value)
    combobox['values'] = ("add expense", "add income", "delete", "list", "stats")
    combobox.pack()

    selection_label = tk.Label(window, textvariable=selected_value)
    selection_label.pack()

    def on_select(event):
        command = selected_value.get()
        apc=Commands()
        match(command):
            case 'add expense':
                apc.add(True)
            case 'add income':
                apc.add(False)
            case 'delete':
                apc.delete()
            case 'list':
                apc.list_items()
            case 'stats':
                apc.stats()
    combobox.bind("<<ComboboxSelected>>", on_select)

    window.mainloop()