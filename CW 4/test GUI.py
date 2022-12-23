#### auther Liyang
#### date: 2022/12/22 

import tkinter as tk
from Demo1 import read_and_calculate

root=tk.Tk()

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
    U_value = read_and_calculate(K_values, ds)
    print(U_value)
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
sub_btn.grid(row=4,column=4)

# performing an infinite loop
# for the window to display
root.mainloop()
