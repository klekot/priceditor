# -*- coding: utf-8 -*-
from Tkinter import *
from codecs import *

def db_settings(db_ini_file):
    global hostname
    global database
    global db_user
    global db_pass
    default_db = IntVar()
    with open(db_ini_file, 'r') as db_ini:
        db_set_arr = [s for s in db_ini.read().split('\n')]
    hostname = db_set_arr[0]
    database = db_set_arr[1]
    db_user  = db_set_arr[2]
    db_pass  = db_set_arr[3]
    
    def save_destroy():
        global cur_db_var
        hostname   = hostname_entry.get() # 'localhost'
        database   = database_entry.get() # 'poliinfo_bitrix'
        db_user    = db_user_entry.get()  # 'poliinfo_bitrix'
        db_pass    = db_pass_entry.get()  # 'Y2Gd75q'
        cur_db_var = database + ' @ ' + hostname
        if default_db.get() != 0:
            pass
        db_set.destroy()
    
    db_set = Toplevel()
    db_set.title("Настройка базы данных")
    db_set_frame=Frame(db_set, width=400, height=250)
    db_set_frame.pack()
    cur_db_var = database + ' @ ' + hostname
    current_label = Label(db_set, text='Текущие настройки: ')
    current_label.place(x=10, y=10)
    cur_db_label = Label(db_set, text=cur_db_var)
    cur_db_label.config(fg='red', font='Arial 13')
    cur_db_label.place(x=150, y=10)
    hostname_label = Label(db_set, text='IP-адрес хоста: ')
    hostname_label.place(x=10, y=50)
    hostname_entry = Entry(db_set, width=33, font='Arial 10')
    hostname_entry.place(x=150, y=50)
    database_label = Label(db_set, text='Имя базы данных: ')
    database_label.place(x=10, y=80)
    database_entry = Entry(db_set, width=33, font='Arial 10')
    database_entry.place(x=150, y=80)
    db_user_label  = Label(db_set, text='Имя пользователя: ')
    db_user_label.place(x=10, y=110)
    db_user_entry = Entry(db_set, width=33, font='Arial 10')
    db_user_entry.place(x=150, y=110)
    db_pass_label  = Label(db_set, text='Пароль пользователя: ')
    db_pass_label.place(x=10, y=140)
    db_pass_entry = Entry(db_set, width=33, font='Arial 10')
    db_pass_entry.place(x=150, y=140)
    
    default_check = Checkbutton(db_set, text='Использовать по умолчанию', variable=default_db)
    default_check.place(x=145, y=190)
    
    close_btn = Button(db_set, text="Сохранить и закрыть", command=save_destroy)
    close_btn.place(x=150, y=220)