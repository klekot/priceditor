from Tkinter import *
def item_path_show(menu_point, all_cats, names_col, full_path, frame0):
    for i in range(len(all_cats[0])):
        if all_cats[0][i] == menu_point:
            full_path.set(all_cats[0][i].encode('utf-8', errors='replace') + "  >  ")

        elif all_cats[1][i] == menu_point:
            full_path.set(all_cats[0][i].encode('utf-8', errors='replace') + "  >  " + \
                        all_cats[1][i].encode('utf-8', errors='replace') + "  >  ")

        elif all_cats[2][i] == menu_point:
            full_path.set(all_cats[0][i].encode('utf-8', errors='replace') + "  >  " + \
                        all_cats[1][i].encode('utf-8', errors='replace') + "  >  " + \
                        all_cats[2][i].encode('utf-8', errors='replace') + "  >  ")

        elif all_cats[3][i] == menu_point:
            full_path.set(all_cats[0][i].encode('utf-8', errors='replace') + "  >  " + \
                        all_cats[1][i].encode('utf-8', errors='replace') + "  >  " + \
                        all_cats[2][i].encode('utf-8', errors='replace') + "  >  " + \
                        all_cats[3][i].encode('utf-8', errors='replace') + "  >  ")

        elif names_col[i] == menu_point:
            full_path.set(all_cats[0][i].encode('utf-8', errors='replace') + "  >  " + \
                        all_cats[1][i].encode('utf-8', errors='replace') + "  >  " + \
                        all_cats[2][i].encode('utf-8', errors='replace') + "  >  " + \
                        all_cats[3][i].encode('utf-8', errors='replace') + "  >  " + \
                        names_col[i].encode('utf-8', errors='replace'))
    open_item_path = Label(frame0, textvariable=full_path, fg="red", font=("Helvetica", 10))
    open_item_path.place(x=10, y=672)