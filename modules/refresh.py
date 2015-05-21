# -*- coding: utf-8 -*-
from modules.html_show import *
from Tkinter import *
import ttk
import ImageTk
import Image
import requests
from StringIO import StringIO

#  my class #
from modules import Images

def resize(image, max_w, max_h):
    w = float(image.size[0])
    h = float(image.size[1])
    r = float(w / h)
    if r > 1:
        ratio = float(max_w / w)
    else:
        ratio = float(max_h / h)
    new_w = int(w * ratio)
    new_h = int(h * ratio)
    return (new_w, new_h)

def refresh(query, names_col, textbox, textbox_1, params_col, explain_col, img_source_entry, \
            img_col, pdf_source_entry, pdf_col, attention_col, dim_col, schm1_col, schm2_col, \
            dim_source_entry, schm1_source_entry, schm2_source_entry, img_directory, frame_picture, \
            view_d, view_s1, view_s2):
    global image_dev
    global image_dim
    global image_schm1
    global image_schm2
    for i in range(len(names_col)):
        if names_col[i] == query:
            textbox.delete(1.0, END)
            textbox.insert(END, params_col[i])
            textbox_1.delete(1.0, END)
            textbox_1.insert(END, attention_col[i])
            html_show(explain_col[i])
            img_source_entry.delete(0, END)
            img_source_entry.insert(END, img_col[i])
            pdf_source_entry.delete(0, END)
            pdf_source_entry.insert(END, pdf_col[i])
            dim_source_entry.delete(0, END)
            dim_source_entry.insert(END, dim_col[i])
            schm1_source_entry.delete(0, END)
            schm1_source_entry.insert(END, schm1_col[i])
            schm2_source_entry.delete(0, END)
            schm2_source_entry.insert(END, schm2_col[i])

            i_dev = Images.Images(query, names_col, img_directory, img_col, dim_col, schm1_col, schm2_col)
            img_dev_path = i_dev.img_dev_path(query, names_col, img_directory, img_col)
            pilim_dev = Image.open(StringIO((requests.get(img_dev_path)).content))
            size_dev = resize(pilim_dev, 220, 220)
            pilim_dev.thumbnail(size_dev, Image.ANTIALIAS)
            image_dev = ImageTk.PhotoImage(pilim_dev)
            panel_dev = Label(frame_picture, image = image_dev)
            panel_dev.place_forget()
            panel_dev.place(x=0, y=0)

            i_dim = Images.Images(query, names_col, img_directory, img_col, dim_col, schm1_col, schm2_col)
            img_dim_path = i_dim.img_dim_path(query, names_col, img_directory, dim_col)
            pilim_dim = Image.open(StringIO((requests.get(img_dim_path)).content))
            size_dim = resize(pilim_dim, 600, 450)
            pilim_dim.thumbnail(size_dim, Image.ANTIALIAS)
            image_dim = ImageTk.PhotoImage(pilim_dim)
            panel_dim = Label(view_d, image = image_dim)
            panel_dim.place_forget()
            panel_dim.place(x=0, y=0)

            i_schm1 = Images.Images(query, names_col, img_directory, img_col, dim_col, schm1_col, schm2_col)
            img_schm1_path = i_schm1.img_schm1_path(query, names_col, img_directory, schm1_col)
            pilim_schm1 = Image.open(StringIO((requests.get(img_schm1_path)).content))
            size_schm1 = resize(pilim_schm1, 600, 450)
            pilim_schm1.thumbnail(size_schm1, Image.ANTIALIAS)
            image_schm1 = ImageTk.PhotoImage(pilim_schm1)
            panel_schm1 = Label(view_s1, image = image_schm1)
            panel_schm1.place_forget()
            panel_schm1.place(x=0, y=0)

            i_schm2 = Images.Images(query, names_col, img_directory, img_col, dim_col, schm1_col, schm2_col)
            img_schm2_path = i_schm2.img_schm2_path(query, names_col, img_directory, schm2_col)
            pilim_schm2 = Image.open(StringIO((requests.get(img_schm2_path)).content))
            size_schm2 = resize(pilim_schm2, 600, 450)
            pilim_schm2.thumbnail(size_schm2, Image.ANTIALIAS)
            image_schm2 = ImageTk.PhotoImage(pilim_schm2)
            panel_schm2 = Label(view_s2, image = image_schm2)
            panel_schm2.place_forget()
            panel_schm2.place(x=0, y=0)