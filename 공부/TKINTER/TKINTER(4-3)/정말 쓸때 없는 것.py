import tkinter as tk

root = tk.Tk()
root.geometry('1200x1200')
root.resizable(False, False)

bt = []
k = 0
for i in range(23):
    for j in range(100):
        bt.append(tk.Button(text='버튼'+str(k)))
        bt[k].place(x=55*i, y=55*j)
        k += 1
root.mainloop()