from tkinter import *
from tkinter import messagebox


def ask_permission():
    messagebox.askyesno(
        message='Divas wants to chat with you',
        icon='question', title='DivaGroup')

    messagebox.askokcancel(message='Divas wants to chat with you',
                           icon='question', title='DivaGroup')


ask_permission()

top = Tk()
top.geometry("100x100")


def hello():
    messagebox.showinfo("Say Hello", "Hello World")


B1 = Button(top, text="Say Hello", command=hello)
B1.place(x=35, y=50)

top.mainloop()
