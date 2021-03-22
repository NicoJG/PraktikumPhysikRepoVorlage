# Mehrere Ergebnisse als CSV Datei abspeichern
# um diese z.B. in eine Tabelle umzuwandeln
# mit pandas ist es z.B. einfacher einen Spalte mit Strings zu haben

# wechsle die Working Directory zum Versuchsordner, damit das Python-Script von überall ausgeführt werden kann
import os
import pathlib
os.chdir(pathlib.Path(__file__).absolute().parent.parent.__str__())

# Imports
import pandas as pd

# Daten einlesen
data = pd.read_csv('data/NAME.csv')
x,y,z = data.to_numpy().T

# Berechnungen machen
# ...

# Daten speichern
data = {'x[Ohm]':x, 'y[J]':y, 'z[V]':z}
df = pd.DataFrame(data)
df.to_csv('data/NAME.csv', index=False)