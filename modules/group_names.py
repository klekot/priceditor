# -*- coding: utf-8 -*-

def group_names(names_col, img_col, dim_col, schm1_col, schm2_col, pdf_col):
        all_cols = [[img_col], [dim_col], [schm1_col], [schm2_col], [pdf_col]]
        for c, col in enumerate(all_cols):
            for i, item in enumerate(col):
                item_group = []
                name_group = []
                if item not in group:
                    item_group.append(item)
                else:
                    name_group.append(names_col[i])