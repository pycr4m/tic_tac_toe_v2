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
        try:
            zug = input(f"Welches Feld wählst Du?\t:")
            if str(zug) == "q" or zug == "Q":
                return "q", "q"
            elif int(zug) in freie_felder and zugnummer in [1, 3, 5, 7, 9]:
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
        except ValueError:
            print(f"Wähle ein freies Feld aus: {freie_felder}")