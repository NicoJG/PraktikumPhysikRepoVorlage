# Einzelne Ergebnisse Speichern (damit man nicht print benutzen muss)
# JSON Dateien werden als Dictionary eingelesen.


# wechsle die Working Directory zum Versuchsordner, damit das Python-Script von überall ausgeführt werden kann
import os
import pathlib
os.chdir(pathlib.Path(__file__).absolute().parent.parent.__str__())

# Imports
import json

# JSON Datei einlesen (am Anfang)
json_file_path = 'data/Ergebnisse.json'
try:
    with open(json_file_path,'r') as json_file:
        Ergebnisse = json.load(json_file)
except FileNotFoundError as err:
    # Falls Datei noch nicht existiert, leere Dictionary erstellen
    # Allerdings sollte der Ordner 'data' schon existieren
    Ergebnisse = {}

# Irgendwas berechnen...
x = 2
y = 1/3
# um mit Werten aus der JSON Datei zu rechen
# müssen diese evtl. erst in einen anderen Typ umgewandelt werden,
# wenn die Werte als String gespeichert wurden
# z.B.: x = float(Ergebnisse['Kategorie']['x'])

# berechnete Werte in der Dictionary speichern (am besten in Kategorien)
if not 'Kategorie' in Ergebnisse:
    Ergebnisse['Kategorie'] = dict()
Ergebnisse['Kategorie']['x'] = x
Ergebnisse['Kategorie']['y'] = round(y,5) # Anzahl der Kommastellen einstellen
Ergebnisse['Kategorie']['z'] = f'{x}+-{y:.2f}' # oder als String formatieren

# Dictionary als JSON Datei speichern (am Ende)
with open(json_file_path,'w') as json_file:
    json.dump(Ergebnisse, json_file, indent=4)