# -*- coding: utf-8 -*-
import os
import xlrd
from xlwt import Workbook
from xlwt import easyxf
from xlutils.copy import copy
from Tkinter import *
import ttk
import tkFileDialog
import sys
from codecs import *
import webbrowser
import ImageTk
import PIL.Image
import requests
from StringIO import StringIO

#################################################### now let's plug my own modules ####################################################
from modules import AutocompleteEntry
from modules.tree_cats import *
from modules.html_show import *
from modules.item_path_show import *
from modules.show_empty import *
from modules.show_open_item import *
from modules.list_to_search import *
from modules.loading_arrs import *
from modules.full_path_show import *
from modules.autofill_names import *
from modules.menu_point import *
from modules.items import *
from modules.level_1_items import *
from modules.level_2_items import *
from modules.level_3_items import *
from modules.categories import *
from modules.back_show import *
from modules.search import *
from modules.page_design import *
from modules.show_info import *

####################################################### Inner functions definitions ###################################################
def apply_design():
    page_design(frameZ, pages, explain_col, names_col, short_col, img_col, pdf_col, include_col, \
        dim_col, schm1_col, schm2_col, attention_col, params_col, template_file, template_fill)

def OpenUrl(url):
    webbrowser.open_new(url)

def plug_red_from_menu():
    global sw
    sw = 1
    optmenu.delete(0, 1)
    optmenu.add_command(label="Скрывать незаполненные позиции", command=unplug_red_from_menu)
    #optmenu.add_command(label="Показывать незаполненные позиции", command=plug_red_from_menu)
    optmenu.add_command(label="Обновить дизайн всех элементов", command=apply_design)
    
def unplug_red_from_menu():
    global sw
    sw = 0
    optmenu.delete(0, 1)
    #optmenu.add_command(label="Скрывать незаполненные позиции", command=unplug_red_from_menu)
    optmenu.add_command(label="Показывать незаполненные позиции", command=plug_red_from_menu)
    optmenu.add_command(label="Обновить дизайн всех элементов", command=apply_design)
  
def Quit():
    global root
    root.destroy()
       
def LoadFile():
    global fn
    global book
    global sh

    fn = tkFileDialog.Open(root, filetypes = [('*.xls files', '.xls')]).show()
    if fn == '':
        return
    book = xlrd.open_workbook(fn, 'rt' ,formatting_info=True)
    sh = book.sheet_by_index(0)
    loading_arrs(sh, names_col, explain_col, all_cats, img_col, pdf_col, short_col, include_col, \
                dim_col, schm1_col, schm2_col, attention_col, params_col, frame0)
    full_path_show(frame0, fn)
    categories(all_cats, level_0, call_level_1, call_items0)
    autofill_names(names_col, names_list, e)
    apply_design()
    load_template()

def CloseFile():
    names_list     = []
    names_col      = []
    explain_col    = []
    img_col        = []
    pdf_col        = []
    short_col      = []
    pages          = []
    include_col    = []
    dim_col        = []
    schm1_col      = []
    schm2_col      = []
    attention_col  = []
    params_col     = []
    all_cats       = [[],[],[],[],[]]
    frame0.pack_forget()

def SaveFile():
    fns = tkFileDialog.SaveAs(root, filetypes = [('*.xls files', '.xls')]).show()
    if fns == '':
        return
    wb = copy(book)
    w_sheet = wb.get_sheet(0)
    plain = easyxf('')
    for i,cell in enumerate(sh.col(112)):
        if not i or i<10: # to take unchanged rows of headers of file of price
            continue
        if type(explain_col[i])==str:
            w_sheet.write(i,112,explain_col[i].decode('utf-8', errors='replace'),plain)
        else:
            w_sheet.write(i,112,explain_col[i],plain)

    for i,cell in enumerate(sh.col(104)):
        if not i or i<10:
            continue
        if type(img_col[i])==str:
            w_sheet.write(i,104,img_col[i].decode('utf-8', errors='replace'),plain)
        else:
            w_sheet.write(i,104,img_col[i],plain)

    for i,cell in enumerate(sh.col(105)):
        if not i or i<10:
            continue
        if type(pdf_col[i])==str:
            w_sheet.write(i,105,pdf_col[i].decode('utf-8', errors='replace'),plain)
        else:
            w_sheet.write(i,105,pdf_col[i],plain)

    for i,cell in enumerate(sh.col(98)):
        if not i or i<10:
            continue
        if type(params_col[i])==str:
            w_sheet.write(i,98,params_col[i].decode('utf-8', errors='replace'),plain)
        else:
            w_sheet.write(i,98,params_col[i],plain)

    for i,cell in enumerate(sh.col(99)):
        if not i or i<10:
            continue
        if type(attention_col[i])==str:
            w_sheet.write(i,99,attention_col[i].decode('utf-8', errors='replace'),plain)
        else:
            w_sheet.write(i,99,attention_col[i],plain)

    for i,cell in enumerate(sh.col(118)):
        if not i or i<10:
            continue
        if type(dim_col[i])==str:
            w_sheet.write(i,118,dim_col[i].decode('utf-8', errors='replace'),plain)
        else:
            w_sheet.write(i,118,dim_col[i],plain)

    for i,cell in enumerate(sh.col(114)):
        if not i or i<10:
            continue
        if type(schm1_col[i])==str:
            w_sheet.write(i,114,schm1_col[i].decode('utf-8', errors='replace'),plain)
        else:
            w_sheet.write(i,114,schm1_col[i],plain)

    for i,cell in enumerate(sh.col(116)):
        if not i or i<10:
            continue
        if type(schm2_col[i])==str:
            w_sheet.write(i,116,schm2_col[i].decode('utf-8', errors='replace'),plain)
        else:
            w_sheet.write(i,116,schm2_col[i],plain)

    wb.save(fns)

def info():
    show_info(info_txt)

def OpenProg():
    global frame0
    global level_0
    global e

    def entry_return(event):
        global query
        search(e, v, names_col, all_cats, full_path, frame0, img_source_entry, textbox, params_col, img_col, pdf_source_entry, pdf_col, \
            level_0, level_1, level_2, level_3, listbox, call_list_to_search, sw, call_level_1, call_items0, call_level_2, call_items1, \
            call_level_3, call_items2, call_items3, textbox_1, explain_col, attention_col, dim_col, schm1_col, schm2_col, \
            dim_source_entry, schm1_source_entry, schm2_source_entry, img_directory, frame_picture, view_d, view_s1, view_s2, frameZ)

    def call_list_to_search(event):
        list_to_search(event, e, names_col, img_source_entry, pdf_source_entry, all_cats, full_path, \
            frame0, v, textbox, textbox_1, params_col, img_col, pdf_col, back_show, pages, explain_col, \
            attention_col, dim_col, schm1_col, schm2_col, dim_source_entry, schm1_source_entry, \
            schm2_source_entry, img_directory, frame_picture, view_d, view_s1, view_s2)
        back_show(menu_point(event), level_0, level_1, level_2, level_3, listbox, all_cats, \
            names_col, call_list_to_search, sw, frameZ, params_col, call_level_1, call_items0, \
            call_level_2, call_items1, call_level_3, call_items2, call_items3)

    def call_items0(event):
        items(0, event, listbox, all_cats, names_col, call_list_to_search)
        show_empty(sw, frame0, listbox, names_col, params_col)

    def call_items1(event):
        items(1, event, listbox, all_cats, names_col, call_list_to_search)
        show_empty(sw, frame0, listbox, names_col, params_col)

    def call_items2(event):
        items(2, event, listbox, all_cats, names_col, call_list_to_search)
        show_empty(sw, frame0, listbox, names_col, params_col)

    def call_items3(event):
        items(3, event, listbox, all_cats, names_col, call_list_to_search)
        show_empty(sw, frame0, listbox, names_col, params_col)
        item_path_show(menu_point(event), all_cats, names_col, full_path, frame0)

    def call_level_1(event):
        level_1_items(event, level_1, level_2, level_3, listbox, all_cats, names_col, full_path, frame0, call_level_2, call_items1)

    def call_level_2(event):
        level_2_items(event, level_2, level_3, listbox, all_cats, names_col, full_path, frame0, call_level_3, call_items2)

    def call_level_3(event):
        level_3_items(event, level_3, listbox, all_cats, names_col, full_path, frame0, call_items3)
        show_empty(sw, frame0, listbox, names_col, params_col)

    def load_template():
        with open(template_file, 'r') as f:
            template_text = f.read()
            textbox_t.delete(1.0, END)
            textbox_t.insert(END, template_text)

    def save_changes():
        query = e.get()
        for i,item in enumerate(names_col):
            if item == query:
                params_col.pop(i)
                params_col.insert(i, textbox.get(1.0, END).encode('utf-8'))
                textbox.delete(1.0, END)
                textbox.insert(END, params_col[i])           
                attention_col.pop(i)
                attention_col.insert(i, textbox_1.get(1.0, END).encode('utf-8'))
                textbox_1.delete(1.0, END)
                textbox_1.insert(END, attention_col[i])
        with open(template_file, 'w') as f:
            f.write(textbox_t.get(1.0, END).encode('utf-8'))
        load_template()
        apply_design()
        for i,item in enumerate(names_col):
            if item == query:
                html_show(explain_col[i])

    def save_img():
        query = e.get()
        for i,item in enumerate(names_col):
            if item == query:
                img_col.pop(i)
                img_col.insert(i, img_source_entry.get().encode('utf-8'))

    def save_pdf():
        query = e.get()
        for i,item in enumerate(names_col):
            if item == query:
                pdf_col.pop(i)
                pdf_col.insert(i, pdf_source_entry.get().encode('utf-8'))

    def save_dim():
        query = e.get()
        for i,item in enumerate(names_col):
            if item == query:
                dim_col.pop(i)
                dim_col.insert(i, dim_source_entry.get().encode('utf-8'))

    def save_schm1():
        query = e.get()
        for i,item in enumerate(names_col):
            if item == query:
                schm1_col.pop(i)
                schm1_col.insert(i, schm1_source_entry.get().encode('utf-8'))

    def save_schm2():
        query = e.get()
        for i,item in enumerate(names_col):
            if item == query:
                schm2_col.pop(i)
                schm2_col.insert(i, schm2_source_entry.get().encode('utf-8'))

    ######################################################### GUI constraction ##################################################################
    frame0=Frame(frameZ, width=1260, heigh=770)
    frame1=Frame(frame0,width=430,heigh=640)
    frame1.place(x=10, y=35)
    frame2=Frame(frame0,width=330,heigh=700)
    frame2.place(x=550, y=44)
    frame3=Frame(frame0,width=1000, heigh=40)
    frame3.place(x=10, y=677)
    frame_listbox=Frame(frame0,width=44, height=440)
    frame_listbox.place(x=270, y=43)
    frame_picture=Frame(frame1,width=249,heigh=220)
    frame_picture.place(x=0, y=406)

    e = AutocompleteEntry.AutocompleteEntry(frame0, width=43,font='Arial 13')
    e.place(x=10, y=10)
    e.focus_set()
    e.delete(0, END)
    e.insert(0, '')
    e.bind('<Return>', entry_return)

    viewer = ttk.Notebook(frame2)
    viewer.pack(fill="both", expand=True)

    view_0 = ttk.Frame(frame2)
    viewer.add(view_0, text ='Технические характеристики')

    view_s1= ttk.Frame(frame2)
    viewer.add(view_s1, text ='Схема №1 ')

    view_s2= ttk.Frame(frame2)
    viewer.add(view_s2, text ='Схема №2 ')

    view_d = ttk.Frame(frame2)
    viewer.add(view_d, text ='Габариты устройства')

    view_1 = ttk.Frame(frame2)
    viewer.add(view_1, text ='Специальное объявление')

    view_t = ttk.Frame(frame2)
    viewer.add(view_t, text ='Редактировать шаблон')

    label_fill0 = Label(view_d, text="")
    label_fill0.pack()

    label_fill1 = Label(view_s1, text="")
    label_fill1.pack()

    label_fill2 = Label(view_s2, text="")
    label_fill2.pack()

    label_dim = Label(view_d, text="Файл с картинкой:")
    label_dim.place(x=10, y=502)
    dim_source_entry = Entry(view_d, width=54,font='Arial 13')
    dim_source_entry.place(x=120, y=500)
    dim_btn = Button(view_d, text="Сохранить", command=save_dim)
    dim_btn.place(x=620, y=500)

    label_schm1 = Label(view_s1, text="Файл с картинкой:")
    label_schm1.place(x=10, y=502)
    schm1_source_entry = Entry(view_s1, width=54,font='Arial 13')
    schm1_source_entry.place(x=120, y=500)
    schm1_btn = Button(view_s1, text="Сохранить", command=save_schm1)
    schm1_btn.place(x=620, y=500)

    label_schm2 = Label(view_s2, text="Файл с картинкой:")
    label_schm2.place(x=10, y=502)
    schm2_source_entry = Entry(view_s2, width=54,font='Arial 13')
    schm2_source_entry.place(x=120, y=500)
    schm2_btn = Button(view_s2, text="Сохранить", command=save_schm2)
    schm2_btn.place(x=620, y=500)

    textbox = Text(view_0,height=33,width=96,font='Arial 10',wrap=WORD)
    textbox.pack(side='left')
    scrollbar_t = Scrollbar(view_0)
    scrollbar_t.pack(side=RIGHT, fill=Y)
    scrollbar_t['command'] = textbox.yview
    textbox['yscrollcommand'] = scrollbar_t.set

    textbox_1 = Text(view_1,height=33,width=96,font='Arial 10',wrap=WORD)
    textbox_1.pack(side='left')
    scrollbar_t1 = Scrollbar(view_1)
    scrollbar_t1.pack(side=RIGHT, fill=Y)
    scrollbar_t1['command'] = textbox_1.yview
    textbox_1['yscrollcommand'] = scrollbar_t1.set

    textbox_t = Text(view_t,height=33,width=96,font='Arial 10',wrap=WORD)
    textbox_t.pack(side='left')
    scrollbar_t1 = Scrollbar(view_t)
    scrollbar_t1.pack(side=RIGHT, fill=Y)
    scrollbar_t1['command'] = textbox_t.yview
    textbox_t['yscrollcommand'] = scrollbar_t1.set

    listbox = Listbox(frame_listbox, exportselection=0)
    listbox.config(width=42, height=44)
    listbox.pack(side='left')
    scrollbar = Scrollbar(frame_listbox)
    scrollbar['command'] = listbox.yview
    listbox['yscrollcommand'] = scrollbar.set
    scrollbar.pack(side=RIGHT, fill=Y)

    level_0 = Listbox(frame1, width=41, height=10, exportselection=0)
    level_0.place(x=0, y=8)
    level_1 = Listbox(frame1, width=41, height=5, exportselection=0)
    level_1.place(x=0, y=160)
    level_2 = Listbox(frame1, width=41, height=5, exportselection=0)
    level_2.place(x=0, y=241)
    level_3 = Listbox(frame1, width=41, height=5, exportselection=0)
    level_3.place(x=0, y=323)

    label_open_file = Label(frame0, text="Редактируемый файл:")
    label_open_file.place(x=10, y=700)
    label_open_item = Label(frame0, text="Редактируемая позиция:")
    label_open_item.place(x=548, y=11)
    label_img_source = Label(frame0, text="Путь к картинке товара:")
    label_img_source.place(x=550, y=610)
    label_img_source = Label(frame0, text="Путь к файлу PDF:")
    label_img_source.place(x=910, y=610)
    img_source_entry = Entry(frame0, width=29,font='Arial 13')
    img_source_entry.place(x=550, y=640)
    pdf_source_entry = Entry(frame0, width=29,font='Arial 13')
    pdf_source_entry.place(x=910, y=640)
    progress = ttk.Progressbar(frameZ, length=1242, maximum=1)
    progress.place(x=10, y=740)

    b = Button(frame0, text="Поиск по наименованию", command=lambda event='<Button-1>':entry_return(event))
    b.place(x=409, y=10)
    html_btn = Button(frame0, text="Вывести в браузер", command=lambda aurl=url:OpenUrl(aurl))
    html_btn.place(x=1010, y=700)
    save_btn = Button(frame0, text="Сохранить изменения", command=save_changes)
    save_btn.place(x=1132, y=700)
    img_save_button = Button(frame0, text="Сохранить", command=save_img)
    img_save_button.place(x=825, y=640)
    pdf_save_button = Button(frame0, text="Сохранить", command=save_pdf)
    pdf_save_button.place(x=1185, y=640)

    global fn
    global book
    global sh

    fn = tkFileDialog.Open(root, filetypes = [('*.xls files', '.xls')]).show()
    if fn == '':
        return
    book = xlrd.open_workbook(fn, 'rt' ,formatting_info=True)
    sh = book.sheet_by_index(0)
    loading_arrs(sh, names_col, explain_col, all_cats, img_col, pdf_col, short_col, include_col, \
                dim_col, schm1_col, schm2_col, attention_col, params_col, frameZ)
    full_path_show(frame0, fn)
    categories(all_cats, level_0, call_level_1, call_items0)
    autofill_names(names_col, names_list, e)
    page_design(frameZ, pages, explain_col, names_col, short_col, img_col, pdf_col, include_col, \
        dim_col, schm1_col, schm2_col, attention_col, params_col, template_file, template_fill)
    load_template()

    frame0.pack()

if __name__ == '__main__':
    ################################################### Making lists and variables ########################################################
    names_list     = []
    names_col      = []
    explain_col    = []
    img_col        = []
    pdf_col        = []
    short_col      = []
    pages          = []
    include_col    = []
    dim_col        = []
    schm1_col      = []
    schm2_col      = []
    attention_col  = []
    params_col     = []
    all_cats       = [[],[],[],[],[]]
    url            = 'page.html'
    template_file  = 'template.html'
    img_directory  = 'http://poligon.info/images/'
    wall_pic       = 'priceditor_logo.jpg' # pic must have dimentions 1255 x 770 pixels
    info_txt       = 'info.txt'
    query          = ''
    root           = Tk()
    v              = StringVar()
    full_path      = StringVar()
    sw             = 1
    
    hostname   = 'localhost'
    database   = 'poliinfo_bitrix'
    db_user    = 'poliinfo_bitrix'
    db_pass    = 'Y2Gd75q'
    db_request = "select `NAME` from `b_iblock_element` where `id`=89631"

    root.resizable(0,0)
    root.title("Price Editor 1.6")
    frameZ=Frame(root, width=1260, heigh=770)
    frameZ.pack()

    wallpaper      = PIL.Image.open(wall_pic)
    wall_picture   = ImageTk.PhotoImage(wallpaper)
    wall_pic_label = Label(frameZ, image = wall_picture)
    wall_pic_label.place(x=0, y=0)

    ###################################################### create a toplevel menu ##############################################################

    menubar = Menu(frameZ)

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Файл", menu=filemenu)
    filemenu.add_command(label="Открыть", command=OpenProg)
    filemenu.add_command(label="Сохранить", command=SaveFile)
    filemenu.add_command(label="Закрыть", command=CloseFile)
    filemenu.add_separator()
    filemenu.add_command(label="Выход", command=Quit)

    optmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Опции", menu=optmenu)
    optmenu.add_command(label="Скрывать незаполненные позиции", command=unplug_red_from_menu)
    optmenu.add_command(label="Обновить дизайн всех элементов", command=apply_design)

    settings_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Настройки", menu=settings_menu)

    about_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Справка", menu=about_menu)
    about_menu.add_command(label="О программе", command=info)

    # display the menu
    root.config(menu=menubar)

    root.mainloop()