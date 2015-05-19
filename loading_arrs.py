import xlrd
import ttk

def loading_arrs(sh, names_col, explain_col, all_cats, img_col, pdf_col, short_col, \
                include_col, dim_col, schm1_col, schm2_col, attention_col, params_col, frameZ):
    progress = ttk.Progressbar(frameZ, length=1242, maximum=sh.nrows)
    progress.place(x=10, y=740)
    for i in range(sh.nrows):
        progress.step(1)
        frameZ.update()
        names_col.append(sh.cell_value(rowx=i, colx=5))
        explain_col.append(sh.cell_value(rowx=i, colx=112))
        all_cats[0].append(sh.cell_value(rowx=i, colx=106))
        all_cats[1].append(sh.cell_value(rowx=i, colx=107))
        all_cats[2].append(sh.cell_value(rowx=i, colx=108))
        all_cats[3].append(sh.cell_value(rowx=i, colx=109))
        all_cats[4].append(sh.cell_value(rowx=i, colx=110))
        img_col.append(sh.cell_value(rowx=i, colx=104))
        pdf_col.append(sh.cell_value(rowx=i, colx=105))
        short_col.append(sh.cell_value(rowx=i, colx=7))
        include_col.append(sh.cell_value(rowx=i, colx=0))
        dim_col.append(sh.cell_value(rowx=i, colx=118))
        schm1_col.append(sh.cell_value(rowx=i, colx=114))
        schm2_col.append(sh.cell_value(rowx=i, colx=116))
        attention_col.append(sh.cell_value(rowx=i, colx=99))
        params_col.append(sh.cell_value(rowx=i, colx=98))