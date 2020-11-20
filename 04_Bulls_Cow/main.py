
import random
from tkinter import *
window = Tk()

window.title("BULLS COW GAME")
window.geometry("400x400")


def cow(n1, n2):
    count = 0
    for i in n1:
        if i in n2:
            count = count + 1
    return count


def bull(n1, n2):
    count = 0
    for i in range(len(n1)):
        if n1[i] == n2[i]:
            count = count + 1
    return count


def gererate_random_number():
    nums = ''
    while True:
        a = str(random.randint(0, 9))
        if a not in nums:
            nums = nums + a
        if len(nums) == 4:
            break
    return nums


original = gererate_random_number()

l1 = Label(window, text="Welcome to BullsCow Game")
l1.config(font=("Calibri", 18))

l1.pack(pady=10)


l2 = Label(window, text="Enter your guess : ")
l2.pack()

f1 = Frame(window,)
f1.pack(pady=10)

count = 0


def check():
    global count
    count += 1
    guess = entry_text1.get() + entry_text2.get() + \
        entry_text3.get() + entry_text4.get()
    bull_n = bull(original, guess)
    cow_n = cow(original, guess)
    entry_text1.set("")
    entry_text2.set("")
    entry_text3.set("")
    entry_text4.set("")

    Label(f2, text="Guess={}, Cow={}, Bull={}".format(
        guess, cow_n, bull_n)).pack()
    # if guess == original:


entry_text1 = StringVar()

e1 = Entry(f1, text=entry_text1, font=("Calibri", 14), width=1)
e1.grid(row=0, column=0, ipadx=4, ipady=4, padx=4)

entry_text2 = StringVar()
e2 = Entry(f1, text=entry_text2,  font=(
    "Calibri", 14), width=1, justify=CENTER)
e2.grid(row=0, column=1, ipadx=4, ipady=4, padx=4)

entry_text3 = StringVar()
e3 = Entry(f1, text=entry_text3,  font=("Calibri", 14), width=1)
e3.grid(row=0, column=2, ipadx=4, ipady=4, padx=4)

entry_text4 = StringVar()
e4 = Entry(f1, text=entry_text4,  font=("Calibri", 14), width=1)
e4.grid(row=0, column=3, ipadx=4, ipady=4, padx=4)


b1 = Button(f1, text="Check", font=("Calibri", 14), command=check)
b1.grid(row=0, column=4, padx=4)


f2 = Frame(window,)
f2.pack(pady=10)


window.mainloop()
