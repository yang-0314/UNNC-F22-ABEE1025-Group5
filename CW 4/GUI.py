import  tkinter.messagebox
from tkinter import * 

win = Tk()
win.title('welcome')
win.geometry('500x200')
def fun_start ():
    tkinter.messagebox.showinfo('welcome', 
    "hello welcome to use the 'U_value'calculater")
btn = Button (win,text="Start",command=fun_start)
btn.place(x=200,y=20)
win.mainloop()