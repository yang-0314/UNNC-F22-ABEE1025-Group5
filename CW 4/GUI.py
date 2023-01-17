from tkinter import messagebox as mb
from tkinter import * 

win = Tk()

win.title('welcome')
win.geometry('500x200')
def fun_start ():
    res = mb.askquestion('calculater','Confirme your value')

    if res == 'yes':
        win.destroy()
        root = Tk()
         
    return
    tkinter.messagebox.showinfo('welcome', 
    "hello welcome to use the 'U_value'calculater")
btn = Button (win,text="Start",command=fun_start)
btn.place(x=200,y=20)
win.mainloop()