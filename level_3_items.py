from menu_point import *
from item_path_show import *
from arr import *
from show_empty import *

def level_3_items(event, level_3, listbox, all_cats, names_col, full_path, frame0, call_items3):
    level_3.delete(0, END)
    listbox.delete(0, END)
    menu_point(event)
    item_path_show(menu_point(event), all_cats, names_col, full_path, frame0)
    for i in arr(2, all_cats, event):
        level_3.insert(END, i)
        level_3.bind("<Double-Button-1>", call_items3)     