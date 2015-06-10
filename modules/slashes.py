# -*- coding: utf-8 -*-
import os
from valid_name import *

def slashes(query, upload_file, suffix, mark):
    upload_file_path = os.path.split(upload_file)[0]
    upload_file_name = os.path.split(upload_file)[1]
    arr = []
    for letter in upload_file_path:
        if letter != '\\':
            arr.append(letter)
        else:
            arr.append('\\' + '\\')

    ext = [l for l in upload_file_name]         
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
     
    return "".join(arr), (valid_name("".join(query)) + sep + suffix + mark + "".join(ext_arr))