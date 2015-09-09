from Tkinter import *
import os

def full_path_show(frame0, fn):
    w = Label(frame0, text=os.path.abspath(fn), fg="blue")
    w.place(x=135, y=680)
