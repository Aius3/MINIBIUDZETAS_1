def sumavimas(tipas):
    suma = 0
    for elem in tipas:
        suma += int(elem[2])
    return suma


def vidurkis(tipas):
    suma = 0
    for elem in tipas:
        suma += int(elem[2])
    if len(tipas) > 0:
        return suma / len(tipas)
    else:
        return 0


def didziausias(tipas):
    if len(tipas) > 0:
        didz = int(tipas[0][2])
        didz_pav = tipas[0][1]
        for elem in tipas:
            ar_didz = int(elem[2])
            if ar_didz > didz:
                didz = ar_didz
                didz_pav = elem[1]
        return f"{didz_pav} - {didz}"
    else:
        return 0


def maziausias(tipas):
    if len(tipas) > 0:
        maz = int(tipas[0][2])
        maz_pav = tipas[0][1]
        for elem in tipas:
            ar_maz = int(elem[2])
            if ar_maz < maz:
                maz = ar_maz
                maz_pav = elem[1]
        return f"{maz_pav} - {maz}"
    else:
        return 0


def trinimas(tipas):
    print("Pasirinkite kurį sąrašą trinti: ")
    for num, elem in enumerate(tipas, start=1):
        print(f"{num}. {elem}")
    if tipas:
        trint = input("> ")
        del tipas[int(trint) - 1]
    else:
        print("Sąrašas tuščias!")
