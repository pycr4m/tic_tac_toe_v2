def spieler_festlegen():
    print()
    print("Nun werden Spieler1 und Spieler2 festgelegt:")
    print()

    spieler1 = input(f"Name Spieler1?\t: ")
    spieler2 = input(f"Name Spieler2?\t: ")
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
    print(f"\033[1;1;36m{spieler1.title()}\033[0m ist \033[1;1;36mSpieler1\033[0m und bekommt das Symbol \033[1;1;36mX\033[0m!")
    print()
    print("und")
    print()
    print(f"\033[1;1;31m{spieler2.title()}\033[0m ist \033[1;1;31mSpieler2\033[0m und bekommt das Symbol \033[1;1;31mO\033[0m!")