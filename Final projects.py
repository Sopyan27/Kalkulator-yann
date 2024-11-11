import tkinter as tk

window = tk.Tk()
window.title("Kalkulator")
window.geometry("400x600")

def tombol_klik(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

def bt_del():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

expression = ""
input_text = tk.StringVar()

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=5)

frame1 = tk.Frame(window, bg="Grey")
frame1.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

frame2 = tk.Frame(window, bg="Black")
frame2.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

frame1.grid_columnconfigure(0, weight=1)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_rowconfigure(1, weight=1)

for i in range(5):
    frame2.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame2.grid_columnconfigure(i, weight=1)

label1 = tk.Label(frame1, text="Muhammad Sopyan, XII PPLG 1", bg="white", font=("Arial", 12))
label1.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

label2 = tk.Label(frame1, text="Halo, ini Muhammad Sopyan XII PPLG 1", textvariable=input_text, bg="gray", anchor="e", justify="right", font=("Arial", 32), fg="white")
label2.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

button_font = ("Arial", 18)

buttons = [
    ("C", bt_clear, 0, 0), ("DEL", bt_del, 0, 1), ("/", lambda: tombol_klik("/"), 0, 3), 
    ("%", lambda: tombol_klik("/100"), 0, 2),
    ("7", lambda: tombol_klik("7"), 1, 0), ("8", lambda: tombol_klik("8"), 1, 1), ("9", lambda: tombol_klik("9"), 1, 2), ("×", lambda: tombol_klik("*"), 1, 3),
    ("4", lambda: tombol_klik("4"), 2, 0), ("5", lambda: tombol_klik("5"), 2, 1), ("6", lambda: tombol_klik("6"), 2, 2), ("-", lambda: tombol_klik("-"), 2, 3),
    ("1", lambda: tombol_klik("1"), 3, 0), ("2", lambda: tombol_klik("2"), 3, 1), ("3", lambda: tombol_klik("3"), 3, 2), ("+", lambda: tombol_klik("+"), 3, 3),
    ("0", lambda: tombol_klik("0"), 4, 0, 2), (".", lambda: tombol_klik("."), 4, 2), ("=", bt_equal, 4, 3)
]

for (text, command, row, col, *colspan) in buttons:
    button = tk.Button(frame2, text=text, command=command, 
                       bg="grey" if text in ["+", "-", "*", "/", "C", "DEL", "×", "=","%"] else None, 
                       fg="white" if text in ["+", "-", "*", "/", "C", "DEL", "×", "=","%"] else None, font=button_font)
    button.grid(row=row, column=col, columnspan=colspan[0] if colspan else 1, sticky="nsew", pady=10, padx=10)

window.mainloop()