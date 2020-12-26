from PyDictionary import PyDictionary
from tkinter import *
window = Tk()
window.geometry('400x400')
frame = Frame(window)
frame.pack(padx=0, pady=40)

n_r = 6

d = {(i, j): StringVar() for i in range(0, n_r) for j in range(0, n_r)}

last_ = (0, 0)

words_found = []
player_score = {'p1': 0, 'p2': 0}

player = 'p1'


def check(i, j):
    global last_
    last_ = (i, j)


dictionary = PyDictionary()


def check_in_dictionary(words):
    count = 0
    for word in words:
        if (word not in words_found and len(word) > 1) or word == 'a':
            a = dictionary.meaning(word)
            if a != None:
                count += len(word)
                words_found.append(word)
    print(words_found)
    return count


def get_right_left(j):
    words = [d[(last_[0], last_[1])].get()]

    pos = 1
    while True:
        if ((last_[1]+j*pos > 5) or (last_[1]+j*pos < 0)):
            break

        if not d[(last_[0], last_[1]+j*pos)].get():
            break
        if j == 1:
            word = words[pos-1]+d[last_[0], last_[1]+j*pos].get()
        else:
            word = d[last_[0], last_[1]+j*pos].get() + words[pos-1]

        words.append(word)
        pos = pos + 1

    return(words)


def get_top_bottom(i):
    words = [d[(last_[0], last_[1])].get()]

    pos = 1
    while True:
        if ((last_[0]+i*pos > 5) or (last_[0]+i*pos < 0)):
            break

        if not d[(last_[0]+i*pos, last_[1])].get():
            break
        if i == 1:
            word = words[pos-1]+d[last_[0]+i*pos, last_[1]].get()
        else:
            word = d[last_[0]+i*pos, last_[1]].get()+words[pos-1]
        words.append(word)
        pos = pos + 1

    return(words)


def dothis():
    words = set(get_right_left(1)+get_right_left(-1) +
                get_top_bottom(1)+get_top_bottom(-1))
    print(words)
    score = check_in_dictionary(words)
    global player
    player_score[player] = player_score[player] + score
    if player == 'p1':
        player = 'p2'
    else:
        player = 'p1'
    print(player_score)


for i in range(0, n_r):
    for j in range(0, n_r):
        Entry(frame, width=1, justify=CENTER,
              textvariable=d[(i, j)], validatecommand=lambda i=i, j=j: check(i, j), validate="focusin", font="Calibri 24").grid(row=i, column=j, ipadx=8)

frame1 = Frame(window)
frame1.pack()

Button(frame1, text='check', command=dothis).pack()
window.mainloop()
