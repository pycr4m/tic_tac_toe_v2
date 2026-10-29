def spieler_festlegen():
    print()
    print("Nun werden Spieler1 und Spieler2 festgelegt:")
    print()
    spieler1 = input(f"Wie lautet der Name vom ersten Spieler? \t: ")
    if spieler1 == "q" or spieler1 == "Q":
        return "q","q"
    spieler2 = input(f"Wie lautet der Name vom zweiten Spieler?\t: ")
    while True:
        if spieler2.title == spieler1.title:
            print()
            print(f"Gib einen anderen Namen als Spieler1 \033[1;1;36m{spieler1.title()}\033[0m ein!")
            print()
        else:
            break
    if spieler2 == "q" or spieler2 == "Q":
        return "q","q"
    print()
    print("SUPER!")
    print()
    print(f"\033[1;1;33m{spieler1.title()}\033[0m")
    print("und")
    print(f"\033[1;1;33m{spieler2.title()}\033[0m")
    print("sind unsere beiden Spieler!")
    return spieler1, spieler2