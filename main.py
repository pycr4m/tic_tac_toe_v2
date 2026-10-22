import random

def main():
    brett = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    zugnummer = 0
    begruessung()                                # Zeile 20
    spieler1, spieler2 = spieler_festlegen()     # Zeile 26
    spieler1, spieler2 = beginner_bestimmen(spieler1, spieler2)       # Zeile 49

    punktestand_spieler1 = 0
    punktestand_spieler2 = 0


    while True:
        spielfeld_ausgeben(brett)
        brett, zugnummer = zug_abfragen(brett, zugnummer, spieler1, spieler2)
        if spielende_pruefen(brett, spieler1, spieler2) == 1:
            punktestand_spieler1 += 1
            break
        elif spielende_pruefen(brett, spieler1, spieler2) == 2:
            punktestand_spieler2 += 1
            break
        else:
            continue

    print("Aktueller Punktestand:")
    print(f"{spieler1.title()}: {punktestand_spieler1} Punkte")
    print(f"{spieler2.title()}: {punktestand_spieler2} Punkte")

    while True:
        neue_runde = input("Soll eine neue Runde gespielt werden? (Y/n) \t:")
        if neue_runde in ["Y", "y", ""]:
            brett = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            zugnummer = 0
            print()
            print("Nun Wechseln der Startpieler!")
            platzhalter_spieler = spieler1
            spieler1 = spieler2
            spieler2 = platzhalter_spieler

            platzhalter_punktestand = punktestand_spieler1
            punktestand_spieler1 = punktestand_spieler2
            punktestand_spieler2 = platzhalter_punktestand

            print(f"\t\033[1;1;36m{spieler1.title()}\033[0m erhält \033[1;1;36mX\033[0m als Symbol und beginnt!")
            print(f"\t\033[1;1;31m{spieler2.title()}\033[0m erhält Symbol \033[1;1;31mO\033[0m und zieht als zweites.")

            while True:
                spielfeld_ausgeben(brett)
                brett, zugnummer = zug_abfragen(brett, zugnummer, spieler1, spieler2)
                if spielende_pruefen(brett, spieler1, spieler2) == 1:
                    punktestand_spieler1 += 1
                    print("Aktueller Punktestand:")
                    print(f"{spieler1.title()}: {punktestand_spieler1} Punkte")
                    print(f"{spieler2.title()}: {punktestand_spieler2} Punkte")
                    break
                elif spielende_pruefen(brett, spieler1, spieler2) == 2:
                    punktestand_spieler2 += 1
                    print("Aktueller Punktestand:")
                    print(f"{spieler1.title()}: {punktestand_spieler1} Punkte")
                    print(f"{spieler2.title()}: {punktestand_spieler2} Punkte")
                    break
                else:
                    continue
        else:
            print("Auf Wiedersehen!")
            break


def begruessung():
    print()
    print("Willkommen zu einer neuen Runde Tic Tac Toe!")
    print()


def spieler_festlegen():
    print()
    print("Nun werden Spieler1 und Spieler2 festgelegt:")
    print()
    spieler1 = input(f"Wie lautet der Name vom ersten Spieler? \t: ")
    spieler2 = input(f"Wie lautet der Name vom zweiten Spieler?\t: ")
    while True:
        if spieler2.title == spieler1.title:
            print()
            print(f"Gib einen anderen Namen als Spieler1 \033[1;1;36m{spieler1.title()}\033[0m ein!")
            print()
        else:
            break
    print()
    print("SUPER!")
    print()
    print(f"\033[1;1;33m{spieler1.title()}\033[0m")
    print("und")
    print(f"\033[1;1;33m{spieler2.title()}\033[0m")
    print("sind unsere beiden Spieler!")
    return spieler1, spieler2

def beginner_bestimmen(spieler1, spieler2):
    print()
    print("Nun wird ausgelost, wer anfängt:")
    print()
    print("Wir werfen eine \033[1;1;33mMünze\033[0m.")
    print()
    print(f"\033[1;1mKopf\033[0m heißt {spieler1.title()} fängt an und \033[1;1mZahl\033[0m bedeutet, dass {spieler2.title()} anfängt.")
    print()
    muenzwurf1 = random.choice(["Kopf","Zahl"])
    if muenzwurf1 == "Kopf":
        print(f"Es wurde \033[1;1;33m{muenzwurf1}\033[0m geworfen! : ")
        print(f"\t\033[1;1;36m{spieler1.title()}\033[0m erhält \033[1;1;36mX\033[0m als Symbol und beginnt!")
        print(f"\t\033[1;1;31m{spieler2.title()}\033[0m erhält Symbol \033[1;1;31mO\033[0m und zieht als zweites.")
        return spieler1, spieler2
    else:
        print(f"Es wurde \033[1;1;33m{muenzwurf1}\033[0m geworfen! : ")
        print(f"\033[1;1;36m{spieler2.title()}\033[0m erhält \033[1;1;36mX\033[0m als Symbol und beginnt!")
        print(f"\033[1;1;31m{spieler1.title()}\033[0m erhält Symbol \033[1;1;31mO\033[0m und zieht als zweites.")
        platzhalter = spieler1
        spieler1 = spieler2
        spieler2 = platzhalter
        return spieler1, spieler2

def spielfeld_ausgeben(brett):
    if brett[0] == "X":
        f1_z1_0 = "\033[1;36mooo    ooo\033[0m"
        f1_z2_0 = "\033[1;36m  oo  oo  \033[0m"
        f1_z3_0 = "\033[1;36m    oo    \033[0m"
        f1_z4_0 = "\033[1;36m  oo  oo  \033[0m"
        f1_z5_0 = "\033[1;36mooo    ooo\033[0m"
    elif brett[0] == "O":
        f1_z1_0 = "\033[1;31m   oooo   \033[0m"
        f1_z2_0 = "\033[1;31m ooo  ooo \033[0m"
        f1_z3_0 = "\033[1;31mooo    ooo\033[0m"
        f1_z4_0 = "\033[1;31m ooo  ooo \033[0m"
        f1_z5_0 = "\033[1;31m   oooo   \033[0m"
    else:
        f1_z1_0 = "\033[1;33m     o    \033[0m"
        f1_z2_0 = "\033[1;33m    oo    \033[0m"
        f1_z3_0 = "\033[1;33m   o o    \033[0m"
        f1_z4_0 = "\033[1;33m     o    \033[0m"
        f1_z5_0 = "\033[1;33m   oooo   \033[0m"

    if brett[1] == "X":
        f2_z1_0 = "\033[1;36mooo    ooo\033[0m"
        f2_z2_0 = "\033[1;36m  oo  oo  \033[0m"
        f2_z3_0 = "\033[1;36m    oo    \033[0m"
        f2_z4_0 = "\033[1;36m  oo  oo  \033[0m"
        f2_z5_0 = "\033[1;36mooo    ooo\033[0m"
    elif brett[1] == "O":
        f2_z1_0 = "\033[1;31m   oooo   \033[0m"
        f2_z2_0 = "\033[1;31m ooo  ooo \033[0m"
        f2_z3_0 = "\033[1;31mooo    ooo\033[0m"
        f2_z4_0 = "\033[1;31m ooo  ooo \033[0m"
        f2_z5_0 = "\033[1;31m   oooo   \033[0m"
    else:
        f2_z1_0 = "\033[1;33m    ooo   \033[0m"
        f2_z2_0 = "\033[1;33m   o   o  \033[0m"
        f2_z3_0 = "\033[1;33m      o   \033[0m"
        f2_z4_0 = "\033[1;33m     o    \033[0m"
        f2_z5_0 = "\033[1;33m   ooooo  \033[0m"

    if brett[2] == "X":
        f3_z1_0 = "\033[1;36mooo    ooo\033[0m"
        f3_z2_0 = "\033[1;36m  oo  oo  \033[0m"
        f3_z3_0 = "\033[1;36m    oo    \033[0m"
        f3_z4_0 = "\033[1;36m  oo  oo  \033[0m"
        f3_z5_0 = "\033[1;36mooo    ooo\033[0m"
    elif brett[2] == "O":
        f3_z1_0 = "\033[1;31m   oooo   \033[0m"
        f3_z2_0 = "\033[1;31m ooo  ooo \033[0m"
        f3_z3_0 = "\033[1;31mooo    ooo\033[0m"
        f3_z4_0 = "\033[1;31m ooo  ooo \033[0m"
        f3_z5_0 = "\033[1;31m   oooo   \033[0m"
    else:
        f3_z1_0 = "\033[1;33m    ooo   \033[0m"
        f3_z2_0 = "\033[1;33m   o   o  \033[0m"
        f3_z3_0 = "\033[1;33m     oo   \033[0m"
        f3_z4_0 = "\033[1;33m   o   o  \033[0m"
        f3_z5_0 = "\033[1;33m    ooo   \033[0m"

    if brett[3] == "X":
        f4_z1_0 = "\033[1;36mooo    ooo\033[0m"
        f4_z2_0 = "\033[1;36m  oo  oo  \033[0m"
        f4_z3_0 = "\033[1;36m    oo    \033[0m"
        f4_z4_0 = "\033[1;36m  oo  oo  \033[0m"
        f4_z5_0 = "\033[1;36mooo    ooo\033[0m"
    elif brett[3] == "O":
        f4_z1_0 = "\033[1;31m   oooo   \033[0m"
        f4_z2_0 = "\033[1;31m ooo  ooo \033[0m"
        f4_z3_0 = "\033[1;31mooo    ooo\033[0m"
        f4_z4_0 = "\033[1;31m ooo  ooo \033[0m"
        f4_z5_0 = "\033[1;31m   oooo   \033[0m"
    else:
        f4_z1_0 = "\033[1;33m     oo   \033[0m"
        f4_z2_0 = "\033[1;33m    o o   \033[0m"
        f4_z3_0 = "\033[1;33m   o  o   \033[0m"
        f4_z4_0 = "\033[1;33m  o o o o \033[0m"
        f4_z5_0 = "\033[1;33m      o   \033[0m"

    if brett[4] == "X":
        f5_z1_0 = "\033[1;36mooo    ooo\033[0m"
        f5_z2_0 = "\033[1;36m  oo  oo  \033[0m"
        f5_z3_0 = "\033[1;36m    oo    \033[0m"
        f5_z4_0 = "\033[1;36m  oo  oo  \033[0m"
        f5_z5_0 = "\033[1;36mooo    ooo\033[0m"
    elif brett[4] == "O":
        f5_z1_0 = "\033[1;31m   oooo   \033[0m"
        f5_z2_0 = "\033[1;31m ooo  ooo \033[0m"
        f5_z3_0 = "\033[1;31mooo    ooo\033[0m"
        f5_z4_0 = "\033[1;31m ooo  ooo \033[0m"
        f5_z5_0 = "\033[1;31m   oooo   \033[0m"
    else:
        f5_z1_0 = "\033[1;33m  ooooo   \033[0m"
        f5_z2_0 = "\033[1;33m  o       \033[0m"
        f5_z3_0 = "\033[1;33m  oooo    \033[0m"
        f5_z4_0 = "\033[1;33m      o   \033[0m"
        f5_z5_0 = "\033[1;33m  oooo    \033[0m"

    if brett[5] == "X":
        f6_z1_0 = "\033[1;36mooo    ooo\033[0m"
        f6_z2_0 = "\033[1;36m  oo  oo  \033[0m"
        f6_z3_0 = "\033[1;36m    oo    \033[0m"
        f6_z4_0 = "\033[1;36m  oo  oo  \033[0m"
        f6_z5_0 = "\033[1;36mooo    ooo\033[0m"
    elif brett[5] == "O":
        f6_z1_0 = "\033[1;31m   oooo   \033[0m"
        f6_z2_0 = "\033[1;31m ooo  ooo \033[0m"
        f6_z3_0 = "\033[1;31mooo    ooo\033[0m"
        f6_z4_0 = "\033[1;31m ooo  ooo \033[0m"
        f6_z5_0 = "\033[1;31m   oooo   \033[0m"
    else:
        f6_z1_0 = "\033[1;33m   ooooo  \033[0m"
        f6_z2_0 = "\033[1;33m  o       \033[0m"
        f6_z3_0 = "\033[1;33m  ooooo   \033[0m"
        f6_z4_0 = "\033[1;33m  o    o  \033[0m"
        f6_z5_0 = "\033[1;33m   oooo   \033[0m"

    if brett[6] == "X":
        f7_z1_0 = "\033[1;36mooo    ooo\033[0m"
        f7_z2_0 = "\033[1;36m  oo  oo  \033[0m"
        f7_z3_0 = "\033[1;36m    oo    \033[0m"
        f7_z4_0 = "\033[1;36m  oo  oo  \033[0m"
        f7_z5_0 = "\033[1;36mooo    ooo\033[0m"
    elif brett[6] == "O":
        f7_z1_0 = "\033[1;31m   oooo   \033[0m"
        f7_z2_0 = "\033[1;31m ooo  ooo \033[0m"
        f7_z3_0 = "\033[1;31mooo    ooo\033[0m"
        f7_z4_0 = "\033[1;31m ooo  ooo \033[0m"
        f7_z5_0 = "\033[1;31m   oooo   \033[0m"
    else:
        f7_z1_0 = "\033[1;33m  ooooooo \033[0m"
        f7_z2_0 = "\033[1;33m      o   \033[0m"
        f7_z3_0 = "\033[1;33m    ooo   \033[0m"
        f7_z4_0 = "\033[1;33m    o     \033[0m"
        f7_z5_0 = "\033[1;33m   o      \033[0m"

    if brett[7] == "X":
        f8_z1_0 = "\033[1;36mooo    ooo\033[0m"
        f8_z2_0 = "\033[1;36m  oo  oo  \033[0m"
        f8_z3_0 = "\033[1;36m    oo    \033[0m"
        f8_z4_0 = "\033[1;36m  oo  oo  \033[0m"
        f8_z5_0 = "\033[1;36mooo    ooo\033[0m"
    elif brett[7] == "O":
        f8_z1_0 = "\033[1;31m   oooo   \033[0m"
        f8_z2_0 = "\033[1;31m ooo  ooo \033[0m"
        f8_z3_0 = "\033[1;31mooo    ooo\033[0m"
        f8_z4_0 = "\033[1;31m ooo  ooo \033[0m"
        f8_z5_0 = "\033[1;31m   oooo   \033[0m"
    else:
        f8_z1_0 = "\033[1;33m   oooo   \033[0m"
        f8_z2_0 = "\033[1;33m  o    o  \033[0m"
        f8_z3_0 = "\033[1;33m   oooo   \033[0m"
        f8_z4_0 = "\033[1;33m  o    o  \033[0m"
        f8_z5_0 = "\033[1;33m   oooo   \033[0m"

    if brett[8] == "X":
        f9_z1_0 = "\033[1;36mooo    ooo\033[0m"
        f9_z2_0 = "\033[1;36m  oo  oo  \033[0m"
        f9_z3_0 = "\033[1;36m    oo    \033[0m"
        f9_z4_0 = "\033[1;36m  oo  oo  \033[0m"
        f9_z5_0 = "\033[1;36mooo    ooo\033[0m"
    elif brett[8] == "O":
        f9_z1_0 = "\033[1;31m   oooo   \033[0m"
        f9_z2_0 = "\033[1;31m ooo  ooo \033[0m"
        f9_z3_0 = "\033[1;31mooo    ooo\033[0m"
        f9_z4_0 = "\033[1;31m ooo  ooo \033[0m"
        f9_z5_0 = "\033[1;31m   oooo   \033[0m"
    else:
        f9_z1_0 = "\033[1;33m    ooo   \033[0m"
        f9_z2_0 = "\033[1;33m   o   o  \033[0m"
        f9_z3_0 = "\033[1;33m    o oo  \033[0m"
        f9_z4_0 = "\033[1;33m       o  \033[0m"
        f9_z5_0 = "\033[1;33m    ooo   \033[0m"

    zeile1 = "|================================|"
    zeile2 = "|"+f7_z1_0+"|"+f8_z1_0+"|"+f9_z1_0+"|"
    zeile3 = "|"+f7_z2_0+"|"+f8_z2_0+"|"+f9_z2_0+"|"
    zeile4 = "|"+f7_z3_0+"|"+f8_z3_0+"|"+f9_z3_0+"|"
    zeile5 = "|"+f7_z4_0+"|"+f8_z4_0+"|"+f9_z4_0+"|"
    zeile6 = "|"+f7_z5_0+"|"+f8_z5_0+"|"+f9_z5_0+"|"
    zeile7 = "|================================|"
    zeile8 = "|"+f4_z1_0+"|"+f5_z1_0+"|"+f6_z1_0+"|"
    zeile9 = "|"+f4_z2_0+"|"+f5_z2_0+"|"+f6_z2_0+"|"
    zeile10 = "|"+f4_z3_0+"|"+f5_z3_0+"|"+f6_z3_0+"|"
    zeile11 = "|"+f4_z4_0+"|"+f5_z4_0+"|"+f6_z4_0+"|"
    zeile12 = "|"+f4_z5_0+"|"+f5_z5_0+"|"+f6_z5_0+"|"
    zeile13 = "|================================|"
    zeile14 = "|"+f1_z1_0+"|"+f2_z1_0+"|"+f3_z1_0+"|"
    zeile15 = "|"+f1_z2_0+"|"+f2_z2_0+"|"+f3_z2_0+"|"
    zeile16 = "|"+f1_z3_0+"|"+f2_z3_0+"|"+f3_z3_0+"|"
    zeile17 = "|"+f1_z4_0+"|"+f2_z4_0+"|"+f3_z4_0+"|"
    zeile18 = "|"+f1_z5_0+"|"+f2_z5_0+"|"+f3_z5_0+"|"
    zeile19 = "|================================|"

    # print("brett aktualisiert")
    print(f"""
    \t\t{zeile1}
    \t\t{zeile2}
    \t\t{zeile3}
    \t\t{zeile4}
    \t\t{zeile5}
    \t\t{zeile6}
    \t\t{zeile7}
    \t\t{zeile8}
    \t\t{zeile9}
    \t\t{zeile10}
    \t\t{zeile11}
    \t\t{zeile12}
    \t\t{zeile13}
    \t\t{zeile14}
    \t\t{zeile15}
    \t\t{zeile16}
    \t\t{zeile17}
    \t\t{zeile18}
    \t\t{zeile19}
    """)

    return f1_z1_0, f1_z2_0, f1_z3_0, f1_z4_0, f1_z5_0, f2_z1_0, f2_z2_0, f2_z3_0, f2_z4_0, f2_z5_0 ,f3_z1_0, f3_z2_0, f3_z3_0, f3_z4_0, f3_z5_0, f4_z1_0, f4_z2_0, f4_z3_0, f4_z4_0, f4_z5_0, f5_z1_0, f5_z2_0, f5_z3_0, f5_z4_0, f5_z5_0, f6_z1_0, f6_z2_0, f6_z3_0, f6_z4_0, f6_z5_0, f7_z1_0, f7_z2_0, f7_z3_0, f7_z4_0, f7_z5_0, f8_z1_0, f8_z2_0, f8_z3_0, f8_z4_0, f8_z5_0, f9_z1_0, f9_z2_0, f9_z3_0, f9_z4_0, f9_z5_0

def zug_abfragen(brett, zugnummer, spieler1, spieler2):
    zugnummer = zugnummer + 1
    if zugnummer in [1, 3, 5, 7, 9]:
        print(f"\033[1;1;36m{spieler1.title()}\033[0m mit \033[1;1;36mX\033[0m ist am Zug!")
    else:
        print(f"\033[1;1;31m{spieler2.title()}\033[0m mit \033[1;1;31mO\033[0m ist am Zug")

    freie_felder = []
    for i in brett:
        if i not in ["X","O"]:
            freie_felder.append(i)

    while True:
        zug = input(f"Welches Feld wählst Du?\t:")
        if int(zug) in freie_felder and zugnummer in [1, 3, 5, 7, 9]:
            brett[int(zug)-1] = "X"
            # print(f"X auf Feld {zug} für Zug Nummer {zugnummer} eingetragen.")
            return brett, zugnummer
        elif int(zug) in freie_felder and zugnummer in [2, 4, 6, 8]:
            brett[int(zug)-1] = "O"
            # print(f"O auf Feld {zug} für Zug Nummer {zugnummer} eingetragen.")
            return brett, zugnummer
        else:
            print(f"Wähle ein freies Feld aus: {freie_felder}")
            continue

def spielende_pruefen(brett, spieler1, spieler2):
    if brett[0] == "X" and brett[1] == "X" and brett[2] == "X":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;36mGLÜCKWUNSCH\033[0m!!! \033[1;1;36m{spieler1.title()}\033[0m hat gewonnen! \033[1;1;36mGLÜCKWUNSCH\033[0m!!!")
        return 1
    if brett[0] == "O" and brett[1] == "O" and brett[2] == "O":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;31mGLÜCKWUNSCH\033[0m!!! \033[1;1;31m{spieler2.title()}\033[0m hat gewonnen! \033[1;1;31mGLÜCKWUNSCH\033[0m!!!")
        return 2
    if brett[3] == "X" and brett[4] == "X" and brett[5] == "X":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;36mGLÜCKWUNSCH\033[0m!!! \033[1;1;36m{spieler1.title()}\033[0m hat gewonnen! \033[1;1;36mGLÜCKWUNSCH\033[0m!!!")
        return 1
    if brett[3] == "O" and brett[4] == "O" and brett[5] == "O":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;31mGLÜCKWUNSCH\033[0m!!! \033[1;1;31m{spieler2.title()}\033[0m hat gewonnen! \033[1;1;31mGLÜCKWUNSCH\033[0m!!!")
        return 2
    if brett[6] == "X" and brett[7] == "X" and brett[8] == "X":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;36mGLÜCKWUNSCH\033[0m!!! \033[1;1;36m{spieler1.title()}\033[0m hat gewonnen! \033[1;1;36mGLÜCKWUNSCH\033[0m!!!")
        return 1
    if brett[6] == "O" and brett[7] == "O" and brett[8] == "O":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;31mGLÜCKWUNSCH\033[0m!!! \033[1;1;31m{spieler2.title()}\033[0m hat gewonnen! \033[1;1;31mGLÜCKWUNSCH\033[0m!!!")
        return 2
    if brett[0] == "X" and brett[4] == "X" and brett[8] == "X":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;36mGLÜCKWUNSCH\033[0m!!! \033[1;1;36m{spieler1.title()}\033[0m hat gewonnen! \033[1;1;36mGLÜCKWUNSCH\033[0m!!!")
        return 1
    if brett[0] == "O" and brett[4] == "O" and brett[8] == "O":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;31mGLÜCKWUNSCH\033[0m!!! \033[1;1;31m{spieler2.title()}\033[0m hat gewonnen! \033[1;1;31mGLÜCKWUNSCH\033[0m!!!")
        return 2
    if brett[2] == "X" and brett[4] == "X" and brett[6] == "X":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;36mGLÜCKWUNSCH\033[0m!!! \033[1;1;36m{spieler1.title()}\033[0m hat gewonnen! \033[1;1;36mGLÜCKWUNSCH\033[0m!!!")
        return 1
    if brett[2] == "O" and brett[4] == "O" and brett[6] == "O":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;31mGLÜCKWUNSCH\033[0m!!! \033[1;1;31m{spieler2.title()}\033[0m hat gewonnen! \033[1;1;31mGLÜCKWUNSCH\033[0m!!!")
        return 2
    if brett[0] == "X" and brett[3] == "X" and brett[6] == "X":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;36mGLÜCKWUNSCH\033[0m!!! \033[1;1;36m{spieler1.title()}\033[0m hat gewonnen! \033[1;1;36mGLÜCKWUNSCH\033[0m!!!")
        return 1
    if brett[0] == "O" and brett[3] == "O" and brett[6] == "O":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;31mGLÜCKWUNSCH\033[0m!!! \033[1;1;31m{spieler2.title()}\033[0m hat gewonnen! \033[1;1;31mGLÜCKWUNSCH\033[0m!!!")
        return 2
    if brett[1] == "X" and brett[4] == "X" and brett[7] == "X":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;36mGLÜCKWUNSCH\033[0m!!! \033[1;1;36m{spieler1.title()}\033[0m hat gewonnen! \033[1;1;36mGLÜCKWUNSCH\033[0m!!!")
        return 1
    if brett[1] == "O" and brett[4] == "O" and brett[7] == "O":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;31mGLÜCKWUNSCH\033[0m!!! \033[1;1;31m{spieler2.title()}\033[0m hat gewonnen! \033[1;1;31mGLÜCKWUNSCH\033[0m!!!")
        return 2
    if brett[2] == "X" and brett[5] == "X" and brett[8] == "X":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;36mGLÜCKWUNSCH\033[0m!!! \033[1;1;36m{spieler1.title()}\033[0m hat gewonnen! \033[1;1;36mGLÜCKWUNSCH\033[0m!!!")
        return 1
    if brett[2] == "O" and brett[5] == "O" and brett[8] == "O":
        spielfeld_ausgeben(brett)
        print()
        print(f"\033[1;1;31mGLÜCKWUNSCH\033[0m!!! \033[1;1;31m{spieler2.title()}\033[0m hat gewonnen! \033[1;1;31mGLÜCKWUNSCH\033[0m!!!")
        return 2
    else:
        return 0

main()