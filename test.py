from tkinter import *
from tkinter import messagebox
import random

lottery_numbers = []
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('PythonExamples.org - Tkinter Example')


def showMsg():
    # messagebox.showinfo('Message', 'Here are your numbers' + lottery_numbers)
    messagebox.showinfo(str(lottery_numbers))


def already_there(number):
    if number not in lottery_numbers:
        lottery_numbers.append(number)

    while len(lottery_numbers) <= 5:
        number = random.randint(1, 95)
        already_there(number)


button = Button(tkWindow,
                text='Submit',
                command=showMsg)
button.pack()

tkWindow.mainloop()
