import tkinter as tk
root =tk.Tk()
root.geometry()
root.title('MENU')
def temp():
    pass
mb = tk.Menu(root)
fm = tk.Menu(mb, tearoff=0)
mb.add_cascade(label='파일(f)', menu=fm)
fm.add_command(label='새 파일(n)', command=temp)
fm.add_command(label='열기(o)', command=temp)
fm.add_command(label='다른 이름으로 저장(a)', command=temp)
fm.add_command(label='저장(s)', command=temp)
em = tk.Menu(mb, tearoff=0)
mb.add_cascade(label='편집', menu=em)

hm = tk.Menu(mb, tearoff=0)
mb.add_cascade(label='사용법', menu=hm)

text = tk.Text()
text.pack()

root.config(menu=mb)
root.mainloop()