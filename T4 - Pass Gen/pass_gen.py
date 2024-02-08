
from tkinter import *
from random import randint
from tkinter import messagebox

tk_app = Tk()
tk_app.title('PY Password Generator by Vinish')
tk_app.geometry('500x500')
tk_app.iconbitmap()
tk_app.configure(background="#7300E5")

def gen_pass():
    ent_pass.delete(0, END)
    pass_length = int(tk_entry.get())
    the_password = ""
    for item in range(pass_length):
        the_password += chr(randint(33, 126))
    ent_pass.insert(0, the_password)

def copy_pass():
    tk_app.clipboard_clear()
    tk_app.clipboard_append(ent_pass.get())
    popup()
    
def popup():
    messagebox.showinfo("Copy password", "Password is copied to clipboard")

lbl_frame = LabelFrame(tk_app, text = "Enter length of password", font = ("Helvetic", 20, "bold"))
lbl_frame.pack(pady = 20)

tk_entry = Entry(lbl_frame, font = ("Helvetica", 25))
tk_entry.pack(padx = 20, pady = 20)

btn_frame = Frame(tk_app, background="#7300E5")
btn_frame.pack(pady = 20)

gen_btn = Button(btn_frame, fg = "green", text = "Generate Strong Password", command = gen_pass)
gen_btn.grid(column = 0, row = 0, padx = 20)

output_frame = LabelFrame(tk_app, text = "Your Password!", font = ("Helvetic", 20, "bold"))
output_frame.pack(pady = 10)

ent_pass = Entry(output_frame, text = "", font = ('Helvetica', 25), bd = 0, bg = "systemButtonFace")
ent_pass.pack(pady = 20)

btn_frame = Frame(tk_app, background = "#7300E5")
btn_frame.pack(pady = 20)

clip_btn = Button(btn_frame, fg = "red", text = "Copy to Clipboard", command = copy_pass)
clip_btn.grid(column = 1, row = 0, padx = 10)

tk_app.mainloop()