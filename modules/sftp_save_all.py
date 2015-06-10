# -*- coding: utf-8 -*-
import ttk
from modules.sftp_upload import *
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

def sftp_save_all(names_col, img_col, pdf_col, dim_col, schm1_col, schm2_col, \
                  vendor_col, target_root, sftp_server, sftp_user, sftp_pass, frameZ):
    all_cols = [[img_col], [dim_col], [schm1_col], [schm2_col]]#, [pdf_col]]
    for c, col in enumerate(all_cols):
        for i, item in enumerate(all_cols[c]):
            progress = ttk.Progressbar(frameZ, length=1235, maximum=len(names_col))
            progress.place(x=10, y=740)
            for n in range(len(names_col)):
                progress.step(1)
                frameZ.update()
                target_branch  = '/images/catalog/'
                """
                if c < 4:
                    target_branch  = '/images/catalog/'
                else:
                    target_branch  = '/PDF/'
                    suffix = ''
                    plur = ''
                    mark = ''
                """
                if c == 0:
                    suffix = 'device'
                    plur = 's/'
                    mark = ''
                if c == 1:
                    suffix = 'dim'
                    plur = 's/'
                    mark = ''
                if c == 2:
                    suffix = 'plug'
                    plur = 's/'
                    mark = '1'
                if c == 3:
                    suffix = 'plug'
                    plur = 's/'
                    mark = '2'
                if (isinstance(all_cols[c][i][n], unicode) == True) and (all_cols[c][i][n] != '') \
                                                                    and vendors_name(vendor_col[n]) !='':
                    catalog_part = vendors_name(vendor_col[n]) + '/' + suffix + plur
                    target_folder = target_root + target_branch + catalog_part
                    local_path = 'Z:\\home\\localhost\\www\\images\\' + old_file_place(all_cols[c][i][n])[0]
                    local_name = old_file_place(all_cols[c][i][n])[1]
                    ready_name = target_name(names_col[n], all_cols[c][i][n], suffix, mark)
                    put_file = local_path + local_name
                    old_name = target_folder + local_name
                    new_name = target_folder + ready_name
                    sftp_upload(sftp_server, sftp_user, sftp_pass, target_folder, put_file, old_name, new_name)