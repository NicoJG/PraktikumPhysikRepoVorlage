# PraktikumPhysikRepoVorlage

Diese Vorlage kann verwendet werden, um eine Ordnerstruktur für das Physik Anfängerpraktikum (oder auch das Fortgeschrittenenpraktikum) an der Technischen Universität Dortmund zu haben.  

Viele Dateien sind der [Vorlage](https://github.com/pep-dortmund/toolbox-workshop/tree/master/latex-template) vom [Toolbox-Workshop](https://toolbox.pep-dortmund.org/) entnommen. (und teilweise abgeändert/angepasst)  

# Konzept der Ordner- und Datei-Struktur

In einigen Dateien sind, zusätzlich zur Vorlage vom Toolbox Workshop, Ergänzungen enthalten. Diese sind allerdings teilweise auskommentiert.  
Ich würde empfehlen alle Dateien mal durchzuschauen und die Kommentare zu lesen.  

Alle Ordner mit dem Namen "build" werden von git ignoriert. Wenn dies unerwünscht ist müsst ihr die Datei ".gitignore" verändern.  

Erklärungen:  

Ordner/Datei | Erklärung | Anders als Toolbox Workshop Vorlage
- | - | -
**default/** | Dateien, die für fast jeden Versuch genau gleich sein sollen | nun ist nicht mehr alles in jedem Versuchsordner
default/bib/ | BibTeX Dateien (Literaturverzeichnis) mit Einträgen die man in vielen Versuchen braucht | 
default/latex/ | LaTeX Kram den man immer braucht | 
default/latex/header.tex | Haupt LaTeX Header | Aufgeteilt in mehrere Dateien
default/latex/packages.tex | alle "\usepackage" Befehle sowie Package Einstellungen | biblatex Sortierung und Nummerierung; weitere nützliche Packages 
default/latex/authors.tex | ist für die Titelseite zuständig. Dort müssen die Namen noch geändert werden. | 
default/latex/custom_commands.tex | alle von euch definierten Commands. Dort sind auch schon 2 Beispiele eingefügt. | 
default/python/ | Style Dateien für matplotlib | runde Marker kleiner und schwarzer Rand ; Grid verändert 
**example_code/** | Code den man nicht auswendig weiß und ggf. rauskopieren kann | 
example_code/python/read_write_json.py | Ergebnisse von Rechnungen in einer .json Datei speichern, anstatt diese mit print() ausgeben zu lassen | 
**V000_Vorlage/** | sollte kopiert und umbenannt werden, wenn man einen neuen Versuch anfängt | Ordnerstruktur nach Dateityp und nur das Makefile im Hauptordner 
V000_Vorlage/latex/ | alle Dateien die mit LaTeX zu tun haben | einiges wird aus dem default/latex/ Ordner importiert 
V000_Vorlage/latex/main.tex | Haupt LaTeX Datei, die alle anderen Dateien einbindet ; Datum muss angepasst werden! | Zielsetzung hinzugefügt 
V000_Vorlage/latex/lit.bib | alle Literaturreferenzen, die für diesen Versuch relevant sind | 
V000_Vorlage/data/ | alle Messdaten hier speichern ; evtl. auch Ergebnisse von Rechnungen hier speichern | 
V000_Vorlage/python/ | alle Python Dateien | 
V000_Vorlage/python/plot1.py | Code den man fast immer benötigt; damit ist es möglich die Datei von überall auszuführen und die Pfade werden trotzdem korrekt erkannt (relativ zum Versuchsordner); ausführbar über "python plot1.py" oder über den Run Button in VSCode | anderer Standard Code 
/V000_Vorlage/Makefile | Herzstück der Dateistruktur; mit dem Befehl "make" alle Dateien hintereinander ausführen lassen und so den ganzen Versuch builden; mit "make plots" sollten alle Plots erstellt werden (damit nicht immer auch LaTeX ausgeführt wird); Makefile bei jeder neu erstellten Datei aktualisieren | "make plots"; Python Dateien einfacherer Befehl (durch den Code in plot1.py) 
