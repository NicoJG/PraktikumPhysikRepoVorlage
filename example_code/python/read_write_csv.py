# Mehrere Ergebnisse als CSV Datei abspeichern
# um diese z.B. in eine Tabelle umzuwandeln

# wechsle die Working Directory zum Versuchsordner, damit das Python-Script von überall ausgeführt werden kann
import os
os.chdir(os.path.dirname(__file__)+'/../')

# Imports
import numpy as np

# Daten einlesen
x,y,z = np.genfromtxt('data/NAME.csv', delimiter=',', skip_header=1, unpack=True)

# Berechnungen machen
# ...

# Daten speichern
data = list(zip(x, y, z))
np.savetxt('data/NAME.csv', data, header='x[Ohm],y[J],z[V]', comments='', fmt='%1.1f,%1.3f,%i')
# Nicht so wie hier die alten Daten überschreiben, sondern neue Datei anlegen!
# fmt = format (Genauigkeit,...)