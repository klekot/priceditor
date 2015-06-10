# -*- coding: utf-8 -*-
import sys
import ttk
from codecs import *
from modules.short_to_ul import *
#from valid_name import *

def encol(col):
	if (type(col) == int) or (type(col) == float):
		return str(col).encode('utf-8', errors='replace')
	else:
		return col.encode('utf-8', errors='replace')

def template_fill(template_file, params, name, img, pdf, dim, schm1, schm2, short, attention):
	with open(template_file, 'r') as f:
		variables = [params, name, img, pdf, dim, schm1, schm2, short, attention]
		lines = [line for line in f.readlines()]
		new_lines = []
		for i, line in enumerate(lines):
			if ("{%") in line:
				characters = []
				for character in line:
					characters.append(character)
				for c, char in enumerate(characters):
					if (char == '{') and (characters[c+1] == '%'):
						beg_index = c
					if (char == '%') and (characters[c+1] == '}'):
						end_index = c+1
				beg_line = "".join(characters[0:beg_index])
				end_line = "".join(characters[end_index+1:])
				tag_line = "".join(characters[beg_index+3:end_index-2])
				for var in variables:
					if tag_line 	== "params":
						new_line 	 = beg_line + variables[0] + end_line
					if tag_line 	== "name":
						new_line 	 = beg_line + variables[1] + end_line
					if tag_line 	== "img":
						new_line 	 = beg_line + variables[2] + end_line
					if tag_line 	== "pdf":
						new_line 	 = beg_line + variables[3] + end_line
					if (tag_line	== "dim") and (dim != ""):
						new_line 	 = beg_line + variables[4] + end_line
					if (tag_line	== "dim") and (dim == ""):
						new_line 	 = "<tr><td><b>Информация будет доступна позже.</b></td></tr>"
					if (tag_line	== "schm1") and (schm1 != ""):
						new_line 	 = beg_line + variables[5] + end_line
					if (tag_line	== "schm1") and (schm1 == ""):
						new_line 	 = "<tr><td><b>Информация будет доступна позже.</b></td></tr>"
					if (tag_line	== "schm2") and (schm2 != ""):
						new_line 	 = beg_line + variables[6] + end_line
					if (tag_line	== "schm2") and (schm2 == ""):
						new_line 	 = "<tr><td></td></tr>"
					if tag_line 	== "short":
						new_line 	 = beg_line + short_to_ul(variables[7]) + end_line
					if tag_line 	== "attention":
						new_line 	 = beg_line + variables[8] + end_line

				new_lines.append(new_line)						
			else:
				new_lines.append(line)			
	return "".join(new_lines)

def page_design(frameZ, pages, explain_col, names_col, short_col, img_col, pdf_col, include_col, \
				dim_col, schm1_col, schm2_col, attention_col, params_col, template_file, template_fill):
	reload(sys)  
	sys.setdefaultencoding('utf8')
	pages =  []

	progress = ttk.Progressbar(frameZ, length=1235, maximum=len(params_col))
	progress.place(x=10, y=740)
	for i, item in enumerate(params_col):
	        progress.step(1)
	        frameZ.update()
		params = encol(item)
		name = encol(names_col[i])
		img = encol(img_col[i])
		pdf = encol(pdf_col[i])
		dim = encol(dim_col[i])
		schm1 = encol(schm1_col[i])
		schm2 = encol(schm2_col[i])
		short = encol(short_col[i])
		attention = encol(attention_col[i])
		pages.append(template_fill(template_file, params, name, img, pdf, dim, schm1, schm2, short, attention))

	progress = ttk.Progressbar(frameZ, length=1235, maximum=len(explain_col))
	progress.place(x=10, y=740)
	for i, item in enumerate(explain_col):
	        progress.step(1)
	        frameZ.update()
		if (type(item) == int) or (type(item) == float):
			explain = str(item).encode('utf-8', errors='replace')
		else:
			explain = item.encode('utf-8', errors='replace')

		if type(include_col[i]) == float:
			sel_index = int(include_col[i])
		elif type(include_col[i]) == str:
			if (include_col[i].encode('utf-8', errors='replace') == ''):
				sel_index = 0
		else:
			sel_index = include_col[i]
			
		bad_line  = "/PDF/<?=$arResult['PROPERTIES']['pdf']['VALUE'];?>" 
		if (sel_index == 1):
			explain_col.pop(i)
			explain_col.insert(i, pages[i])

		elif bad_line in explain:
			explain_col.pop(i)
			explain_col.insert(i, pages[i])