import random

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
        print(f"\t\033[1;1;36m{spieler1.title()}\033[0m erhält \033[1;1;36mX\033[0m als Symbol und beginnt.")
        print(f"\t\033[1;1;31m{spieler2.title()}\033[0m erhält Symbol \033[1;1;31mO\033[0m und zieht als zweites.")
        return spieler1, spieler2
    else:
        print(f"Es wurde \033[1;1;33m{muenzwurf1}\033[0m geworfen! : ")
        print(f"\033[1;1;36m{spieler2.title()}\033[0m erhält \033[1;1;36mX\033[0m als Symbol und beginnt.")
        print(f"\033[1;1;31m{spieler1.title()}\033[0m erhält Symbol \033[1;1;31mO\033[0m und zieht als zweites.")
        platzhalter = spieler1
        spieler1 = spieler2
        spieler2 = platzhalter
        return spieler1, spieler2