import tkinter as tk
root = tk.Tk()
root.geometry('320x240')
root.title('프rame test')

f_a = tk.Frame(root)
f_a.pack()

rf = tk.Frame(root)
rf.pack(side=tk.RIGHT, expand=True)

lf = tk.Frame(root)
lf.pack(side=tk.LEFT, expand=True)
lb1 = tk.Label(f_a, text=str(" ('안')안녕하세요"))
lb1.pack()

bt1 = tk.Button(lf, text='버튼1')
bt1.pack()

bt2 = tk.Button(rf, text='버튼1')
bt2.pack()

bt3 = tk.Button(lf, text='버튼1')
bt3.pack()

bt4 = tk.Button(rf, text='버튼1')
bt4.pack()

root.mainloop()
