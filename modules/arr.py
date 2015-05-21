from modules.menu_point import *

def arr(l, all_cats, event):
	arr = []
	for i, item in enumerate(all_cats[l]):
	    if (item==menu_point(event)) and (all_cats[l+1][i] not in arr) and (all_cats[l+1][i]!=''):
	        arr.append(all_cats[l+1][i])
	return arr