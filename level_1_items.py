from menu_point import *
from item_path_show import *
from arr import *

def level_1_items(event, level_1, level_2, level_3, listbox, all_cats, names_col, full_path, frame0, call_level_2, call_items1):                        
    level_1.delete(0, END)
    level_2.delete(0, END)
    level_3.delete(0, END)
    listbox.delete(0, END)
    menu_point(event)
    item_path_show(menu_point(event), all_cats, names_col, full_path, frame0)
    for i in arr(0, all_cats, event):
        level_1.insert(END, i)
        level_1.bind("<Double-Button-1>", call_level_2)
        level_1.bind("<Double-Button-1>", call_items1, add="+")