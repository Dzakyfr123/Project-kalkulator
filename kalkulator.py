import tkinter as tk

def tombol_klik(teks):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + teks)

def hapus():
    entry.delete(0, tk.END)

def hitung():
    try:
        hasil = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(hasil))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


window = tk.Tk()
window.title("Kalkulator")
window.config(bg="orange")

entry = tk.Entry(window, font=("Arial", 20), bg="white", fg="black", bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

tombol_data = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in tombol_data:
    if text == "=":
        tombol = tk.Button(window, text=text, font=("Arial", 20), width=5, height=2, bg="lightgreen", command=hitung)
    else:
        tombol = tk.Button(window, text=text, font=("Arial", 20), width=5, height=2, bg="lightblue", command=lambda t=text: tombol_klik(t))
    tombol.grid(row=row, column=col)

tombol_hapus = tk.Button(window, text="C", font=("Arial", 20), width=5, height=2, bg="red", command=hapus)
tombol_hapus.grid(row=4, column=4)

window.mainloop()
