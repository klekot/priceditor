from Tkinter import *

def show_open_db(cur_db_strvar, frame0):
    current_db_label = Label(frame0, textvariable=cur_db_strvar)
    current_db_label.config(fg='red')
    current_db_label.place(x=1063, y=677)