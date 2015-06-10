# -*- coding: utf-8 -*-
from Tkinter import *
from codecs import *
from modules.parse_db_ini import *
from modules.show_open_db import *

def save_destroy(db_ini_file, hostname_entry, database_entry, db_user_entry, \
                 db_pass_entry, default_db, db_set, cur_db_strvar, frame0):
    hostname   = hostname_entry.get() # 'localhost'
    database   = database_entry.get() # 'poliinfo_bitrix'
    db_user    = db_user_entry.get()  # 'poliinfo_bitrix'
    db_pass    = db_pass_entry.get()  # 'Y2Gd75q'
    if default_db.get() != 0:
        def_hostname = hostname
        def_database = database
        def_db_user  = db_user
        def_db_pass  = db_pass
        with open(db_ini_file, 'w') as db_ini:
            db_ini.write("WARNING!!! Do not change order of strings below\n\
to prevent from lost connection with working database.\n\
Program logic is depends of every string position!\n\
\n\
[default]\n\
\n\
" + def_hostname + "\n\
" + def_database + "\n\
" + def_db_user + "\n\
" + def_db_pass + "\n\
\n\
[current]\n\
\n\
" + hostname + "\n\
" + database + "\n\
" + db_user + "\n\
" + db_pass)
    else:
        def_hostname = parse_db_ini(db_ini_file)[0]
        def_database = parse_db_ini(db_ini_file)[1]
        def_db_user  = parse_db_ini(db_ini_file)[2]
        def_db_pass  = parse_db_ini(db_ini_file)[3]
        with open(db_ini_file, 'w') as db_ini:
            db_ini.write("WARNING!!! Do not change order of strings below\n\
to prevent from lost connection with working database.\n\
Program logic is depends of every string position!\n\
\n\
[default]\n\
\n\
" + def_hostname + "\n\
" + def_database + "\n\
" + def_db_user + "\n\
" + def_db_pass + "\n\
\n\
[current]\n\
\n\
" + hostname + "\n\
" + database + "\n\
" + db_user + "\n\
" + db_pass)
    cur_db_strvar.set(database + " @ " + hostname)
    db_set.destroy()
    show_open_db(cur_db_strvar, frame0)  
def show_pass(db_pass_btn_text, db_pass_entry, db_pass_v, db_set, db_pass_btn):
    def sh_p1():
        show_pass(db_pass_btn_text, db_pass_entry, db_pass_v, db_set, db_pass_btn)  
    def sh_p2():
        show_pass(db_pass_btn_text, db_pass_entry, db_pass_v, db_set, db_pass_btn)
    if db_pass_btn_text == "Показать":
        db_pass_entry.destroy()
        db_pass_btn_text = "Скрывать"
        db_pass_entry = Entry(db_set, textvariable=db_pass_v, width=24, font='Arial 10')
        db_pass_entry.place(x=150, y=140)
        db_pass_btn.destroy()
        db_pass_btn = Button(db_set, text=db_pass_btn_text, command=sh_p1)
        db_pass_btn.place(x=328, y=139)
    else:
        db_pass_entry.destroy()
        db_pass_btn_text = "Показать"
        bullet = '*'
        db_pass_entry = Entry(db_set, textvariable=db_pass_v, width=24, font='Arial 10', show=bullet)
        db_pass_entry.place(x=150, y=140)
        db_pass_btn.destroy()
        db_pass_btn = Button(db_set, text=db_pass_btn_text, command=sh_p2)
        db_pass_btn.place(x=328, y=139)

def db_settings(db_ini_file, cur_db_strvar, frame0):
    default_db = IntVar()
    def sd():
        save_destroy(db_ini_file, hostname_entry, database_entry, db_user_entry, \
                 db_pass_entry, default_db, db_set, cur_db_strvar, frame0)
    def sh_p():
        show_pass(db_pass_btn_text, db_pass_entry, db_pass_v, db_set, db_pass_btn)
    db_set = Toplevel()
    db_set.title("Настройка базы данных")
    db_set_frame=Frame(db_set, width=400, height=250)
    db_set_frame.pack()
    current_label = Label(db_set, text='Текущие настройки: ')
    current_label.place(x=10, y=10)
    cur_db_label = Label(db_set, textvariable=cur_db_strvar)
    cur_db_label.config(fg='red', font='Arial 13')
    cur_db_label.place(x=150, y=10)
    hostname_label = Label(db_set, text='IP-адрес хоста: ')
    hostname_label.place(x=10, y=50)
    hostname_v = StringVar()
    hostname_v.set(parse_db_ini(db_ini_file)[0])
    hostname_entry = Entry(db_set, textvariable=hostname_v, width=33, font='Arial 10')
    hostname_entry.place(x=150, y=50)
    database_label = Label(db_set, text='Имя базы данных: ')
    database_label.place(x=10, y=80)
    database_v = StringVar()
    database_v.set(parse_db_ini(db_ini_file)[1])
    database_entry = Entry(db_set, textvariable=database_v, width=33, font='Arial 10')
    database_entry.place(x=150, y=80)
    db_user_label  = Label(db_set, text='Имя пользователя: ')
    db_user_label.place(x=10, y=110)
    db_user_v = StringVar()
    db_user_v.set(parse_db_ini(db_ini_file)[2])
    db_user_entry = Entry(db_set, textvariable=db_user_v, width=33, font='Arial 10')
    db_user_entry.place(x=150, y=110)
    db_pass_label  = Label(db_set, text='Пароль пользователя: ')
    db_pass_label.place(x=10, y=140)
    db_pass_v = StringVar()
    db_pass_v.set(parse_db_ini(db_ini_file)[3])
    db_pass_btn_text = "Показать"
    bullet = '*'
    db_pass_entry = Entry(db_set, textvariable=db_pass_v, width=24, font='Arial 10', show=bullet)
    db_pass_entry.place(x=150, y=140)

    db_pass_btn = Button(db_set, text=db_pass_btn_text, command=sh_p)
    db_pass_btn.place(x=328, y=139)
    
    default_check = Checkbutton(db_set, text='Использовать по умолчанию', variable=default_db)
    default_check.place(x=145, y=190)
    
    close_btn = Button(db_set, text="Сохранить и закрыть", command=sd)
    close_btn.place(x=150, y=220)