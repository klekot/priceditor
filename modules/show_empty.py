from Tkinter import *
import ttk

def show_empty(sw, frameZ, listbox, names_col, params_col):
    if sw != 0:
        progress = ttk.Progressbar(frameZ, length=1235, maximum=len(listbox.get(0, END)))
        progress.place(x=10, y=740)
        for i, item in enumerate(listbox.get(0, END)):
            try:
                progress.step(1)
                frameZ.update()
            except:
                pass
            for j, name in enumerate(names_col):
                if (item==name) and (params_col[j]==''):
                    try:
                        listbox.itemconfig(i, fg='red')
                    except:
                        pass
    elif sw == 0:
        pass