from tttv2_begruessung import begruessung
from tttv2_spielerfestlegen import spieler_festlegen
from tttv2_beginner_bestimmen import beginner_bestimmen
from tttv2_spielfeld_ausgeben import spielfeld_ausgeben
from tttv2_zug_abfragen import zug_abfragen
from tttv2_spielende_pruefen import spielende_pruefen

def main():
    brett = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    zugnummer = 0
    runde = 1
    noch_einmal_spielen = "ja"
    punktestand_spieler1 = 0
    punktestand_spieler2 = 0

    begruessung()
    spieler1, spieler2 = spieler_festlegen()
    if spieler1 == "q" and spieler2 == "q":
        print()
        print("Auf Wiedersehen")
        noch_einmal_spielen = "nein"

    if noch_einmal_spielen == "ja":
        spieler1, spieler2 = beginner_bestimmen(spieler1, spieler2)
        print(f"Runde {runde} beginnt! ")

        while noch_einmal_spielen == "ja":
            spielfeld_ausgeben(brett)
            brett, zugnummer = zug_abfragen(brett, zugnummer, spieler1, spieler2)
            if brett == "q" and zugnummer == "q":
                noch_einmal_spielen = "nein"
                print()
                print("Auf Wiedersehen!")
                break
            elif spielende_pruefen(brett, spieler1, spieler2) == 1:
                punktestand_spieler1 += 1
                print()
                print("Aktueller Punktestand:")
                print(f"{spieler1.title()}: {punktestand_spieler1} Punkt(/e)")
                print(f"{spieler2.title()}: {punktestand_spieler2} Punkt(/e)")
                print()
                break
            elif spielende_pruefen(brett, spieler1, spieler2) == 2:
                punktestand_spieler2 += 1
                print()
                print("Aktueller Punktestand:")
                print(f"{spieler1.title()}: {punktestand_spieler1} Punkt(/e)")
                print(f"{spieler2.title()}: {punktestand_spieler2} Punkt(/e)")
                print()
                break
            elif spielende_pruefen(brett, spieler1, spieler2) == 3:
                punktestand_spieler2 += 1
                punktestand_spieler1 += 1
                print()
                print("WOW! \033[1;1;33mUnentschieden\033[0m!!! ")
                print("Beide Spieler erhalten 1 Punkt.")
                print()
                print("Aktueller Punktestand:")
                print(f"{spieler1.title()}: {punktestand_spieler1} Punkt(/e)")
                print(f"{spieler2.title()}: {punktestand_spieler2} Punkt(/e)")
                print()
                break
            else:
                continue

        while noch_einmal_spielen == "ja":
            while True:
                neue_runde = input("Soll eine neue Runde gespielt werden? (Y/q) \t:")
                if neue_runde in ["Y", "y", "", "Q", "q"]:
                    break
                else:
                    print("Gib \"Y\" für eine neue Runde und \"q\" zum Beenden ein!")
                    continue

            if neue_runde in ["Y", "y", ""]:
                brett = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                zugnummer = 0
                runde += 1
                print()
                print("Nun Wechselt der Startpieler!")

                platzhalter_spieler = spieler1
                spieler1 = spieler2
                spieler2 = platzhalter_spieler

                platzhalter_punktestand = punktestand_spieler1
                punktestand_spieler1 = punktestand_spieler2
                punktestand_spieler2 = platzhalter_punktestand

                print(f"\t\033[1;1;36m{spieler1.title()}\033[0m erhält \033[1;1;36mX\033[0m als Symbol und hat den ersten Zug.")
                print(f"\t\033[1;1;31m{spieler2.title()}\033[0m erhält Symbol \033[1;1;31mO\033[0m und zieht als zweites.")
                print(f"Runde {runde} beginnt! ")

                while True:
                    spielfeld_ausgeben(brett)
                    brett, zugnummer = zug_abfragen(brett, zugnummer, spieler1, spieler2)
                    if brett == "q" and zugnummer == "q":
                                    noch_einmal_spielen = "nein"
                                    print()
                                    print("Auf Wiedersehen!")
                                    break
                    elif spielende_pruefen(brett, spieler1, spieler2) == 1:
                        punktestand_spieler1 += 1
                        print()
                        print("Aktueller Punktestand:")
                        print(f"{spieler1.title()}: {punktestand_spieler1} Punkt(/e)")
                        print(f"{spieler2.title()}: {punktestand_spieler2} Punkt(/e)")
                        print()
                        break
                    elif spielende_pruefen(brett, spieler1, spieler2) == 2:
                        punktestand_spieler2 += 1
                        print()
                        print("Aktueller Punktestand:")
                        print(f"{spieler1.title()}: {punktestand_spieler1} Punkt(/e)")
                        print(f"{spieler2.title()}: {punktestand_spieler2} Punkt(/e)")
                        print()
                        break
                    elif spielende_pruefen(brett, spieler1, spieler2) == 3:
                        punktestand_spieler2 += 1
                        punktestand_spieler1 += 1
                        print()
                        print("WOW! \033[1;1;33mUnentschieden\033[0m!!! ")
                        print("Beide Spieler erhalten 1 Punkt.")
                        print()
                        print("Aktueller Punktestand:")
                        print(f"{spieler1.title()}: {punktestand_spieler1} Punkt(/e)")
                        print(f"{spieler2.title()}: {punktestand_spieler2} Punkt(/e)")
                        print()
                        break
                    else:
                        continue
            else:
                print()
                print("Auf Wiedersehen!")
                break

main()