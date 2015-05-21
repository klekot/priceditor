def tree_cats(dir_lvl, all_cats):
    if dir_lvl==0:
        lvl = all_cats[0]
    elif dir_lvl==1:
        lvl = all_cats[1]
    elif dir_lvl==2:
        lvl = all_cats[2]
    elif dir_lvl==3:
        lvl = all_cats[3]
    elif dir_lvl==4:
        lvl = all_cats[4]
    
    cat_names = []
    for i in range(10, len(lvl)):
        if (lvl[i]!='') and (lvl[i] not in cat_names):
            cat_names.append(lvl[i])
    return cat_names