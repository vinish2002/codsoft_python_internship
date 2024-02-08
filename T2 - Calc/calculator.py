
from tkinter import *

tk_calc = Tk()
tk_calc.title("PY Calc by Vinish")
tk_calc.iconbitmap()
tk_calc.config(background="#00FFDF")
tk_calc.resizable(True, True)

def click(num):
    exp = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(exp) + str(num))

def add_btn():
    first_num = entry_field.get()
    global expression
    global operation
    operation = "add"
    expression = int(first_num)
    entry_field.delete(0, END)


def subt_btn():
    first_num = entry_field.get()
    global expression
    global operation
    operation = "subtract"
    expression = int(first_num)
    entry_field.delete(0, END)


def mul_btn():
    first_num = entry_field.get()
    global expression
    global operation
    operation = "multiply"
    expression = int(first_num)
    entry_field.delete(0, END)

def div_btn():
    first_num = entry_field.get()
    global expression
    global operation
    operation = "divide"
    expression = int(first_num)
    entry_field.delete(0, END)

def clear():
    entry_field.delete(0, END)

def equal_btn():
    second_num = entry_field.get()
    entry_field.delete(0, END)
    if operation == "add":
        entry_field.insert(0, expression + int(second_num))
    elif operation == "subtract":
        entry_field.insert(0, expression - int(second_num))
    elif operation == "multiply":
        entry_field.insert(0, expression * int(second_num))
    elif operation == "divide":
        result = expression / int(second_num)
        if (expression % int(second_num) == 0):
            entry_field.insert(0, int(result))
        else:
            entry_field.insert(0, result)
    else:
        entry_field.insert("error")

entry_field = Entry(tk_calc, width = 35, justify="right", borderwidth = 6)
entry_field.grid(row=0, column=0, columnspan=3, ipadx=10, pady=15)

num_0 = Button(tk_calc, borderwidth=3, text="0", height=1, width=7, padx=20, pady=10, command=lambda:click(0))
num_1 = Button(tk_calc, borderwidth=3, text="1", height=1, width=7, padx=20, pady=10, command=lambda:click(1))
num_2 = Button(tk_calc, borderwidth=3, text="2", height=1, width=7, padx=20, pady=10, command=lambda:click(2))
num_3 = Button(tk_calc, borderwidth=3, text="3", height=1, width=7, padx=20, pady=10, command=lambda:click(3))
num_4 = Button(tk_calc, borderwidth=3, text="4", height=1, width=7, padx=20, pady=10, command=lambda:click(4))
num_5 = Button(tk_calc, borderwidth=3, text="5", height=1, width=7, padx=20, pady=10, command=lambda:click(5))
num_6 = Button(tk_calc, borderwidth=3, text="6", height=1, width=7, padx=20, pady=10, command=lambda:click(6))
num_7 = Button(tk_calc, borderwidth=3, text="7", height=1, width=7, padx=20, pady=10, command=lambda:click(7))
num_8 = Button(tk_calc, borderwidth=3, text="8", height=1, width=7, padx=20, pady=10, command=lambda:click(8))
num_9 = Button(tk_calc, borderwidth=3, text="9", height=1, width=7, padx=20, pady=10, command=lambda:click(9))

btn_add = Button(tk_calc, borderwidth=3, text="+", height=1, width=7, padx=20, pady=10, command=add_btn)
btn_subtract = Button(tk_calc, borderwidth=3, text="-", height=1, width=7, padx=20, pady=10, command=subt_btn)
btn_divide = Button(tk_calc, borderwidth=3, text="/", height=1, width=7, padx=20, pady=10, command=div_btn)
btn_multiply = Button(tk_calc, borderwidth=3, text="x", height=1, width=7, padx=20, pady=10, command=mul_btn)
btn_equal = Button(tk_calc, borderwidth=3, text="=", height=1, width=7, padx=70, pady=10, command=equal_btn)
btn_clear = Button(tk_calc, borderwidth=3, text="clear", height=1, width=7, padx=70, pady=10, command=clear)

num_0.grid(row=4, column=0)
num_1.grid(row=3, column=0)
num_2.grid(row=3, column=1)
num_3.grid(row=3, column=2)
num_4.grid(row=2, column=0)
num_5.grid(row=2, column=1)
num_6.grid(row=2, column=2)
num_7.grid(row=1, column=0)
num_8.grid(row=1, column=1)
num_9.grid(row=1, column=2)

btn_add.grid(row=4, column=1)
btn_subtract.grid(row=4, column=2)
btn_multiply.grid(row=5, column=0)
btn_divide.grid(row=6, column=0)
btn_equal.grid(row=5, column=1, columnspan=2)
btn_clear.grid(row=6, column=1, columnspan=2)

tk_calc.mainloop()