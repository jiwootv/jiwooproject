import tkinter as tk


def click():
    name = b.get()
    print(name)
    a.config(text=name)


root = tk.Tk()

a = tk.Label(text="아아아아안녕")
a.pack()

b = tk.Entry()
b.pack()

btn = tk.Button(root, text="ok", command=click)
btn.pack()

root.mainloop()