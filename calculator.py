# Kyle Hinsey, CIS 345, TTh 12:00, A6
import math
from tkinter import *


def btn_press(btn):
    global calculation, number1, operation
    value = calculation.get()
    # if statement to process certain button press
    # will check if there is already a decimal in the string
    if btn == '.' and '.' in value:
        pass
    # change the sign of the string
    elif btn == '+/-':
        try:
            if value[0] == '-':
                value = value[1:]
            else:
                value = '-' + value
        except IndexError:
            pass
    # remove last value of string
    elif btn == '->':
        value = value[:-1]
    # find the square root of the number
    elif btn == 'sqrt':
        # when finding the square root of a number, the number must already be in the display
        try:
            value = str(math.sqrt(float(value)))
        # return error in case the user is trying to find the square root of a negative number
        except ValueError:
            value = 'Error'
    # operation user wants done
    elif btn in ['/', '*', '-', '+']:
        number1 = float(value)
        operation = btn
        value = ''
    else:
        # since the value of the numbers being pressed by the button is already a string,
        # there is no need to change its type
        value += btn
    # set the final value of the string
    calculation.set(value)


def equals():
    global number1, operation, calculation
    ans = 0  # declare ans here to prevent scope errors
    number2 = float(calculation.get())
    if operation == '*':
        ans = number1 * number2
    elif operation == '/':
        try:
            ans = number1 / number2
        except ZeroDivisionError:
            ans = 'Error'
    elif operation == '-':
        ans = number1 - number2
    elif operation == '+':
        ans = number1 + number2
    # set the calculation and reset the first number
    number1 = ''
    operation = ''
    # round answer to prevent python floating
    if ans != 'Error':
        ans = round(ans, 8)
    calculation.set(str(ans))


def clear_entry():
    global calculation, number1, operation
    # set the string to a blank string -- resetting it
    calculation.set('')
    # rest the number1 and operation to the default
    number1 = float()
    operation = ''


# create window
window = Tk()
window.geometry('320x320')
window.title('Kyle Hinsey - A6 Calculator')
window['bg'] = 'dodgerblue'

# create a variable for the display
calculation = StringVar()
calculation.set('')
# variables to perform operations
number1 = float()
operation = ''

# row 0 ===============================================================================================================

num_box = Entry(window, font=40, textvariable=calculation, justify=RIGHT, state=DISABLED)
num_box.grid(columnspan=4, padx=5, pady=5, ipadx=32, ipady=10)

# row 1 ===============================================================================================================

clear_btn = Button(window, text='C', bg='red', font=10, width=5, fg='white', command=clear_entry)
clear_btn.grid(row=1, column=0, padx=5, pady=5)

back_btn = Button(window, text='->', bg='lightgrey', width=5, font=10, command=lambda: btn_press('->'))
back_btn.grid(row=1, column=1, padx=5, pady=5)

sign_btn = Button(window, text='+/-', bg='lightgrey', width=5, font=10, command=lambda: btn_press('+/-'))
sign_btn.grid(row=1, column=2, padx=5, pady=5)

sqrt_btn = Button(window, text='sqrt', bg='lightgrey', width=5, font=10, command=lambda: btn_press('sqrt'))
sqrt_btn.grid(row=1, column=3, padx=5, pady=5)

# row 2 ===============================================================================================================

button7 = Button(window, text='7', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('7'))
button7.grid(row=2, column=0, padx=5, pady=5)

button8 = Button(window, text='8', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('8'))
button8.grid(row=2, column=1, padx=5, pady=5)

button9 = Button(window, text='9', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('9'))
button9.grid(row=2, column=2, padx=5, pady=5)

divide_btn = Button(window, text='/', bg='lightgrey', width=5, font=10, command=lambda: btn_press('/'))
divide_btn.grid(row=2, column=3, padx=5, pady=5)

# row 3 ===============================================================================================================

button4 = Button(window, text='4', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('4'))
button4.grid(row=3, column=0, padx=5, pady=5)

button5 = Button(window, text='5', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('5'))
button5.grid(row=3, column=1, padx=5, pady=5)

button6 = Button(window, text='6', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('6'))
button6.grid(row=3, column=2, padx=5, pady=5)

mult_btn = Button(window, text='*', bg='lightgrey', width=5, font=10, command=lambda: btn_press('*'))
mult_btn.grid(row=3, column=3, padx=5, pady=5)

# row 4 ===============================================================================================================

button1 = Button(window, text='1', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('1'))
button1.grid(row=4, column=0, padx=5, pady=5)

button2 = Button(window, text='2', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('2'))
button2.grid(row=4, column=1, padx=5, pady=5)

button3 = Button(window, text='3', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('3'))
button3.grid(row=4, column=2, padx=5, pady=5)

sub_btn = Button(window, text='-', bg='lightgrey', width=5, font=10, command=lambda: btn_press('-'))
sub_btn.grid(row=4, column=3, padx=5, pady=5)

# row 5 ===============================================================================================================

button0 = Button(window, text='0', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('0'))
button0.grid(row=5, column=0, padx=5, pady=5)

decimal = Button(window, text='.', bg='grey', fg='white', width=5, font=10, command=lambda: btn_press('.'))
decimal.grid(row=5, column=1, padx=5, pady=5)

equal_btn = Button(window, text='=', bg='gold', width=5, font=10, command=equals)
equal_btn.grid(row=5, column=2, padx=5, pady=5)

plus_btn = Button(window, text='+', bg='lightgrey', width=5, font=10, command=lambda: btn_press('+'))
plus_btn.grid(row=5, column=3, padx=5, pady=5)


window.mainloop()
# end application
