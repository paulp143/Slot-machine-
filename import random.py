import random
# Nächster Schritt:
#   Das gesamte system mit try und except ausstatten. Um Fehler auszuschließen.
while True:
    wheel = input("Auf welches Wheel möchtest du setzen? (3, 4, 5) ")
    try:
        wheel=int(wheel)
        if wheel==3 or wheel==4 or wheel==5:
            break
        else:
            print("The wheel has to be either 3, 4 or 5")
    except ValueError:
        print("Invalid Input, Try again")


modus = input("Modus wählen (spins/geld): ").lower()

gewonnenes_geld=0
verlorenes_geld=0
gewonnen = 0
verloren = 0
spins = 0

if modus == "spins":
    max_spins = int(input("Wie viele Spins möchtest du spielen? "))

    for spin in range(max_spins):
        results = [random.randint(1, 3) for _ in range(wheel)]

        if len(set(results)) == 1:
            print(f"Spin {spin + 1}: {results} WIN")
            gewonnen += 1
        else:
            print(f"Spin {spin + 1}: {results} LOSE")
            verloren += 1

    spins = max_spins

elif modus == "geld":
    geld = int(input("Startkapital: "))
    einsatz = int(input("Einsatz pro Spin: "))

    if wheel == 3:
        multiplikator = 5
    elif wheel == 4:
        multiplikator = 20
    else:
        multiplikator = 100

    while geld >= einsatz:
        spins += 1
        geld -= einsatz

        results = [random.randint(1, 3) for _ in range(wheel)]

        if len(set(results)) == 1:
            gewinn = einsatz * multiplikator
            geld += gewinn

            print(
                f"Spin {spins}: {results} WIN +{gewinn}€ | Guthaben: {geld}€"
            )
            gewonnen += 1
            gewonnenes_geld+=gewinn
        else:
            print(
                f"Spin {spins}: {results} LOSE | Guthaben: {geld}€"
            )
            verloren += 1
            verlorenes_geld+=geld

    print(f"\nKein Geld mehr übrig. Endguthaben: {geld}€")

else:
    print("Ungültiger Modus.")
    exit()

print("\n----- Stats -----")
print(f"Spins: {spins}")
print(f"Gewonnen: {gewonnen}")
print(f"Verloren: {verloren}")
if modus=="geld":
    print(f"Gewonnenes Geld: {gewonnenes_geld}€")
    print(f"Verlorenes Geld: {verlorenes_geld}€")

if spins > 0:
    print(f"Gewinnquote: {(gewonnen / spins) * 100:.2f}%")
