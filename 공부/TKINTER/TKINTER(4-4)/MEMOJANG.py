import tkinter as tk
from tkinter.filedialog import *
import os

root = tk.Tk()
root.title('기록장')
root.geometry('1200x600')

tx = tk.Text()
tx.pack()


def saveeff():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    ts = str(tx.get(1.0, 'end'))
    f.write()
    f.close()
def openeff():
    file = askopenfilename(title="파일 선택(하지마세요)", filetypes=(("txt파일", "*.txt"), ("모든 파일", '*.*')))
    root.title(os.path.basename(file) + " - 메모장")
    tx.delete(1.0, 'end')
    f = open(file, "r")
    tx.insert(1.0, f.read())
    f.close()


m = tk.Menu(root)
fm = tk.Menu(m, tearoff=0)
m.add_cascade(label='파일', menu=fm)
fm.add_command(label='jㅓ장', command=saveeff)
fm.add_command(label='O픈', command=openeff)
root.config(menu=m)



# mb=tk.Menu(root)
# fm=tk.Menu(mb, tearoff=0)
# mb.add_cascade(label='파일', Menu=fm)
# fm.add_cascade(label='파일', Menu=fm)
# cm.add_cascade(label='파일', Menu=fm)

root.mainloop()
