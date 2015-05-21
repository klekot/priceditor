from Tkinter import *
from modules.item_path_show import *
from modules.show_open_item import *
from modules.html_show import *
from modules.back_show import *
from modules.refresh import *

def search(e, v, names_col, all_cats, full_path, frame0, img_source_entry, textbox, params_col, img_col, pdf_source_entry, pdf_col, \
        level_0, level_1, level_2, level_3, listbox, call_list_to_search, sw, call_level_1, call_items0, call_level_2, call_items1, \
        call_level_3, call_items2, call_items3, textbox_1, explain_col, attention_col, dim_col, schm1_col, schm2_col, \
        dim_source_entry, schm1_source_entry, schm2_source_entry, img_directory, frame_picture, view_d, view_s1, view_s2, frameZ):
    global query
    query = e.get()
    item_path_show(query, all_cats, names_col, full_path, frame0)
    show_open_item(v, query, frame0)
    for i in range(len(names_col)):
        if names_col[i] == query:
            textbox.delete(1.0, END)
            textbox.insert(END, params_col[i])
            html_show(textbox.get(1.0, END))
            img_source_entry.delete(0, END)
            img_source_entry.insert(END, img_col[i])
            pdf_source_entry.delete(0, END)
            pdf_source_entry.insert(END, pdf_col[i])
    refresh(query, names_col, textbox, textbox_1, params_col, explain_col, img_source_entry, \
            img_col, pdf_source_entry, pdf_col, attention_col, dim_col, schm1_col, schm2_col, \
            dim_source_entry, schm1_source_entry, schm2_source_entry, img_directory, frame_picture, \
            view_d, view_s1, view_s2)
    back_show(query, level_0, level_1, level_2, level_3, listbox, all_cats, names_col, call_list_to_search, \
        sw, frameZ, params_col, call_level_1, call_items0, call_level_2, call_items1, call_level_3, call_items2, call_items3)