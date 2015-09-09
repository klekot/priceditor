# -*- coding: utf-8 -*-
from Tkinter import *
from codecs import *

def show_man(man_txt):
    global man
    global manual   
    with open(man_txt, 'r') as f:
        manual = f.read()
    man = Toplevel()
    man.title("Справка")
    frame_man=Frame(man, width=560, height=600)
    frame_man.pack()
    text_man = Text(frame_man, height=50,width=85,font='Arial 10',wrap=WORD)
    #text_info.place(x=9, y=9)
    text_man.pack(side='left')
    scrollbar_i = Scrollbar(frame_man)
    scrollbar_i.pack(side=RIGHT, fill=Y)
    scrollbar_i['command'] = text_man.yview
    text_man['yscrollcommand'] = scrollbar_i.set
    text_man.insert(END, manual)
    text_man.configure(state='disabled')
    # close_btn = Button(frame_man, text="Закрыть", command=man.destroy)
    # close_btn.place(x=160, y=400)
