from distutils.core import setup
import py2exe
setup(windows=[{"script":"main_program.pyw"}], options={"py2exe":{"includes":["sip"]}})
