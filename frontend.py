import tkinter as tk
import subprocess

def get_text():
    command = entry.get()
    result_label.config(text=f"You entered: {command}")
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check the return code to see if the command was successful
        if result.returncode == 0:
            print("Command executed successfully")
            print("Standard Output:")
            print(result.stdout)
        else:
            print("Command failed with an error code:", result.returncode)
            print("Error Output:")
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", str(e))

window = tk.Tk()
window.title("Get Information Example")

entry = tk.Entry(window)
entry.pack()

get_button = tk.Button(window, text="Get Text", command=get_text)
get_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()