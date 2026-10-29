from tttv2_spielfeld_ausgeben import spielfeld_ausgeben

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
    freie_felder = []
    for i in brett:
        if i not in ["X","O"]:
            freie_felder.append(i)
    if freie_felder == []:
        return 3