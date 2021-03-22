# wechsle die Working Directory zum Versuchsordner, damit das Python-Script von überall ausgeführt werden kann
import os
import pathlib
os.chdir(pathlib.Path(__file__).absolute().parent.parent.__str__())
# benutze die matplotlibrc und header-matplotlib.tex Dateien aus dem default Ordner
# Folgendes auskommentieren, wenn es schneller gehen soll (dafür weniger schön)
os.environ['MATPLOTLIBRC'] = (pathlib.Path(__file__).absolute().parent.parent.parent / 'default' / 'python' / 'matplotlibrc').__str__()
os.environ['TEXINPUTS'] =  (pathlib.Path(__file__).absolute().parent.parent.parent / 'default' / 'python').__str__() + ':'

# Imports
import numpy as np
import matplotlib.pyplot as plt

