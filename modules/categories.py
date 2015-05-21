from Tkinter import *
from modules.tree_cats import *

def categories(all_cats, level_0, call_level_1, call_items0):
    for i in tree_cats(0, all_cats):
        level_0.insert(END, i)
        level_0.bind("<Double-Button-1>", call_level_1)
        level_0.bind("<Double-Button-1>", call_items0, add="+")