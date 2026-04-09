import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "←":
        value = entry.get()
        if value:
            entry.delete(len(value)-1, tk.END)
    else:
        if text == ",":
            text = "."
        entry.insert(tk.END, text)


def key_press(event):
    key = event.keysym
    char = event.char

    if key == "Return" or char == "=":
        calculate()
    elif key == "BackSpace":
        value = entry.get()
        if value:
            entry.delete(len(value)-1, tk.END)
    elif key == "Escape" or char.lower() == "c":
        entry.delete(0, tk.END)
    elif char == ",":
        entry.insert(tk.END, ".")
    elif char in "0123456789.+-*/":
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.bind("<Key>", key_press)

entry = tk.Entry(root, font="Arial 20", justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "←", "+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    btn = tk.Button(frame, text=button, font="Arial 18", width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(root, text="C" , font="Arial 18")
clear_button.pack(fill=tk.BOTH)
clear_button.bind("<Button-1>", click)

root.mainloop()