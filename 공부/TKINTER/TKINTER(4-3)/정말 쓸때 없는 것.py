import tkinter as tk
import tkinter

root = tk.Tk()
root.geometry('1200x1200')
root.resizable(False, False)

image = tk.PhotoImage(file="gimgenuuck.gif")

label5 = tk.Label(root, image=image)

label6 = tkinter.Label(root, text='''울트라 슈퍼 레전드 래어!
김근육. 빨간 적과 모든 적을 무조건 날리고 한방에 죽인다 그리고 파동 데미지를 주며, 초초초초초초그그그그그극
데미지를 준다. 또 전투에서 승리 할 때마다 동무 tong조림 10개씩 추가, 머니 1972 증정..''', anchor='n', fg='red', justify='left')

k = 0
b = 0


def command():
    global label2
    global label3
    global label5
    global label6
    label5.config(image='')
    label6.config(text='')
    image = tk.PhotoImage(file="tera-a.gif")

    label2 = tk.Label(root, image=image)

    label2.pack()
    label3 = tkinter.Label(root, text='''레전드 래어!
    테라의 요정. 빨간 적과 모든 적을 무조건 날리고 한방에 죽인다.''', anchor='n', fg='red', justify='left')
    label3.config(font=("Courier", 13), )
    label3.pack()
    root.mainloop()


def command2():
    global label2
    global label3
    global label5
    global label6
    label2.config(image='')
    label3.config(text='')
    image = tk.PhotoImage(file="gimgenuuck.gif")

    label5 = tk.Label(root, image=image)

    label5.pack()
    label6 = tkinter.Label(root, text='''울트라 슈퍼 레전드 래어!
    김근육. 빨간 적과 모든 적을 무조건 날리고 한방에 죽인다 그리고 파동 데미지를 주며, 초초초초초초그그그그그극
    데미지를 준다. 또 전투에서 승리 할 때마다 동무 통조림 10개씩 추가, 머니 1972 증정..''', anchor='n', fg='red', justify='left')
    label6.config(font=("Courier", 13), )
    label6.pack()
    root.mainloop()


bt = tk.Button(text="래전드 레어", command=command)
bt.pack()

bt2 = tk.Button(text="울트라 슈퍼 래전드 레어", command=command2)
bt2.pack()

root.mainloop()
