#!/usr/bin/env python
from tkinter import *
from tkinter import messagebox
import random

lottery_numbers = []
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('PythonExamples.org - Tkinter Example')


def already_there(number):
    if number not in lottery_numbers:
        lottery_numbers.append(number)


    while len(lottery_numbers) <= 5:
        number = random.randint(1, 95)
        already_there(number)

lottery_numbers.sort()
print(lottery_numbers)



def showMsg():
    # messagebox.showinfo('Message', 'Here are your numbers' + lottery_numbers)
    messagebox.showinfo(generate_numbers)
    # print(messagebox)



button = Button(tkWindow,
                text='Submit',
                command=generate_numbers())

button.pack()

tkWindow.mainloop()
