import tkinter as tk

root = tk.Tk()
ab = tk.Label(text='안녕')
ab.config(font=("Courier", 19720))
ab.pack()

bc = tk.Entry()
bc.pack()

root.mainloop()
