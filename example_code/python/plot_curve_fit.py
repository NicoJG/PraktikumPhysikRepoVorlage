# Erstelle aus gegebnen Daten eine Ausgleichskurve
# Und Plotte diese Kurve + die Daten


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
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Daten einlesen
x,y,z = np.genfromtxt('data/NAME.csv',delimiter=',',unpack=True)

# Ausgleichskurven Funktion (hier Ausgleichsgerade)
def f(x,a,b):
    return a*x + b
# oder als Lambda Funktion
f = lambda x,a,b: a*x + b

# Ausgleichskurve berechnen
params,pcov = curve_fit(f,x,y)

# Parameter
a = params[0]
b = params[1]

# Unsicherheiten
a_err = np.absolute(pcov[0][0])**0.5
b_err = np.absolute(pcov[1][1])**0.5

# Werte irgendwie ausgeben lassen
# z.B. mit print, aber besser als JSON Datei abspeichern
print(f'{a = }+-{a_err}')
print(f'{b = :.2f}+-{b_err:.2f}')

# Plot der Ausgleichskurve
x_linspace = np.linspace(np.min(x), np.max(x), 100)
plt.plot(x_linspace, f(x_linspace,*params), 'k-', label='Ausgleichskurve')
# Plot der Daten
plt.plot(x, y, 'ro', label='Daten')

# Achsenbeschriftung mit LaTeX (nur wenn matplotlibrc benutzt wird)
plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
plt.ylabel(r'$y \:/\: \si{\micro\joule}$')

# in matplotlibrc leider (noch) nicht möglich
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

# Plot als PDF speichern
plt.savefig('build/plot_NAME.pdf')