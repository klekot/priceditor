# -*- coding: utf-8 -*-
import sys
from codecs import *

def short_to_ul(short):
	reload(sys)  
	sys.setdefaultencoding('utf8')
	arr = []
	for i, index in enumerate(short):
		arr.append(index)
	new_arr = []
	par_open = 0
	par_close= 0
	for i, index in enumerate(arr):
		pars = par_open - par_close
		if (index == '('):
			par_open +=1
		elif (index == ')'):
			par_close +=1
		if (index != ','):
			new_arr.append(index)
		else:
			if pars == 0:
				new_arr.append("</li><li>")
			else:
				new_arr.append(",")
	begin_s = "<ul class=\"props_list\"><li> "
	end_s   = "</li></ul>"
	arr_s   = "".join(new_arr)
	out_str = begin_s + arr_s + end_s
	return out_str

if __name__ == '__main__':
	short = "Реле контроля напряжения, 3-фазн., (Un=690/400VAC, многофункциональное), 2 CO (требует TR3)"
	print short_to_ul(short)