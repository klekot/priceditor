c:\Python27\python.exe setup.py py2exe


После py2exe перенести в папку с exe файлом нужные html txt  и прочие файлы, 
а потом в файле tk.tcl исправить номер версии:
C:\Users\gnato\Desktop\Igor\progs\python_progs\priceditor\dist\tcl\tk8.5\tk.tcl

package require -exact Tk  8.5.12 <-- вот так