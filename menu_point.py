from Tkinter import *

def menu_point(event):
    widget = event.widget
    selection=widget.curselection()
    menu_point = widget.get(selection[0])
    return menu_point