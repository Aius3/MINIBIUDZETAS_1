from datetime import datetime
from funkcijos import sumavimas, vidurkis, didziausias, maziausias

pajamos = []
islaidos = []

while True:
    print("Pagrindinis meniu: \n"
          "1. Įvesti pajamas\n"
          "2. Įvesti išlaidas\n"
          "3. Atspausdinti pajamų eilutes\n"
          "4. Atspausdinti išlaidų eilutes\n"
          "5. Atspausdinti statistiką\n"
          "q - išeiti\n")
    pagr_meniu_pasirinkimas = input("> ")

    if pagr_meniu_pasirinkimas == "1":
        data = input("Įveskite datą: ")
        pav = input("Įveskite pajamų pavadinimą: ")
        suma = input("Įveskite pajamų sumą: ")
        pajamos.append([data, pav, suma])

    if pagr_meniu_pasirinkimas == "2":
        data = input("Įveskite datą: ")
        pav = input("Įveskite išlaidų pavadinimą: ")
        suma = input("Įveskite išlaidų sumą: ")
        islaidos.append([data, pav, suma])

    if pagr_meniu_pasirinkimas == "3":
        for elem in pajamos:
            print("Pajamos:")
            print(elem)

    if pagr_meniu_pasirinkimas == "4":
        for elem in islaidos:
            print("Išlaidos:")
            print(elem)

    if pagr_meniu_pasirinkimas == "5":

        print(f"Visų pajamų šaltinių suma: {sumavimas(pajamos)}")
        print(f"Visų pajamų šaltinių vidurkis: {vidurkis(pajamos)}")
        print(f"Didžiausias pajamų šaltinis: {didziausias(pajamos)}")
        print(f"Mažaiausias pajamų šaltinis: {maziausias(pajamos)}")

        print(f"Visų išlaidų šaltinių suma: {sumavimas(islaidos)}")
        print(f"Visų pajamų šaltinių vidurkis: {vidurkis(islaidos)}")
        print(f"Didžiausias išlaidų šaltinis: {didziausias(islaidos)}")
        print(f"Mažaiausias išlaidų šaltinis: {maziausias(islaidos)}")

        print(f"Likusi pajamų suma atėmus išlaidas: {sumavimas(pajamos)-sumavimas(islaidos)}")

    if pagr_meniu_pasirinkimas == "q":
        break
