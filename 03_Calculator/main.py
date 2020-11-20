
from tkinter import *


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ""
    input_text.set("")


def btn_equal():
    try:
        global expression
        # 'eval' function is used for evaluating the string expressions directly
        result = str(eval(expression))
        # you can also implement your own function to evalute the expression istead of 'eval' function
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""


if __name__ == '__main__':
    window = Tk()
    window.geometry("312x320")

    # in order to prevent resize
    window.resizable(0, 0)

    # set title
    window.title("Calculator")

    input_text = StringVar()
    expression = ""

    input_frame = Frame(window, width=312, height=60, bd=0,
                        highlightbackground="black", highlightcolor="black", highlightthickness=1)
    input_frame.pack(side=TOP)

    input_field = Entry(input_frame, font=('arial', 20, 'bold'),
                        textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
    input_field.grid(row=0, column=0)
    # 'ipady' is an internal padding to increase the height of input field
    input_field.pack(ipady=5, ipadx=5)

    btns_frame = Frame(window, width=312, bg="grey")
    btns_frame.pack()

    clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee",
                   cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
    divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                    cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

    seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
                   cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
    eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
                   cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
    nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
    multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
                      cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

    four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
    five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
    six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
    minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
                   cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

    # The fourth row will comprise of the buttons '1', '2', '3' and 'Addition (+)'
    one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
    two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
    three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
                   cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
    plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

    # Finally, the fifth row will comprise of the buttons '0', 'Decimal (.)', and 'Equal To (=)'
    zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(0)).grid(row=4, column=0, padx=1, pady=1)
    point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
                   cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=1, padx=1, pady=1)
    equals = Button(btns_frame, text="=", fg="black", width=21, height=3, bd=0, bg="#eee",
                    cursor="hand2", command=lambda: btn_equal()).grid(row=4, column=2, columnspan=2, padx=1, pady=1)

    window.mainloop()
