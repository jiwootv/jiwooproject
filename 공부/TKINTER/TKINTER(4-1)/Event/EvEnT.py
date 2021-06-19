import tkinter as tk


def okclick():
    name = b.get()
    print(name)
    a.config(text=name)


def ret(event):
    a.config(text='안녕')
    print(event)


root = tk.Tk()

a = tk.Label(text='안...녕? 일까?')
a.pack()

b=tk.Entry()
b.pack()

btn = tk.Button(root, text='O케이', command=okclick)
btn.pack()

a.bind('<Button-1>', ret)
root.mainloop()