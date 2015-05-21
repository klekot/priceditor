from modules.menu_point import *
from modules.item_path_show import *
from modules.arr import *

def level_2_items(event, level_2, level_3, listbox, all_cats, names_col, full_path, frame0, call_level_3, call_items2):
    level_2.delete(0, END)
    level_3.delete(0, END)
    listbox.delete(0, END)  
    menu_point(event)
    item_path_show(menu_point(event), all_cats, names_col, full_path, frame0)
    for i in arr(1, all_cats, event):
        level_2.insert(END, i)
        level_2.bind("<Double-Button-1>", call_level_3)
        level_2.bind("<Double-Button-1>", call_items2, add="+")