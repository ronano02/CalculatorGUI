from tkinter import *

gui = Tk()
gui.title('Calculator')
gui.resizable(0, 0)
gui.configure(bg='#434343')

entry = Entry(gui, font=('arial', 20, 'bold'), width=25, borderwidth=5, bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=4, pady=0)


# Records and inserts on screen the values inputted from user
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


# Stores the first value and calculation method as global variables to be used in the equal function
def button_calculate(function):
    global first_number
    first_number = float(entry.get())
    global method
    method = function
    entry.delete(0, END)


# Intakes second value from user then performs calculation with value entered previously and chosen calculation method
def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if method == '+':
        entry.insert(0, first_number + float(second_number))
    if method == '-':
        entry.insert(0, first_number - float(second_number))
    if method == '*':
        entry.insert(0, first_number * float(second_number))
    if method == '/':
        entry.insert(0, first_number / float(second_number))


# Clears screen
def button_clear():
    entry.delete(0, END)


# Defines buttons text, colour, padding, and function
button_1 = Button(gui, text='1', padx=35, pady=12, command=lambda: button_click(1), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_2 = Button(gui, text='2', padx=35, pady=12, command=lambda: button_click(2), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_3 = Button(gui, text='3', padx=35, pady=12, command=lambda: button_click(3), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_4 = Button(gui, text='4', padx=35, pady=12, command=lambda: button_click(4), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_5 = Button(gui, text='5', padx=35, pady=12, command=lambda: button_click(5), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_6 = Button(gui, text='6', padx=35, pady=12, command=lambda: button_click(6), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_7 = Button(gui, text='7', padx=35, pady=12, command=lambda: button_click(7), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_8 = Button(gui, text='8', padx=35, pady=12, command=lambda: button_click(8), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_9 = Button(gui, text='9', padx=35, pady=12, command=lambda: button_click(9), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_0 = Button(gui, text='0', padx=83.4, pady=12, command=lambda: button_click(0), bg='#999999', fg='white',
                  font='Arial 15 bold')
button_dot = Button(gui, text='.', padx=37.4, pady=12, command=lambda: button_click('.'), bg='#999999', fg='white',
                    font='Arial 15 bold')
button_plus = Button(gui, text='+', padx=34, pady=12, command=lambda: button_calculate('+'), bg='#999999', fg='white',
                     font='Arial 15 bold')
button_minus = Button(gui, text='-', padx=37, pady=12, command=lambda: button_calculate('-'), bg='#999999', fg='white',
                      font='Arial 15 bold')
button_div = Button(gui, text='÷', padx=35, pady=12, command=lambda: button_calculate('/'), bg='#999999', fg='white',
                    font='Arial 15 bold')
button_mult = Button(gui, text='x', padx=35, pady=12, command=lambda: button_calculate('*'), bg='#999999', fg='white',
                     font='Arial 15 bold')
button_clc = Button(gui, text='Clear', padx=113, pady=12, command=button_clear, bg='orange', fg='white',
                    font='Arial 15 bold')
button_eql = Button(gui, text='=', padx=34.4, pady=12, command=button_equal, bg='#999999', fg='white',
                    font='Arial 15 bold')

# Button screen format
button_clc.grid(row=1, column=0, columnspan=3)
button_mult.grid(row=1, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_minus.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_plus.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_div.grid(row=2, column=3)

button_0.grid(row=5, column=0, columnspan=2)
button_dot.grid(row=5, column=2)
button_eql.grid(row=5, column=3)

gui.mainloop()
