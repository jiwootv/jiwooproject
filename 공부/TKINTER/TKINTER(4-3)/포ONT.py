import tkinter as tk
import tkinter.font

root = tk.Tk()

font = tkinter.font.Font(family="Bahnschrift SemiBold SemiConden", size=20 ,slant='italic')
print(tkinter.font.families())
label = tk.Label(root, text="파이썬 1972.6", font=font)
label.pack()
image = tk.PhotoImage(file="tera-a.gif")

label2 = tk.Label(root, image=image)

label2.pack()
label3 = tkinter.Label(root, text='''레전드 래어!
테라의 요정. 빨간 적과 모든 적을 무조건 날리고 한방에 죽인다.''', anchor='n', fg='red', justify='left')
label3.config(font=("Courier", 13), )
label3.pack()
root.mainloop()