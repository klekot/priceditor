# -*- coding: utf-8 -*-
import sys
from codecs import *

def valid_name(name):
    reload(sys)
    forbidden = ['\\', '/', ':', '*', '?', '\"', '<', '>', '|', ' ', '\n', '\r']
    arr = []
    for i, index in enumerate(name):
        if index not in forbidden:
            arr.append(index)
        else:
            arr.append('_')
    return ("".join(arr)).upper()