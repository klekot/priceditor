# -*- coding: utf-8 -*-
from codecs import *

class Images():
	def __init__(self, query, names_col, img_directory, img_col, dim_col, schm1_col, schm2_col):
		self.query = query
		self.names_col = names_col
		self.img_directory = img_directory
		self.img_col = img_col
		self.dim_col = dim_col
		self.schm1_col = schm1_col
		self.schm2_col = schm2_col

	def img_dev_path(self, query, names_col, img_directory, img_col):
		for i in range(len(names_col)):
			if names_col[i] == query:
				return img_directory + img_col[i]

	def img_dim_path(self, query, names_col, img_directory, dim_col):
		for i in range(len(names_col)):
			if names_col[i] == query:
				img_dim_file = dim_col[i]
				return img_directory + dim_col[i]

	def img_schm1_path(self, query, names_col, img_directory, schm1_col):
		for i in range(len(names_col)):
			if names_col[i] == query:
				img_schm1_file = schm1_col[i]
				return img_directory + schm1_col[i]

	def img_schm2_path(self, query, names_col, img_directory, schm2_col):
		for i in range(len(names_col)):
			if names_col[i] == query:
				img_schm2_file = schm2_col[i]
				return img_directory + schm2_col[i]

if __name__ == '__main__':
	direc = 'http://poligon.info/images/'
	names = ['kdfjd', 'oweir', 'asdfoiu', 'asd']
	image = ['2134', '657', '2626', '978', '1234']
	dim = ['kdfjd', 'oweir', 'asdfoiu', 'asd']
	s1 = ['kdfjd', 'oweir', 'asdfoiu', 'asd']
	s2 = ['kdfjd', 'oweir', 'asdfoiu', 'asd']

	i = Images('asd', names, direc, image, dim, s1, s2)
	print i.img_dev_path('asd', names, direc, image)