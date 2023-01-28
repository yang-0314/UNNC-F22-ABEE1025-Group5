import tkinter.messagebox
from tkinter import *

win=Tk()    # creating the main window and storing the window object in 'win'
win.title('This is our own software!')    # setting title of the window
win.geometry('600x200')     # setting the size of the window
def start():     # def the function of the button
    win.destroy()
    tkinter.messagebox.showinfo("Greetings","\
                                Welcome to U-value Calculator! \
                                                                Authors: Liyang YU and Zesheng YANG")
btn=Button(win,text="Click Me To Know More infomation", width=50, height=5, font=('Arial',10,'bold'), command=start, 
            bg='yellow',activebackground='light yellow')
btn.place(x=95, y=50)
win.mainloop()      # running the loop that works as a trigger

import tkinter as tk 
# import the Tkinter library
from Calculator import read_and_calculate
# introduce 'readread_and_calculate' in the 'calculator' module
win = tk.Tk()
win.geometry("600x400")
# setting the size of main window 
lab = Label(win, text ='Please choose the number of layers of building material you want to analyze',
                font=('Arial',12,'bold'), width = 80, height = 13, bg = 'light blue')
lab.pack()

	#####################################################################
#### Below are the four buttons
# def the function of different button 
def run_3():
    win.destroy()
    # as soon as button 3 is pressed
    # window will be destroyed 
    root=tk.Tk()
# setting the windows' name 
    root.title("U_value Calculator")
# setting the windows size
    root.geometry("600x400")


# declaring string variable
# for storing name and password
    K_value_var=tk.StringVar()
    K_value_1_var=tk.StringVar()
    K_value_2_var=tk.StringVar()
    d_var=tk.StringVar()
    d_1_var=tk.StringVar()
    d_2_var=tk.StringVar()


# defining a function that will
# get the d and K_value
# print them on the screen
    def submit():
        K_values=[float(K_value_var.get()), float(K_value_1_var.get()), float(K_value_2_var.get())]
        ds=[float(d_var.get()), float(d_1_var.get()), float(d_2_var.get())]
        n = 3
        U_value = read_and_calculate(K_values, ds, n)
        
        print(U_value)
        tk.Label(root, text = U_value).grid(row = 4, column = 2)
        '''
        K_value_var.set("")
        d_var.set("")
        '''
	
# creating a label for
# name using widget Label
    K_value_label = tk.Label(root, text = 'K_1', font=('calibre',10, 'bold'))
    K_value_1_label = tk.Label(root, text = 'K_2', font=('calibre',10, 'bold'))
    K_value_2_label = tk.Label(root, text = 'K_3', font=('calibre',10, 'bold'))
# creating a entry for input
# name using widget Entry
    K_value_entry = tk.Entry(root,textvariable = K_value_var, font=('calibre',10,'normal'))
    K_value_1_entry = tk.Entry(root,textvariable = K_value_1_var, font=('calibre',10,'normal'))
    K_value_2_entry = tk.Entry(root,textvariable = K_value_2_var, font=('calibre',10,'normal'))
# creating a label for password
    d_label = tk.Label(root, text = 'd_1', font = ('calibre',10,'bold'))
    d_1_label = tk.Label(root, text = 'd_2', font = ('calibre',10,'bold'))
    d_2_label = tk.Label(root, text = 'd_3', font = ('calibre',10,'bold'))
# creating a entry for password
    d_entry=tk.Entry(root, textvariable = d_var, font = ('calibre',10,'normal'))
    d_1_entry=tk.Entry(root, textvariable = d_1_var, font = ('calibre',10,'normal'))
    d_2_entry=tk.Entry(root, textvariable = d_2_var, font = ('calibre',10,'normal'))
# creating the result Label
    result_Label = tk.Label(root, text = 'result', font=('calibre',10, 'bold'))
# creating a button using the widget
# Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
    K_value_label.grid(row=0,column=0)
    K_value_1_label.grid(row=1,column=0)    
    K_value_2_label.grid(row=2,column=0)
    K_value_entry.grid(row=0,column=1)
    K_value_1_entry.grid(row=1,column=1)
    K_value_2_entry.grid(row=2,column=1)
    d_label.grid(row=0,column=2)
    d_1_label.grid(row=1,column=2)
    d_2_label.grid(row=2,column=2)
    d_entry.grid(row=0,column=3)
    d_1_entry.grid(row=1,column=3)
    d_2_entry.grid(row=2,column=3)
    sub_btn.grid(row=5,column=3)
    result_Label.grid(row=4,column=1)
    
    def close_1():      # to quit the whole window
        root.destroy()
    Button = tk.Button(root, text = 'Quit', width=10, height=5, command = close_1)
    Button.place(x=400,y=20)
    root.mainloop()
    
# performing an infinite loop
# for the window to display
    root.mainloop()
    return
    
	#####################################################################
	
def run_4():
    win.destroy()
    root=tk.Tk()
# setting the windows' name 
    root.title("U_value Calculator")
# setting the windows size
    root.geometry("600x400")


# declaring string variable
# for storing name and password
    K_value_var=tk.StringVar()
    K_value_1_var=tk.StringVar()
    K_value_2_var=tk.StringVar()
    K_value_3_var=tk.StringVar()
    d_var=tk.StringVar()
    d_1_var=tk.StringVar()
    d_2_var=tk.StringVar()
    d_3_var=tk.StringVar()


# defining a function that will
# get the d and K_value
# print them on the screen
    def submit():
        K_values=[float(K_value_var.get()), float(K_value_1_var.get()),
         float(K_value_2_var.get()), float(K_value_3_var.get())]
        ds=[float(d_var.get()), float(d_1_var.get()),
         float(d_2_var.get()), float(d_3_var.get())]
        n = 4
        U_value = read_and_calculate(K_values, ds, n)
        
        print(U_value)
        tk.Label(root, text = U_value).grid(row = 4, column = 2)
        '''
        K_value_var.set("")
        d_var.set("")
        '''
	
# creating a label for
# name using widget Label
    K_value_label = tk.Label(root, text = 'K_1', font=('calibre',10, 'bold'))
    K_value_1_label = tk.Label(root, text = 'K_2', font=('calibre',10, 'bold'))
    K_value_2_label = tk.Label(root, text = 'K_3', font=('calibre',10, 'bold'))
    K_value_3_label = tk.Label(root, text = 'K_4', font=('calibre',10, 'bold'))
# creating a entry for input
# name using widget Entry
    K_value_entry = tk.Entry(root,textvariable = K_value_var, font=('calibre',10,'normal'))
    K_value_1_entry = tk.Entry(root,textvariable = K_value_1_var, font=('calibre',10,'normal'))
    K_value_2_entry = tk.Entry(root,textvariable = K_value_2_var, font=('calibre',10,'normal'))
    K_value_3_entry = tk.Entry(root,textvariable = K_value_3_var, font=('calibre',10,'normal'))
# creating a label for password
    d_label = tk.Label(root, text = 'd_1', font = ('calibre',10,'bold'))
    d_1_label = tk.Label(root, text = 'd_2', font = ('calibre',10,'bold'))
    d_2_label = tk.Label(root, text = 'd_3', font = ('calibre',10,'bold'))
    d_3_label = tk.Label(root, text = 'd_4', font = ('calibre',10,'bold'))
# creating a entry for password
    d_entry=tk.Entry(root, textvariable = d_var, font = ('calibre',10,'normal'))
    d_1_entry=tk.Entry(root, textvariable = d_1_var, font = ('calibre',10,'normal'))
    d_2_entry=tk.Entry(root, textvariable = d_2_var, font = ('calibre',10,'normal'))
    d_3_entry=tk.Entry(root, textvariable = d_3_var, font = ('calibre',10,'normal'))
# creating the result Label
    result_Label = tk.Label(root, text = 'result', font=('calibre',10, 'bold'))
# creating a button using the widget
# Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
    K_value_label.grid(row=0,column=0)
    K_value_1_label.grid(row=1,column=0)    
    K_value_2_label.grid(row=2,column=0)
    K_value_3_label.grid(row=3,column=0)

    K_value_entry.grid(row=0,column=1)
    K_value_1_entry.grid(row=1,column=1)
    K_value_2_entry.grid(row=2,column=1)
    K_value_3_entry.grid(row=3,column=1)

    d_label.grid(row=0,column=2)
    d_1_label.grid(row=1,column=2)
    d_2_label.grid(row=2,column=2)
    d_3_label.grid(row=3,column=2)

    d_entry.grid(row=0,column=3)
    d_1_entry.grid(row=1,column=3)
    d_2_entry.grid(row=2,column=3)
    d_3_entry.grid(row=3,column=3)

    sub_btn.grid(row=5,column=3)
    result_Label.grid(row=4,column=1)
    
    def close_2():   # to quit the whole window
        root.destroy()
    Button = tk.Button(root, text = 'Quit', width=10, height=5, command = close_2)
    Button.place(x=400,y=20)
    root.mainloop()
    
# performing an infinite loop
# for the window to display
    root.mainloop()    
    return

	#####################################################################

def run_5():
    win.destroy()
    root=tk.Tk()
# setting the windows' name 
    root.title("U_value Calculator")
# setting the windows size
    root.geometry("600x400")


# declaring string variable
# for storing name and password
    K_value_var=tk.StringVar()
    K_value_1_var=tk.StringVar()
    K_value_2_var=tk.StringVar()
    K_value_3_var=tk.StringVar()
    K_value_4_var=tk.StringVar()

    d_var=tk.StringVar()
    d_1_var=tk.StringVar()
    d_2_var=tk.StringVar()
    d_3_var=tk.StringVar()
    d_4_var=tk.StringVar()


# defining a function that will
# get the d and K_value
# print them on the screen
    def submit():
        K_values=[float(K_value_var.get()), float(K_value_1_var.get()),
         float(K_value_2_var.get()), float(K_value_3_var.get()),
         float(K_value_4_var.get())]
        ds=[float(d_var.get()), float(d_1_var.get()),
         float(d_2_var.get()), float(d_3_var.get()),
         float(d_4_var.get())]
        U_value = read_and_calculate(K_values, ds, n)
        n = 5 
        print(U_value)
        tk.Label(root, text = U_value).grid(row = 4, column = 2)
        '''
        K_value_var.set("")
        d_var.set("")
        '''
	
# creating a label for
# name using widget Label
    K_value_label = tk.Label(root, text = 'K_1', font=('calibre',10, 'bold'))
    K_value_1_label = tk.Label(root, text = 'K_2', font=('calibre',10, 'bold'))
    K_value_2_label = tk.Label(root, text = 'K_3', font=('calibre',10, 'bold'))
    K_value_3_label = tk.Label(root, text = 'K_4', font=('calibre',10, 'bold'))
    K_value_4_label = tk.Label(root, text = 'K_5', font=('calibre',10, 'bold'))
# creating a entry for input
# name using widget Entry
    K_value_entry = tk.Entry(root,textvariable = K_value_var, font=('calibre',10,'normal'))
    K_value_1_entry = tk.Entry(root,textvariable = K_value_1_var, font=('calibre',10,'normal'))
    K_value_2_entry = tk.Entry(root,textvariable = K_value_2_var, font=('calibre',10,'normal'))
    K_value_3_entry = tk.Entry(root,textvariable = K_value_3_var, font=('calibre',10,'normal'))
    K_value_4_entry = tk.Entry(root,textvariable = K_value_4_var, font=('calibre',10,'normal'))
# creating a label for password
    d_label = tk.Label(root, text = 'd_1', font = ('calibre',10,'bold'))
    d_1_label = tk.Label(root, text = 'd_2', font = ('calibre',10,'bold'))
    d_2_label = tk.Label(root, text = 'd_3', font = ('calibre',10,'bold'))
    d_3_label = tk.Label(root, text = 'd_4', font = ('calibre',10,'bold'))
    d_4_label = tk.Label(root, text = 'd_5', font = ('calibre',10,'bold'))
# creating a entry for password
    d_entry=tk.Entry(root, textvariable = d_var, font = ('calibre',10,'normal'))
    d_1_entry=tk.Entry(root, textvariable = d_1_var, font = ('calibre',10,'normal'))
    d_2_entry=tk.Entry(root, textvariable = d_2_var, font = ('calibre',10,'normal'))
    d_3_entry=tk.Entry(root, textvariable = d_3_var, font = ('calibre',10,'normal'))
    d_4_entry=tk.Entry(root, textvariable = d_4_var, font = ('calibre',10,'normal'))
# creating the result Label
    result_Label = tk.Label(root, text = 'result', font=('calibre',10, 'bold'))
# creating a button using the widget
# Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
    K_value_label.grid(row=0,column=0)
    K_value_1_label.grid(row=1,column=0)    
    K_value_2_label.grid(row=2,column=0)
    K_value_3_label.grid(row=3,column=0)
    K_value_4_label.grid(row=4,column=0)

    K_value_entry.grid(row=0,column=1)
    K_value_1_entry.grid(row=1,column=1)
    K_value_2_entry.grid(row=2,column=1)
    K_value_3_entry.grid(row=3,column=1)
    K_value_4_entry.grid(row=4,column=1)

    d_label.grid(row=0,column=2)
    d_1_label.grid(row=1,column=2)
    d_2_label.grid(row=2,column=2)
    d_3_label.grid(row=3,column=2)
    d_4_label.grid(row=4,column=2)

    d_entry.grid(row=0,column=3)
    d_1_entry.grid(row=1,column=3)
    d_2_entry.grid(row=2,column=3)
    d_3_entry.grid(row=3,column=3)
    d_4_entry.grid(row=4,column=3)

    sub_btn.grid(row=5,column=3)
    result_Label.grid(row=6,column=1)
    
    def close_3():      # to quit the whole window
        root.destroy()
    Button = tk.Button(root, text = 'Quit', width=10, height=5, command = close_3)
    Button.place(x=400,y=20)
    root.mainloop()
    
# performing an infinite loop
# for the window to display
    root.mainloop()    
    return
    
	#######################################################
	
def run_5():
    win.destroy()
    root=tk.Tk()
# setting the windows' name 
    root.title("U_value Calculator")
# setting the windows size
    root.geometry("600x400")


# declaring string variable
# for storing name and password
    K_value_var=tk.StringVar()
    K_value_1_var=tk.StringVar()
    K_value_2_var=tk.StringVar()
    K_value_3_var=tk.StringVar()
    K_value_4_var=tk.StringVar()
    K_value_5_var=tk.StringVar()

    d_var=tk.StringVar()
    d_1_var=tk.StringVar()
    d_2_var=tk.StringVar()
    d_3_var=tk.StringVar()
    d_4_var=tk.StringVar()
    d_5_var=tk.StringVar()


# defining a function that will
# get the d and K_value
# print them on the screen
    def submit():
        K_values=[float(K_value_var.get()), float(K_value_1_var.get()),
         float(K_value_2_var.get()), float(K_value_3_var.get()),
         float(K_value_4_var.get()),float(K_value_5_var.get())]
        ds=[float(d_var.get()), float(d_1_var.get()),
         float(d_2_var.get()), float(d_3_var.get()),
         float(d_4_var.get()), float(d_5_var.get())]
        n = 6
        U_value = read_and_calculate(K_values, ds, n)
        
        print(U_value)
        tk.Label(root, text = U_value).grid(row = 4, column = 2)
        '''
        K_value_var.set("")
        d_var.set("")
        '''
	
# creating a label for
# name using widget Label
    K_value_label = tk.Label(root, text = 'K_1', font=('calibre',10, 'bold'))
    K_value_1_label = tk.Label(root, text = 'K_2', font=('calibre',10, 'bold'))
    K_value_2_label = tk.Label(root, text = 'K_3', font=('calibre',10, 'bold'))
    K_value_3_label = tk.Label(root, text = 'K_4', font=('calibre',10, 'bold'))
    K_value_4_label = tk.Label(root, text = 'K_5', font=('calibre',10, 'bold'))
    K_value_5_label = tk.Label(root, text = 'K_6', font=('calibre',10, 'bold'))
# creating a entry for input
# name using widget Entry
    K_value_entry = tk.Entry(root,textvariable = K_value_var, font=('calibre',10,'normal'))
    K_value_1_entry = tk.Entry(root,textvariable = K_value_1_var, font=('calibre',10,'normal'))
    K_value_2_entry = tk.Entry(root,textvariable = K_value_2_var, font=('calibre',10,'normal'))
    K_value_3_entry = tk.Entry(root,textvariable = K_value_3_var, font=('calibre',10,'normal'))
    K_value_4_entry = tk.Entry(root,textvariable = K_value_4_var, font=('calibre',10,'normal'))
    K_value_5_entry = tk.Entry(root,textvariable = K_value_5_var, font=('calibre',10,'normal'))
# creating a label for password
    d_label = tk.Label(root, text = 'd_1', font = ('calibre',10,'bold'))
    d_1_label = tk.Label(root, text = 'd_2', font = ('calibre',10,'bold'))
    d_2_label = tk.Label(root, text = 'd_3', font = ('calibre',10,'bold'))
    d_3_label = tk.Label(root, text = 'd_4', font = ('calibre',10,'bold'))
    d_4_label = tk.Label(root, text = 'd_5', font = ('calibre',10,'bold'))
    d_5_label = tk.Label(root, text = 'd_6', font = ('calibre',10,'bold'))
# creating a entry for password
    d_entry=tk.Entry(root, textvariable = d_var, font = ('calibre',10,'normal'))
    d_1_entry=tk.Entry(root, textvariable = d_1_var, font = ('calibre',10,'normal'))
    d_2_entry=tk.Entry(root, textvariable = d_2_var, font = ('calibre',10,'normal'))
    d_3_entry=tk.Entry(root, textvariable = d_3_var, font = ('calibre',10,'normal'))
    d_4_entry=tk.Entry(root, textvariable = d_4_var, font = ('calibre',10,'normal'))
    d_5_entry=tk.Entry(root, textvariable = d_5_var, font = ('calibre',10,'normal'))
# creating the result Label
    result_Label = tk.Label(root, text = 'result', font=('calibre',10, 'bold'))
# creating a button using the widget
# Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
    K_value_label.grid(row=0,column=0)
    K_value_1_label.grid(row=1,column=0)    
    K_value_2_label.grid(row=2,column=0)
    K_value_3_label.grid(row=3,column=0)
    K_value_4_label.grid(row=4,column=0)
    K_value_5_label.grid(row=5,column=0)

    K_value_entry.grid(row=0,column=1)
    K_value_1_entry.grid(row=1,column=1)
    K_value_2_entry.grid(row=2,column=1)
    K_value_3_entry.grid(row=3,column=1)
    K_value_4_entry.grid(row=4,column=1)
    K_value_5_entry.grid(row=5,column=1)

    d_label.grid(row=0,column=2)
    d_1_label.grid(row=1,column=2)
    d_2_label.grid(row=2,column=2)
    d_3_label.grid(row=3,column=2)
    d_4_label.grid(row=4,column=2)
    d_5_label.grid(row=5,column=2)

    d_entry.grid(row=0,column=3)
    d_1_entry.grid(row=1,column=3)
    d_2_entry.grid(row=2,column=3)
    d_3_entry.grid(row=3,column=3)
    d_4_entry.grid(row=4,column=3)
    d_5_entry.grid(row=5,column=3)

    sub_btn.grid(row=6,column=3)
    result_Label.grid(row=6,column=1)
    
    def close_4():      # to quit the whole window
        root.destroy()
    Button = tk.Button(root, text = 'Quit', width=10, height=5, command = close_4)
    Button.place(x=400,y=20)
    root.mainloop()
    
# performing an infinite loop
# for the window to display
    root.mainloop()    
    return
########################################################################

choose_but_1 = tk.Button(win, text = '3', width=10, height=5, command = run_3)
choose_but_2 = tk.Button(win, text = '4', width=10, height=5, command = run_3)
choose_but_3 = tk.Button(win, text = '5', width=10, height=5, command = run_4)
choose_but_4 = tk.Button(win, text = '6', width=10, height=5, command = run_5)
choose_but_1.place(relx = 0.1, rely = 0.7)
choose_but_2.place(relx = 0.3, rely = 0.7)
choose_but_3.place(relx = 0.5, rely = 0.7)
choose_but_4.place(relx = 0.7, rely = 0.7)
win.mainloop()
