# wechsle die Working Directory zum Versuchsordner, damit das Python-Script von überall ausgeführt werden kann
import os
os.chdir(os.path.dirname(__file__)+'/../')
# benutze die matplotlibrc und header-matplotlib.tex Dateien aus dem default Ordner
os.environ['MATPLOTLIBRC'] = os.path.dirname(__file__)+'/../../default/python/matplotlibrc'
os.environ['TEXINPUTS'] =  os.path.dirname(__file__)+'/../../default/python/:'

# Imports
import numpy as np
import matplotlib.pyplot as plt