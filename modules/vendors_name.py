# -*- coding: utf-8 -*-

def vendors_name(vendor):
    vendor = vendor.upper()
    good_vendor = ''
    valid_names = ['BENEDICT', 'CBI', 'CITEL', 'EMKO', \
                   'FARNELL', 'GRAESSLIN', 'HHI', 'HUBER+SUHNER',\
                   'RELECO', 'RELEQUICK', 'SONDER', 'TELE', 'VEMER', \
                   'POLIGON', 'ПОЛИГОН', 'POLIGONSPB']
    for name in valid_names:
        if vendor.find(name) == -1:
            pass
        else:
            if (name == 'ПОЛИГОН') or (name == 'POLIGON'):
                good_vendor = 'POLIGONSPB'
            good_vendor = name          
    return good_vendor