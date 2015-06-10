# -*- coding: utf-8 -*-
import ttk
import os
import shutil
from modules.vendors_name import *
from modules.valid_name import *

def old_file_place(old_items_name):
    arr = [l for l in old_items_name]
    count = arr.count('/')
    path_arr = []
    name_arr = []
    while len(arr) > 0:
        if count > 0:
            path_arr.append(arr.pop(0))
            count = arr.count('/')
        else:
            name_arr.append(arr.pop(0))
    path_win = []
    for p in path_arr:
        if p != '/':
            path_win.append(p)
        else:
            path_win.append('\\')
    return "".join(path_win), "".join(name_arr)

def target_name(item, old_items_name, suffix, mark):
    ext = [l for l in old_items_name]         
    count = ext.count('.')
    while count > 1:
        ext.pop(0)
        count = ext.count('.')
    ext_arr  = []
    dot = len(ext)
    for i, letter in enumerate(ext):
        if letter == '.':
            dot = i
        if i < dot:
            pass
        else:
            ext_arr.append(letter)    
    if suffix != '':
        sep = "_"
    else:
        sep = ""   
    return valid_name(item) + sep + suffix + mark + "".join(ext_arr)

def local_save_all(names_col, img_col, pdf_col, dim_col, schm1_col, schm2_col, vendor_col, frameZ):
    global suffix
    global plur
    global ready_name
    global local_name
    all_cols = [[img_col], [dim_col], [schm1_col], [schm2_col], [pdf_col]]
    for c, col in enumerate(all_cols):
        for i, item in enumerate(all_cols[c]):
            progress = ttk.Progressbar(frameZ, length=1235, maximum=len(names_col))
            progress.place(x=10, y=740)
            for n in range(len(names_col)):
                progress.step(1)
                frameZ.update()
                target_branch  = 'images\\catalog\\'
                if c < 4:
                    target_branch  = 'images\\catalog\\'
                else:
                    target_branch  = 'PDF\\datasheets\\'
                    suffix = ''
                    plur = ''
                    mark = ''
                if c == 0:
                    suffix = 'device'
                    plur = 's'
                    mark = ''
                if c == 1:
                    suffix = 'dim'
                    plur = 's'
                    mark = ''
                if c == 2:
                    suffix = 'plug'
                    plur = 's'
                    mark = '1'
                if c == 3:
                    suffix = 'plug'
                    plur = 's'
                    mark = '2'
                if (isinstance(all_cols[c][i][n], unicode) == True) and (all_cols[c][i][n] != '') \
                                                                    and vendors_name(vendor_col[n]) !='':
                    catalog_part = vendors_name(vendor_col[n]) + '\\' + suffix + plur + '\\'
                    local_root = 'Z:\\home\\localhost\\www\\'
                    local_path = local_root + 'images\\' + old_file_place(all_cols[c][i][n])[0]
                    local_path_pdf = local_root + 'PDF\\' + old_file_place(all_cols[c][i][n])[0]
                    target_folder = local_root + target_branch + catalog_part
                    local_name = old_file_place(all_cols[c][i][n])[1]
                    ready_name = target_name(names_col[n], all_cols[c][i][n], suffix, mark)
                    if c < 4:
                        put_file = local_path + local_name
                        new_name = target_folder + ready_name
                    else:
                        put_file = local_path_pdf + local_name
                        new_name = target_folder + local_name
                    try:
                        shutil.copyfile(put_file, new_name)
                        if c < 4:
                            all_cols[c][i].pop(n)
                            all_cols[c][i].insert(n, ('catalog/' + vendors_name(vendor_col[n]) + '/' + suffix + plur + '/' + ready_name))
                        else:
                            all_cols[c][i].pop(n)
                            all_cols[c][i].insert(n, ('datasheets/' + vendors_name(vendor_col[n]) + '/' + local_name))
                    except IOError as err:
                        if c == 0:
                            print 'err c==0'
                            """
                            with open('local_save_log.txt', 'rw') as log:
                                if log.readline() == '':
                                    log.write(str(err) + ' - ' +  names_col[n] + '\n')
                            """         
                            with open('local_save_log.txt', 'a') as log:
                                log.write(str(err) + ' - ' +  names_col[n] + '\n')
                        else:
                            print 'err c==1,2,3,4'
                            with open('local_save_log.txt', 'a') as log:
                                log.write(str(err) + ' - ' +  names_col[n] + '\n')
        print "Done " + str(c) + '-----------------------'                   