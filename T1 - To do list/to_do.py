#Python program for creating a TO-DO list

import os
import pickle
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog

th_root = Tk()
th_root.title('To-Do List with PYTHON by Vinish')
th_root.iconbitmap()
th_root.geometry("700x500")
th_root.configure(background='#39EAD4')

fonts = Font(
    family='Comic Sans MS',
    size=30,
    weight='normal'
)

tk_frame = Frame(th_root)
tk_frame.pack(pady=10)

tk_list = Listbox(
    tk_frame,
    font = fonts,
    width = 25,
    height = 5,
    bg = "SystemButtonFace",
    bd = 0,
    fg = "#464646",
    highlightthickness = 0,
    selectbackground = "#0B3737",
    activestyle = "none"
)

tk_list.pack(side="left", fill="both")

dupe_list = ["Set Alarm", "Go to walk", "Play football", "Have breakfast"]

for task in dupe_list:
    tk_list.insert(END, task)

def add_task():
    tk_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def delete_task():
    tk_list.delete(ANCHOR)

def cross_out_task():
    tk_list.itemconfig(
        tk_list.curselection(),
        fg = "#dedede"
    )
    
    tk_list.selection_clear(0, END)

def uncross_out_task():
    tk_list.itemconfig(
        tk_list.curselection(),
        fg = "#464646"
    )
    tk_list.selection_clear(0, END)
    
def delete_crossed_task():
    count = 0
    while count < tk_list.size():
        if tk_list.itemcget(count, "fg") == "#dedede":
            tk_list.delete(tk_list.index(count))
        else:
            count += 1

def save_list():
    path = os.getcwd()

    file_name = filedialog.asksaveasfilename(
        initialdir = "path",
        title = "Save File",
        filetypes = (
            ("Dat Files", ".dat"),
            ("All Files", "*.*")
        )
    )

    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

    delete_crossed_task()
    tasks = tk_list.get(0, END)
    output_file = open(file_name, 'wb')
    pickle.dump(tasks, output_file)

def del_list():
    tk_list.delete(0, END)
 
def open_list():
    file_name = filedialog.askopenfilename(
        initialdir = "path",
        title = "Open File",
        filetypes = (
            ("Dat Files", ".dat"),
            ("All Files", "*.*")
        )
    )
    if file_name:
        tk_list.delete(0, END)
        file_input = open(file_name, 'rb')
        stuff = pickle.load(file_input)
        for task in stuff:
            tk_list.insert(END, task)

my_scrollbar = Scrollbar(tk_frame)
my_scrollbar.pack(side="right", fill="both")


tk_list.config(yscrollcommand = my_scrollbar)
my_scrollbar.config(command = tk_list.yview)

my_entry = Entry(th_root, font=("Helvetica", 20), width=30)
my_entry.pack(pady = 20)

button_frame = Frame(th_root, bg='#39EAD4')
button_frame.pack(pady = 20)

delete_button = Button(button_frame, background = '#A20A0A', text = "Delete Task",  fg = 'white', command=delete_task)
add_button = Button(button_frame, background ='#39EA56', text = "Add Task", fg = 'black', command = add_task)
cross_out_button = Button(button_frame, background = '#D7EA39', text = "Cross-Out Task", fg = 'black', command = cross_out_task)
uncross_out_button = Button(button_frame, background = '#0A6DA2', text = "Uncross-Out Task", fg = 'white', command = uncross_out_task)
delete_crossed_button = Button(button_frame, background = '#EA3944', text = "Delete Crossed-Out Task", fg = 'white', command = delete_crossed_task)

delete_button.grid(row = 0, column = 0, padx = 20)
add_button.grid(row = 0, column = 1, padx = 20)
cross_out_button.grid(row = 0, column = 2, padx = 20)
uncross_out_button.grid(row = 0, column = 3, padx = 20)
delete_crossed_button.grid(row = 0, column = 4, padx = 20)

tk_menu = Menu(th_root)
th_root.config(menu = tk_menu)

file_menu = Menu(tk_menu, tearoff = False)
tk_menu.add_cascade(label="File", menu = file_menu)

file_menu.add_command(label="Open...", command = open_list)
file_menu.add_command(label="Save list", command = save_list)
file_menu.add_command(label="Clear list", command = del_list)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = th_root.quit)

help_menu = Menu(tk_menu)
tk_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")
help_menu.add_command(label="Contact")

th_root.mainloop()