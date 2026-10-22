import random
def beginner_bestimmen(spieler1="Spieler1", spieler2="Spieler2"):
    print()
    print("Nun wird ausgelost, wer anfängt:")
    print()
    print("Wir werfen eine Münze.")
    print(f"Kopf heißt {spieler1} fängt an und Zahl bedeutet, dass {spieler2} anfängt.")
    muenzwurf1 = random.choice(["Kopf","Zahl"])
    if muenzwurf1 == "Kopf":
        print(f"Es wurde {muenzwurf1} geworfen: {spieler1} beginnt!")
        return spieler1
    else:
        print(f"Es wurde {muenzwurf1} geworfen: {spieler1} beginnt!")
        return spieler2