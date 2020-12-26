import random
from tkinter import *
import tkinter.messagebox as msgbox

import os
dir = os.path.dirname(__file__)


window = Tk()
window.title("Rock Paper Scissor")
window.geometry("400x400")
frame1 = Frame(window)
frame1.pack(padx=10, pady=60)


def check(selected_img):
    computer_choice = random.choice(['rock', 'paper', 'scissor'])
    win1 = selected_img == 'rock' and computer_choice == 'scissor'
    win2 = selected_img == 'paper' and computer_choice == 'rock'
    win3 = selected_img == 'scissor' and computer_choice == 'paper'
    if selected_img == computer_choice:
        msgbox.showinfo(
            "Draw", "The Result is draw. Both selected {}".format(computer_choice))
    elif win1 or win2 or win3:
        msgbox.showinfo("Winner", "You won the game. You selcted {}, computer selected {}".format(
            selected_img, computer_choice))
    else:
        msgbox.showerror(
            "Loser", "You loss the game. You selcted {}, computer selected {}".format(selected_img, computer_choice))


image_rock = PhotoImage(file=os.path.join(dir, 'rock_modi.png'))

label1 = Button(frame1, image=image_rock, command=lambda: check('rock'))
label1.grid(row=0, column=0, padx=10, pady=10)

image_paper = PhotoImage(file=os.path.join(dir, 'paper_modi.png'))

label2 = Button(frame1, image=image_paper, command=lambda: check('paper'))
label2.grid(row=0, column=1, padx=10, pady=10)

image_scissor = PhotoImage(file=os.path.join(dir, 'scissor_modi.png'))

label3 = Button(frame1, image=image_scissor, command=lambda: check('scissor'))
label3.grid(row=0, column=2, padx=10, pady=10)

window.mainloop()
