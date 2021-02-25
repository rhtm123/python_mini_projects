from tkinter import *
from tkinter import messagebox
import sys


class TicTacToe:
    # contructor method
    def __init__(self):

        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x400")
        self.window.wm_iconbitmap('The-Learning-Setu-Logo.ico')

        self.frame = Frame(self.window)
        self.frame.pack(padx=20, pady=50)
        self.a = {i: StringVar() for i in range(9)}
        self.player = 'X'
        self.playing = StringVar()
        self.playing.set('X')
        self.count = 0
        self.create_buttons()
        self.win_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                         [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        self.window.mainloop()

    def playagain(self):
        self.window.destroy()
        TicTacToe()

    def check_win(self):
        for win in self.win_comb:
            c1 = self.a[win[0]].get() == self.player
            c2 = self.a[win[1]].get() == self.player
            c3 = self.a[win[2]].get() == self.player
            if c1 and c2 and c3:
                res = messagebox.askquestion(
                    "Winner", "Player {} wins the game. Do you want to play again?".format(self.player))
                if res == 'yes':
                    self.playagain()
                else:
                    sys.exit()

    def check_update(self, index_value):
        if not self.a[index_value].get():
            self.a[index_value].set(self.player)

            win = self.check_win()

            self.player = 'X' if self.player == 'O' else 'O'
            self.count += 1
        if not win and self.count == 9:
            res = messagebox.askquestion(
                "Draw", "No one wins the game. Do you want to play again?")
            if res == 'yes':
                self.playagain()
            else:
                sys.exit()

    def create_buttons(self):
        for i in range(9):
            Button(self.frame, textvariable=self.a[i],
                   command=lambda i=i: self.check_update(i), width=1, font="Calibri 30").grid(row=i//3, column=i % 3, ipadx=20)


if __name__ == "__main__":
    TicTacToe()
