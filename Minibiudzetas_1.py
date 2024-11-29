from datetime import datetime

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
        paj_data = input("Įveskite datą: ")
        paj_pav = input("Įveskite pajamų pavadinimą: ")
        paj_suma = input("Įveskite pajamų sumą: ")
        pajamos.append([paj_data, paj_pav, paj_suma])

