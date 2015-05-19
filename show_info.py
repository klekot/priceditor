# -*- coding: utf-8 -*-
from Tkinter import *
from codecs import *

def show_info(info_txt):
    global info
    global information   
    with open(info_txt, 'r') as f:
        information = f.read()
    info = Toplevel()
    info.title("О программе \"Price Editor\"")
    frame_info=Frame(info, width=360, height=330)
    frame_info.pack()
    text_info = Text(frame_info, height=16,width=48,font='Arial 10',wrap=WORD)
    text_info.place(x=9, y=9)
    text_info.insert(END, information)
    text_info.configure(state='disabled')
    close_btn = Button(frame_info, text="Закрыть", command=info.destroy)
    close_btn.place(x=160, y=300)