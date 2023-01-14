# First of all, be aware the basics of program
# Note1: This project is based on '2' value/number calculation; you can't calculate MORE THAN 2 at the same time 
# Note2: Press Clear after every calculation
# Note3: This calculator is built using a very basic method


# ==================================================
from tkinter import *
root = Tk()
root.title('Simple Calculator')
e = Entry(root, width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)
root.configure(bg="#242829")

# Making Functions of Symbols
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0,END)
    
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_clear():
    e.delete(0, END)

# Defining Buttons & Positioning them on the screen

Button1 = Button(root, text = '1',padx= 40, pady= 20,
                command=lambda: button_click(1),
                bg='#554d4d',fg='white').grid(row=4, column=0)
Button2 = Button(root, text = '2',padx= 40, pady= 20,
                command=lambda: button_click(2),
                bg='#554d4d',fg='white').grid(row=4, column=1)
Button3 = Button(root, text = '3',padx= 40, pady= 20,
                command=lambda: button_click(3),
                bg='#554d4d',fg='white').grid(row=4, column=2)

Button4 = Button(root, text = '4',padx= 40, pady= 20,
                command=lambda: button_click(4),
                bg='#554d4d',fg='white').grid(row=3, column=0)
Button5 = Button(root, text = '5',padx= 40, pady= 20,
                command=lambda: button_click(5),
                bg='#554d4d',fg='white').grid(row=3, column=1)
Button6 = Button(root, text = '6',padx= 40, pady= 20,
                command=lambda: button_click(6),
                bg='#554d4d',fg='white').grid(row=3, column=2)

Button7 = Button(root, text = '7',padx= 40, pady= 20,
                command=lambda: button_click(7),
                bg='#554d4d',fg='white').grid(row=2, column=0)
Button8 = Button(root, text = '8',padx= 40, pady= 20,
                command=lambda: button_click(8),
                bg='#554d4d',fg='white').grid(row=2, column=1)
Button9 = Button(root, text = '9',padx= 40, pady= 20,
                command=lambda: button_click(9),
                bg='#554d4d',fg='white').grid(row=2, column=2)

Button0 = Button(root, text = '0',padx= 40, pady= 20.5,
                command=lambda: button_click(0),
                bg='#554d4d',fg='white').grid(row=5, column=0)

Button_clear = Button(root, text = 'Clear',padx= 40, pady= 20, command=button_clear,
bg='#554d4d',fg='white').grid(row=2, column=3)
Button_add = Button(root, text = '+',font=('Arial',23),padx= 35, pady= 3, command=button_add,
bg='#554d4d',fg='white').grid(row=3, column=3)
Button_sub = Button(root, text = '−',font=('Arial',23),padx= 35, pady= 3, command=button_subtract,
bg='#554d4d',fg='white').grid(row=4, column=3)
Button_multi = Button(root, text = '×',font=('Arial',23),padx= 26, pady= 3, command=button_multiply,
bg='#554d4d',fg='white').grid(row=5, column=1)
Button_divi = Button(root, text = '÷',font=('Arial',23),padx= 26, pady= 3, command=button_divide,
bg='#554d4d',fg='white').grid(row=5, column=2)
Button_equal = Button(root, text = '=',font=('Arial',23),padx= 35, pady= 3, command=button_equal,
bg='#554d4d',fg='white').grid(row=5, column=3)



root.mainloop()