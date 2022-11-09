from tkinter import*
from tkinter.font import Font

root = Tk()
root.title('Calculator')
root.geometry('500x500')
myFont = Font(family='Calibri', size=30)

entry = Entry(root, width=21, borderwidth=5, font=('ds-digital', 39))
entry.grid(row=0, column=0, columnspan=5, rowspan=2)

global num
global math


def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(number))
    entry.insert(0, str(current))


def dot():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + '.')


def add():
    first_number = entry.get()
    global num
    global math
    math = 'addition'
    num = float(first_number)
    entry.delete(0, END)


def sub():
    first_number = entry.get()
    global num
    global math
    math = 'subtraction'
    num = float(first_number)
    entry.delete(0, END)


def mul():
    first_number = entry.get()
    global num
    global math
    math = 'multiplication'
    num = float(first_number)
    entry.delete(0, END)


def div():
    first_number = entry.get()
    global num
    global math
    math = 'division'
    num = float(first_number)
    entry.delete(0, END)


def equal():
    second_number = float(entry.get())

    if math == 'addition':
        res = (float(second_number) + float(num))
        entry.delete(0, END)
        entry.insert(0, float(res))

    elif math == 'subtraction':
        res = (float(num) - float(second_number))
        entry.delete(0, END)
        entry.insert(0, float(res))

    elif math == 'multiplication':
        res = (float(num) * float(second_number))
        entry.delete(0, END)
        entry.insert(0, float(res))

    elif math == 'division':
        res = (float(num) / float(second_number))
        entry.delete(0, END)
        entry.insert(0, float(res))


def clear():
    entry.delete(0, END)
    return


def delete():
    current = entry.get()

    if len(current) == 1:
        entry.delete(0, END)

    if len(current) > 1:
        judg = current[-2]
        if judg == '.':
            now = current[0:-2]
            entry.delete(0, END)
            entry.insert(0, now)
        else:
            now = current[0:-1]
            entry.delete(0, END)
            entry.insert(0, now)


b1 = Button(root, pady=15, padx=30, font=myFont, text=1, command=lambda: click(1))
b2 = Button(root, pady=15, padx=30, font=myFont, text=2, command=lambda: click(2))
b3 = Button(root, pady=15, padx=30, font=myFont, text=3, command=lambda: click(3))

b4 = Button(root, pady=15, padx=30, font=myFont, text=4, command=lambda: click(4))
b5 = Button(root, pady=15, padx=30, font=myFont, text=5, command=lambda: click(5))
b6 = Button(root, pady=15, padx=30, font=myFont, text=6, command=lambda: click(6))

b7 = Button(root, pady=15, padx=30, font=myFont, text=7, command=lambda: click(7))
b8 = Button(root, pady=15, padx=30, font=myFont, text=8, command=lambda: click(8))
b9 = Button(root, pady=15, padx=30, font=myFont, text=9, command=lambda: click(9))

b0 = Button(root, pady=15, padx=30, font=myFont, text=0, command=lambda: click(0))
bdot = Button(root, pady=15, padx=36, font=myFont, text='.', command=dot)

bdiv = Button(root, pady=15, padx=35, font=myFont, text='/', command=div)
bmul = Button(root, pady=15, padx=32, font=myFont, text='x', command=mul)
bsub = Button(root, pady=15, padx=31, font=myFont, text='+', command=sub)
badd = Button(root, pady=15, padx=30, font=myFont, text='+', command=add)

bclear = Button(root, pady=15, padx=19, font=myFont, text='AC', command=clear)
bdel = Button(root, pady=15, padx=12.49, font=myFont, fg='#901313', text='DEL', command=delete)
bequals = Button(root, pady=49, padx=30, font=myFont, fg='#199E15', text='=', command=equal)


b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)

b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)

b7.grid(row=4, column=0)
b8.grid(row=4, column=1)
b9.grid(row=4, column=2)

b0.grid(row=5, column=1)
bdot.grid(row=5, column=2)

bdiv.grid(row=2, column=3)
bmul.grid(row=3, column=3)
bsub.grid(row=4, column=3)
badd.grid(row=5, column=3)

bclear.grid(row=2, column=4)
bdel.grid(row=3, column=4)
bequals.grid(row=4, column=4, rowspan=2)


root.mainloop()