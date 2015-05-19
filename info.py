# -*- coding: utf-8 -*-
from Tkinter import *
from codecs import *

from loading_arrs import *
from full_path_show import *
from categories import *
from autofill_names import *

root1 = Tk()
def close_info():
    root1.destroy()

def info():
    info = Toplevel(root1)
    info.grab_set()
    frame_info=Frame(info, width=350, height=120)
    frame_info.pack()
    info_label = Label(frame_info, text="Price Editor (version 1.6)")
    info_label.place(x=20, y=10)
    close_btn = Button(frame_info, text="Закрыть", command=close_info)
    close_btn.place(x=130, y=90)
    root1.mainloop()
