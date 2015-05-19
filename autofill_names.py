from codecs import *

def autofill_names(names_col, names_list, e):
    for i in range(len(names_col)):
        if names_col[i]!='':
            if isinstance(names_col[i], float):
                names_col[i]=int(names_col[i])
                names_col[i]=str(names_col[i])
            names_list.append(names_col[i].encode('utf-8', errors='replace'))
    e.set_completion_list(names_list)