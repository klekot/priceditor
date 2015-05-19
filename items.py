from menu_point import *

def items(level, event, listbox, all_cats, names_col, call_list_to_search):
    listbox.delete(0, END)
    menu_point(event)
    arr = []
    for i, item in enumerate(all_cats[level]):
        if (item==menu_point(event)) and (names_col[i] not in arr) and (names_col[i]!=''):
            arr.append(names_col[i])
    for i in arr:
        listbox.insert(END, i)
        listbox.bind("<Double-Button-1>", call_list_to_search)