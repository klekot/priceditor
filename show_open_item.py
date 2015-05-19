from Tkinter import *

def show_open_item(v, query, frame0):
    v.set(query)
    open_item = Label(frame0, textvariable=v, fg="blue", font=("Helvetica", 16))
    open_item.place(x=680, y=7)