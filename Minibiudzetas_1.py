import pickle
import logging
from funkcijos import sumavimas, vidurkis, didziausias, maziausias, trinimas

logging.basicConfig(level=logging.INFO,
                    filename="zurnalas.log",
                    format="%(asctime)s %(levelname)s %(message)s")

pajamos = []
islaidos = []

while True:
    print("--------------------\n"
          "Pagrindinis meniu: \n"
          "1. Įvesti pajamas\n"
          "2. Įvesti išlaidas\n"
          "3. Atspausdinti pajamų eilutes\n"
          "4. Atspausdinti išlaidų eilutes\n"
          "5. Atspausdinti statistiką\n"
          "6. Trinti duomenis\n"
          "7. Duomenų paieška\n"
          "8. Saugoti duomenis į failą\n"
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
        print("Pajamos:")
        for elem in pajamos:
            print(elem)

    if pagr_meniu_pasirinkimas == "4":
        print("Išlaidos:")
        for elem in islaidos:
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

        print(f"Likusi pajamų suma atėmus išlaidas: {sumavimas(pajamos) - sumavimas(islaidos)}")

    if pagr_meniu_pasirinkimas == "6":

        logging.warning("Trinami failai negali buti atkurti!")

        print("Pasirinkite iš kurio sarašo norite ištrinti: \n"
              "1. Pajamos\n"
              "2. Išlaidos\n")

        trinimo_meniu_pasirinkimas = input("> ")

        if trinimo_meniu_pasirinkimas == "1":
            trinimas(pajamos)

        if trinimo_meniu_pasirinkimas == "2":
            trinimas(islaidos)

    if pagr_meniu_pasirinkimas == "7":

        logging.info("Duomenys ieskomi is pajamu ir islaidu saraso")

        iesko = input("Įveskite ieškomą pajamų arba išlaidų šaltinį: ")
        for elem in pajamos:
            if elem[1] == iesko:
                print(f"rasti pajamų duomenys:\n {elem}")
        for elem in islaidos:
            if elem[1] == iesko:
                print(f"rasti išlaidų duomenys:\n {elem}")

    if pagr_meniu_pasirinkimas == "8":
        with open("saug_duom.pickle", mode="wb") as file:
            #  noinspection PyTypeChecker
            pickle.dump(pajamos, file)
            #  noinspection PyTypeChecker
            pickle.dump(islaidos, file)

    if pagr_meniu_pasirinkimas == "q":
        break
