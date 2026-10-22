# Hauptprogramm
import random
from begruessung import begruessung
from spieler_festlegen import spieler_festlegen
from beginner_bestimmen import beginner_bestimmen
from spielfeld_ausgeben import spielfeld_ausgeben
brett = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    begruessung()
    spieler_festlegen()
    beginner_bestimmen() 
    spielfeld_ausgeben(brett)
        # schleife:
            # zug abfragen
            # zug überprüfen
            # gewinnkondition prüfen
        # ergebnis ausgeben


main()