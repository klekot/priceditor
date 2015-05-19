from tree_cats import *
from show_empty import *
from list_to_search import *

def back_show(item_path, level_0, level_1, level_2, level_3, listbox, all_cats, names_col, call_list_to_search, sw, frameZ, \
            params_col, call_level_1, call_items0, call_level_2, call_items1, call_level_3, call_items2, call_items3):
    global taken_item_0
    global taken_item_1
    global taken_item_2

    listbox.delete(0, END)
    level_0.delete(0, END)
    level_1.delete(0, END)
    level_2.delete(0, END)
    level_3.delete(0, END)

###################################################    
    taken_item_0 = ""
    for index, p in enumerate(tree_cats(0, all_cats)):
        level_0.insert(END, p)
        level_0.bind("<Double-Button-1>", call_level_1)
        level_0.bind("<Double-Button-1>", call_items0, add="+")
        for i in range(len(all_cats[0])):
            if (names_col[i] == item_path) and (all_cats[0][i] == p):
                level_0.selection_set(index)
                level_0.see(index)
                taken_item_0 = tree_cats(0, all_cats)[index]

    listbox.delete(0, END)
    barr = []
    for i, item in enumerate(all_cats[0]):
        if (item==taken_item_0) and (names_col[i] not in barr) and (names_col[i]!=''):
            barr.append(names_col[i])
    for i in barr:
        listbox.insert(END, i)
        listbox.bind("<Double-Button-1>", call_list_to_search)
    show_empty(sw, frameZ, listbox, names_col, params_col)
    for i, item in enumerate(listbox.get(0, END)):
        if item == item_path:
            listbox.selection_set(i)
            listbox.see(i)
######################################################  
 


#########################################################    
    taken_item_1 = ""  
    arr1 = []
    for i, item in enumerate(all_cats[0]):
        if (item==taken_item_0) and (all_cats[1][i] not in arr1) and (all_cats[1][i]!=''):
            arr1.append(all_cats[1][i])
    for index, p in enumerate(arr1):
        level_1.insert(END, p)
        level_1.bind("<Double-Button-1>", call_level_2)
        level_1.bind("<Double-Button-1>", call_items1, add="+")
        for i in range(len(all_cats[1])):
            if (names_col[i] == item_path) and (all_cats[1][i] == p):
                level_1.selection_set(index)
                level_1.see(index)
                taken_item_1 = arr1[index]

    listbox.delete(0, END)
    barr1 = []
    for i, item in enumerate(all_cats[1]):
        if (item==taken_item_1) and (names_col[i] not in barr1) and (names_col[i]!=''):
            barr1.append(names_col[i])
    for i in barr1:
        listbox.insert(END, i)
        listbox.bind("<Double-Button-1>", call_list_to_search)
    show_empty(sw, frameZ, listbox, names_col, params_col)
    for i, item in enumerate(listbox.get(0, END)):
        if item == item_path:
            listbox.selection_set(i)
            listbox.see(i)
#######################################################
    


###########################################################   
    taken_item_2 = ""
    arr2 = []
    for i, item in enumerate(all_cats[1]):
        if (item==taken_item_1) and (all_cats[2][i] not in arr2) and (all_cats[2][i]!=''):
            arr2.append(all_cats[2][i])
    level_2.delete(0, END)
    for index, p in enumerate(arr2):
        level_2.insert(END, p)
        level_2.bind("<Double-Button-1>", call_level_3)
        level_2.bind("<Double-Button-1>", call_items2, add="+")
        for i in range(len(all_cats[2])):
            if (names_col[i] == item_path) and (all_cats[2][i] == p):
                level_2.selection_set(index)
                level_2.see(index)
                taken_item_2 = arr2[index]

    arr3 = []
    for i, item in enumerate(all_cats[0]):
        if (item==taken_item_2) and (all_cats[3][i] not in arr3) and (all_cats[3][i]!=''):
            arr3.append(all_cats[3][i])
    level_3.delete(0, END)
    for index, p in enumerate(arr3):
        level_3.insert(END, p)
        level_0.bind("<Double-Button-1>", call_items3, add="+")
        for i in range(len(all_cats[3])):
            if (names_col[i] == item_path) and (all_cats[3][i] == p):
                level_3.selection_set(index)
                level_3.see(index)
#######################################################################