#   - generate a random number between 1 to 100
#   - Takes input form the user (8 times)
#   - if user input is right -> display congrats otherwise display help message - your input is greater or less

import tkinter as tk
import tkinter.messagebox as msgbox

from random import randint
count = 0

random_number = randint(1, 100)

window = tk.Tk()
# to rename the title of the window
window.wm_iconbitmap('The-Learning-Setu-Logo.ico')

window.title("Guess The Number")
window.geometry("400x400")

input_text = tk.IntVar()

# tkinter.messagebox.showinfo("Alert Message", "This is just a alert message!")
#


def create_hint_label(hint):
    if hint == 'less':
        tk.Label(
            text="Count-> {} Your guess-{}, Hint: Guess is less".format(count, input_text.get()), fg="red").pack(pady=4)
    elif hint == "greater":
        tk.Label(
            text="Count-> {} Your guess-{}, Hint: Guess is greater".format(count, input_text.get()), fg="red").pack(pady=4)
    else:
        tk.Label(
            text="Count-> {} Your guress-{}, You correctly guessed the number.".format(count, random_number), fg="green").pack(pady=4)


def check_input():
    global count
    count += 1
    if input_text.get() < random_number:
        msgbox.showerror(
            "Hint", "Your guess is less than original number!")
        create_hint_label('less')
    elif input_text.get() > random_number:
        msgbox.showerror(
            "Hint", "Your guess is greater than original number!")
        create_hint_label('greater')
    else:
        msgbox.showinfo("Congrats", "You guess it")


    # pack is used to show the object in the window
label1 = tk.Label(
    window, text="Welcome to The learning Setu. ")

label1.config(font=("Helvetica", 14))

label1.pack(pady=20)

label2 = tk.Label(
    window, text="Guess the number (number is between 1 and 100) : ")

label2.config(font=("Helvetica", 12))

label2.pack(pady=2)

# frame = tk.Frame(window)


# first input-field is placed on position 01 (row - 0 and column - 1)
user_input = tk.Entry(window, textvariable=input_text, width=2)
user_input.config(font=("Helvetica", 10))
user_input.pack(pady=10, ipady=4, ipadx=2)

submit_btn = tk.Button(window, text="Submit", command=check_input)
submit_btn.config(font=("Helvetica", 10))
submit_btn.pack()

window.mainloop()
