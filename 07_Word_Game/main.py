from tkinter import *
window = Tk()
window.geometry('400x400')
frame = Frame(window)
frame.pack(padx=0, pady=40)

n_r = 6

d = {(i, j): StringVar() for i in range(0, n_r) for j in range(0, n_r)}


def check():
    for i in d:
        print(d[i].get(), end=" ")
    return True


for i in range(0, n_r):
    for j in range(0, n_r):
        Entry(frame, width=1, justify=CENTER,
              textvariable=d[(i, j)], validatecommand=check,  validate="focusout", font="Calibri 24").grid(row=i, column=j, ipadx=8)
window.mainloop()
