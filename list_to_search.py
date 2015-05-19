from Tkinter import *
from item_path_show import *
from show_open_item import *
from html_show import *
from refresh import *

def list_to_search(event, e, names_col, img_source_entry, pdf_source_entry, all_cats, full_path, \
    frame0, v, textbox, textbox_1, params_col, img_col, pdf_col, back_show, pages, explain_col, \
    attention_col, dim_col, schm1_col, schm2_col, dim_source_entry, schm1_source_entry, \
    schm2_source_entry, img_directory, frame_picture, view_d, view_s1, view_s2):
    global query
    widget = event.widget
    selection=widget.curselection()
    query = widget.get(selection[0])
    item_path_show(query, all_cats, names_col, full_path, frame0)
    e.delete(0, END)
    e.insert(0, query)   
    refresh(query, names_col, textbox, textbox_1, params_col, explain_col, img_source_entry, \
            img_col, pdf_source_entry, pdf_col, attention_col, dim_col, schm1_col, schm2_col, \
            dim_source_entry, schm1_source_entry, schm2_source_entry, img_directory, frame_picture, \
            view_d, view_s1, view_s2)         
    show_open_item(v, query, frame0)