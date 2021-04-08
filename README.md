# PraktikumPhysikRepoVorlage

Diese Vorlage kann verwendet werden, um eine Ordnerstruktur für das Physik Anfängerpraktikum (oder auch das Fortgeschrittenenpraktikum) an der Technischen Universität Dortmund zu haben.  

Viele Dateien sind der [Vorlage](https://github.com/pep-dortmund/toolbox-workshop/tree/master/latex-template) vom [Toolbox-Workshop](https://toolbox.pep-dortmund.org/) entnommen. (und teilweise abgeändert/angepasst)  

# Konzept der Ordner- und Datei-Struktur

In einigen Dateien sind, zusätzlich zur Vorlage vom Toolbox Workshop, Ergänzungen enthalten. Diese sind allerdings teilweise auskommentiert.  
Ich würde empfehlen alle Dateien mal durchzuschauen und die Kommentare zu lesen.  

Alle Ordner mit dem Namen "build" werden von git ignoriert. Wenn dies unerwünscht ist müsst ihr die Datei ".gitignore" verändern.

## default

Dateien, die für fast jeden Versuch genau gleich sein sollen, sind im Ordner "/default" gespeichert.  
Dort ist z.B. der LaTex Header zu finden.  
Dieser Header wurde zur Übersicht in mehrere Dateien aufgeteilt:  
- "/default/latex/header.tex" ist die Haupt Header Datei und bindet alle anderen Dateien ein.  
- "/default/latex/packages.tex" enthält alle \usepackage Befehle, sowie die Einstellungen der Packages.  
- "/default/latex/authors.tex" ist für die Titelseite zuständig. Dort müssen die Namen noch geändert werden.  
- "/default/latex/custom_commands.tex" enthält alle von euch definierten Commands. Dort sind auch schon 2 Beispiele eingefügt.  
Im Ordner "/default/bib" sind die BibTeX Dateien, die Einträge enthalten, die häufig gebraucht werden.  
Im Ordner "/default/python" sind die Style Dateien für matplotlib. Wenn euch etwas an den Plots stört solltet ihr diese Dateien verändern.  

## example_code

Der Ordner "/example_code" ist dafür da um Code abzuspeichern, den man nicht immer auswendig weiß und an dem man sich orientieren kann. 
Gegebenenfalls kann hierraus auch Code kopiert werden, anstatt in alten Versuchen nachzuschauen wie ein bestimmter Code auszusehen hat.  

Ich kann es empfehlen die Ergebnisse von Rechnungen in einer .json Datei zu speichern anstatt diese mit print() ausgeben zu lassen und immer aus der Konsole kopieren zu müssen. Schaut dafür in "/example_code/python/read_write_json.py".

## V000_Vorlage

Der Ordner "/V000_Vorlage" sollte kopiert und umbenannt werden, wenn man einen neuen Versuch anfängt.  
In "V000_Vorlage/latex" sind alle Dateien die mit LaTeX zu tun haben zu finden.  
Hier ist vor Allem die "main.tex" hervorzuheben. Dort muss das Datum angepasst werden und dort werden alle Dateien eingebunden. (auch die Dateien aus "/default/latex")  
In der "lit.bib" sollten alle Literaturreferenzen eingetragen werden, die für diesen Versuch relevant sind.  

In "/V000_Vorlage/data" sollten alle Messdaten gespeichert werden und eventuell auch die Ergebnisse der Auswertung.  

In "/V000_Vorlage/python" sollten alle Python Dateien abgespeichert werden und es ist empfehlenswert pro Plot bzw. pro Auswertungsteil eine Datei anzulegen.  
Dort ist schon eine Datei mit Code zu finden. Dieser Code ermöglicht es die Datei von überall ausführen zu lassen. (z.B. im Terminal über "python 'datei.py'" oder in VSCode über den Run Button oben rechts)  
Alle Pfade werden vom Versuchsordner angegeben und die Dateien in "/default/python" werden eingebunden.  
Solltet ihr weder Plots in der Python Datei erstellen noch auf eine andere Datei zugreifen, ist der Code unnötig.

Die Datei "/V000_Vorlage/Makefile" ist das Herzstück der Dateistruktur. Über diese könnt ihr mit dem Befehl "make" alle Dateien hintereinander ausführen lassen und könnt so den ganzen Versuch builden.  
Mit "make plots" sollten alle Plots erstellt werden. Dieser Befehl ist hilfreich wenn man nicht die ganze PDF erstellen möchte, da dies sehr lange dauert.  
Es ist empfehlenswert die Make Datei immer aktuell zu halten und bei jeder neu erstellten Datei das "Makefile" zu aktualisieren.  
